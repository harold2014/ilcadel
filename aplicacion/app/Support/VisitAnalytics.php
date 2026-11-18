<?php

namespace App\Support;

use App\Models\PageVisit;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use Throwable;

class VisitAnalytics
{
    private const CACHE_KEY = 'visits.snapshot';

    /**
     * @return array<string, mixed>
     */
    public static function snapshot(): array
    {
        try {
            return Cache::remember(self::CACHE_KEY, 15, fn (): array => self::build());
        } catch (Throwable) {
            return self::build();
        }
    }

    public static function flush(): void
    {
        try {
            Cache::forget(self::CACHE_KEY);
        } catch (Throwable) {
        }
    }

    /**
     * @return array<string, mixed>
     */
    private static function build(): array
    {
        $now = now();
        $todayStart = $now->copy()->startOfDay();
        $yesterdayStart = $now->copy()->subDay()->startOfDay();
        $weekStart = $now->copy()->subDays(6)->startOfDay();
        $monthStart = $now->copy()->subDays(29)->startOfDay();
        $weekVisits = self::countSince($weekStart);
        $topCountry = self::topCountry($weekStart);

        return [
            'online_now' => self::distinctSince($now->copy()->subMinutes(5)),
            'online_hits' => self::countSince($now->copy()->subMinutes(5)),
            'total_visits' => (int) PageVisit::query()->count(),
            'unique_ips' => self::distinctSince(null),
            'today_visits' => self::countSince($todayStart),
            'today_unique' => self::distinctSince($todayStart),
            'yesterday_visits' => (int) PageVisit::query()
                ->where('created_at', '>=', $yesterdayStart)
                ->where('created_at', '<', $todayStart)
                ->count(),
            'week_visits' => $weekVisits,
            'week_unique' => self::distinctSince($weekStart),
            'week_average' => (int) round($weekVisits / 7),
            'month_visits' => self::countSince($monthStart),
            'month_unique' => self::distinctSince($monthStart),
            'top_country' => $topCountry['country'] ?? null,
            'top_country_visits' => (int) ($topCountry['visits'] ?? 0),
            'top_pages' => self::topPages($weekStart, 8),
            'top_referers' => self::topReferers($weekStart, 8),
            'devices' => self::topGrouped('device', $weekStart, 5),
            'hourly_today' => self::hourlyToday($todayStart),
            'daily' => self::dailySeries(14),
        ];
    }

    private static function countSince(?Carbon $since): int
    {
        $query = PageVisit::query();
        if ($since) {
            $query->where('created_at', '>=', $since);
        }

        return (int) $query->count();
    }

    private static function distinctSince(?Carbon $since): int
    {
        $query = PageVisit::query();
        if ($since) {
            $query->where('created_at', '>=', $since);
        }

        return (int) $query->distinct()->count('ip_hash');
    }

    /**
     * @return array{country: string, visits: int}|null
     */
    private static function topCountry(Carbon $since): ?array
    {
        $row = PageVisit::query()
            ->select('country', DB::raw('COUNT(*) as visits'))
            ->where('created_at', '>=', $since)
            ->whereNotNull('country')
            ->where('country', '!=', '')
            ->groupBy('country')
            ->orderByDesc('visits')
            ->first();

        if (! $row) {
            return null;
        }

        return ['country' => (string) $row->country, 'visits' => (int) $row->visits];
    }

    /**
     * @return list<array{page: string, visits: int}>
     */
    private static function topPages(Carbon $since, int $limit): array
    {
        $expr = "COALESCE(NULLIF(section, ''), path)";
        $pages = PageVisit::query()
            ->selectRaw($expr.' as page')
            ->where('created_at', '>=', $since);

        return DB::query()
            ->fromSub($pages, 'pages')
            ->selectRaw('page, COUNT(*) as visits')
            ->groupBy('page')
            ->orderByDesc('visits')
            ->limit($limit)
            ->get()
            ->map(fn ($row) => [
                'page' => self::pageLabel((string) $row->page),
                'visits' => (int) $row->visits,
            ])
            ->all();
    }

    /**
     * @return list<array{device: string, visits: int}>
     */
    private static function topGrouped(string $column, Carbon $since, int $limit): array
    {
        return PageVisit::query()
            ->select($column, DB::raw('COUNT(*) as visits'))
            ->where('created_at', '>=', $since)
            ->whereNotNull($column)
            ->where($column, '!=', '')
            ->groupBy($column)
            ->orderByDesc('visits')
            ->limit($limit)
            ->get()
            ->map(fn ($row) => [
                $column => (string) $row->{$column},
                'visits' => (int) $row->visits,
            ])
            ->all();
    }

    /**
     * @return list<array{referer: string, visits: int}>
     */
    private static function topReferers(Carbon $since, int $limit): array
    {
        return PageVisit::query()
            ->select('referer', DB::raw('COUNT(*) as visits'))
            ->where('created_at', '>=', $since)
            ->groupBy('referer')
            ->get()
            ->groupBy(fn ($row): string => self::refererLabel($row->referer))
            ->map(fn ($rows): int => (int) $rows->sum('visits'))
            ->sortDesc()
            ->take($limit)
            ->map(fn (int $visits, string $label): array => [
                'referer' => $label,
                'visits' => $visits,
            ])
            ->values()
            ->all();
    }

