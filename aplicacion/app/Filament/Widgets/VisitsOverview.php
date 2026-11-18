<?php

namespace App\Filament\Widgets;

use App\Support\VisitAnalytics;
use Filament\Widgets\StatsOverviewWidget;
use Filament\Widgets\StatsOverviewWidget\Stat;
use Throwable;

class VisitsOverview extends StatsOverviewWidget
{
    protected static ?int $sort = 1;

    protected ?string $pollingInterval = '20s';

    protected int|array|null $columns = [
        'default' => 1,
        'sm' => 2,
        'lg' => 4,
    ];

    protected function getStats(): array
    {
        try {
            return $this->cards(VisitAnalytics::snapshot());
        } catch (Throwable) {
            return [
                Stat::make('Visitas', '—')->description('No se pudieron cargar las métricas')->color('gray'),
            ];
        }
    }

    /**
     * @param  array<string, mixed>  $s
     * @return array<Stat>
     */
    private function cards(array $s): array
    {
        $hourly = collect($s['hourly_today'] ?? [])->pluck('visits')->map(fn ($v) => (float) $v)->all();
        $daily = collect($s['daily'] ?? [])->pluck('visits')->map(fn ($v) => (float) $v)->all();
        $dailyUnique = collect($s['daily'] ?? [])->pluck('unique')->map(fn ($v) => (float) $v)->all();
        $today = (int) ($s['today_visits'] ?? 0);
        $yesterday = (int) ($s['yesterday_visits'] ?? 0);
        $online = (int) ($s['online_now'] ?? 0);
        $country = (string) ($s['top_country'] ?? '');

        return [
            Stat::make('En línea', number_format($online))
                ->description(number_format((int) ($s['online_hits'] ?? 0)).' páginas · últimos 5 min')
                ->descriptionIcon('heroicon-m-signal')
                ->color($online > 0 ? 'success' : 'gray')
                ->chart($hourly),

            Stat::make('Hoy', number_format($today))
                ->description($this->comparison($today, $yesterday))
                ->descriptionIcon($today >= $yesterday ? 'heroicon-m-arrow-trending-up' : 'heroicon-m-arrow-trending-down')
                ->color($today >= $yesterday ? 'primary' : 'danger')
                ->chart($hourly),

            Stat::make('IPs únicas hoy', number_format((int) ($s['today_unique'] ?? 0)))
                ->description('Visitantes distintos')
                ->descriptionIcon('heroicon-m-globe-alt')
                ->color('warning')
                ->chart($dailyUnique),

            Stat::make('Ayer', number_format($yesterday))
                ->description('Día completo')
                ->descriptionIcon('heroicon-m-clock')
                ->color('gray'),

            Stat::make('Últimos 7 días', number_format((int) ($s['week_visits'] ?? 0)))
                ->description(number_format((int) ($s['week_unique'] ?? 0)).' IPs únicas')
                ->descriptionIcon('heroicon-m-calendar-days')
                ->color('info')
                ->chart($daily),

            Stat::make('Últimos 30 días', number_format((int) ($s['month_visits'] ?? 0)))
                ->description(number_format((int) ($s['month_unique'] ?? 0)).' IPs únicas · promedio '.number_format((int) ($s['week_average'] ?? 0)).'/día')
                ->descriptionIcon('heroicon-m-calendar')
                ->color('info')
                ->chart($daily),

            Stat::make('País principal', $country !== '' ? $country : 'Sin ubicación')
                ->description($country !== '' ? number_format((int) ($s['top_country_visits'] ?? 0)).' visitas en 7 días' : 'Se completa cuando la visita llega desde internet')
                ->descriptionIcon('heroicon-m-map-pin')
                ->color('success'),

            Stat::make('Total', number_format((int) ($s['total_visits'] ?? 0)))
                ->description(number_format((int) ($s['unique_ips'] ?? 0)).' IPs únicas desde el inicio')
                ->descriptionIcon('heroicon-m-chart-bar')
                ->color('gray')
                ->chart($daily),
        ];
    }

    private function comparison(int $today, int $yesterday): string
    {
        if ($yesterday === 0) {
            return $today > 0 ? 'Hoy ya supera a ayer' : 'Sin visitas ayer';
        }

        $diff = (int) round((($today - $yesterday) / $yesterday) * 100);

        return match (true) {
            $diff > 0 => "Hoy va {$diff}% arriba de ayer",
            $diff < 0 => 'Hoy va '.abs($diff).'% abajo de ayer',
            default => 'Hoy va igual que ayer',
        };
    }
}