    /**
     * @return list<array{hour: string, visits: int}>
     */
    private static function hourlyToday(Carbon $todayStart): array
    {
        $hour = self::hourExpression();
        $rows = PageVisit::query()
            ->select(DB::raw($hour.' as hour'), DB::raw('COUNT(*) as visits'))
            ->where('created_at', '>=', $todayStart)
            ->groupBy(DB::raw($hour))
            ->pluck('visits', 'hour');

        $out = [];
        for ($h = 0; $h < 24; $h++) {
            $out[] = [
                'hour' => str_pad((string) $h, 2, '0', STR_PAD_LEFT).':00',
                'visits' => (int) ($rows[$h] ?? $rows[(string) $h] ?? 0),
            ];
        }

        return $out;
    }

    /**
     * @return list<array{label: string, visits: int, unique: int}>
     */
    public static function dailySeries(int $days = 14): array
    {
        $start = now()->subDays($days - 1)->startOfDay();
        $day = self::dayExpression();
        $rows = PageVisit::query()
            ->select(
                DB::raw($day.' as day'),
                DB::raw('COUNT(*) as visits'),
                DB::raw('COUNT(DISTINCT ip_hash) as unique_ips'),
            )
            ->where('created_at', '>=', $start)
            ->groupBy(DB::raw($day))
            ->get()
            ->keyBy(fn ($row) => Carbon::parse($row->day)->toDateString());

        $out = [];
        for ($i = 0; $i < $days; $i++) {
            $date = $start->copy()->addDays($i);
            $row = $rows->get($date->toDateString());
            $out[] = [
                'label' => $date->format('d/m'),
                'visits' => (int) ($row->visits ?? 0),
                'unique' => (int) ($row->unique_ips ?? 0),
            ];
        }

        return $out;
    }

    public static function detectDevice(?string $ua): string
    {
        $ua = strtolower((string) $ua);
        if ($ua === '') {
            return 'otro';
        }
        if (str_contains($ua, 'tablet') || str_contains($ua, 'ipad')) {
            return 'tablet';
        }
        if (str_contains($ua, 'mobi') || str_contains($ua, 'android') || str_contains($ua, 'iphone')) {
            return 'mobile';
        }

        return 'desktop';
    }

    public static function deviceLabel(?string $device): string
    {
        return match ($device) {
            'desktop' => 'Escritorio',
            'mobile' => 'Celular',
            'tablet' => 'Tablet',
            default => 'Otro',
        };
    }

    public static function sectionFromPath(string $path): string
    {
        $page = self::normalizePage($path);

        return match ($page) {
            '', 'index' => 'inicio',
            default => $page,
        };
    }

    public static function pageLabel(string $page): string
    {
        $page = self::normalizePage($page);

        return match ($page) {
            '', 'index', 'inicio' => 'Inicio',
            'institucion' => 'Nosotros',
            'arbitraje' => 'Arbitraje',
            'conciliacion' => 'Conciliación',
            'defensa-legal' => 'Defensa legal',
            'certificaciones' => 'Certificaciones',
            'contacto' => 'Contacto',
            'galeria' => 'Galería',
            'mesa-de-partes' => 'Mesa de partes',
            'consulta' => 'Consulta',
            'reclamaciones', 'libro-de-reclamaciones' => 'Libro de reclamaciones',
            default => Str::limit($page, 32),
        };
    }

    public static function refererLabel(?string $referer): string
    {
        $referer = trim((string) $referer);
        if ($referer === '') {
            return 'Directo';
        }

        $host = parse_url($referer, PHP_URL_HOST);
        if (! $host) {
            return Str::limit($referer, 40);
        }

        $host = Str::lower(Str::replaceStart('www.', '', $host));
        $site = parse_url((string) config('app.url'), PHP_URL_HOST);
        $site = $site ? Str::lower(Str::replaceStart('www.', '', $site)) : '';

        return $host === $site ? 'Navegación interna' : $host;
    }

    public static function isBot(?string $ua): bool
    {
        $ua = strtolower(trim((string) $ua));
        if ($ua === '') {
            return true;
        }

        foreach (['bot', 'spider', 'crawl', 'slurp', 'facebookexternalhit', 'preview', 'wget', 'curl', 'python-requests'] as $needle) {
            if (str_contains($ua, $needle)) {
                return true;
            }
        }

        return false;
    }

    public static function ipHash(string $ip): string
    {
        return hash('sha256', $ip.'|'.config('app.key'));
    }

    private static function normalizePage(string $page): string
    {
        $page = strtolower(trim($page));
        $page = trim($page, '/');
        $page = preg_replace('/\.html$/', '', $page) ?? $page;

        return $page;
    }

    private static function hourExpression(): string
    {
        return DB::connection()->getDriverName() === 'sqlite'
            ? "cast(strftime('%H', created_at) as integer)"
            : 'HOUR(created_at)';
    }

    private static function dayExpression(): string
    {
        return DB::connection()->getDriverName() === 'sqlite'
            ? 'date(created_at)'
            : 'DATE(created_at)';
    }
}
