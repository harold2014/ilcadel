<?php

namespace App\Http\Middleware;

use App\Models\PageVisit;
use App\Models\PageVisitIp;
use App\Support\GeoIp;
use App\Support\VisitAnalytics;
use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;
use Throwable;

class TrackPageVisit
{
    public function handle(Request $request, Closure $next): Response
    {
        $response = $next($request);

        if (! $this->shouldTrack($request, $response)) {
            return $response;
        }

        try {
            $ip = (string) ($request->ip() ?: '0.0.0.0');
            $path = '/'.ltrim($request->path(), '/');
            $visit = PageVisit::query()->create([
                'path' => $path === '//' ? '/' : $path,
                'referer' => substr((string) $request->headers->get('referer'), 0, 255) ?: null,
                'ip_hash' => VisitAnalytics::ipHash($ip),
                'device' => VisitAnalytics::detectDevice($request->userAgent()),
                'section' => VisitAnalytics::sectionFromPath($path),
                'created_at' => now(),
            ]);

            PageVisitIp::query()->updateOrCreate(
                ['ip_hash' => $visit->ip_hash],
                ['last_seen' => now()],
            );

            VisitAnalytics::flush();

            $visitId = $visit->id;
            app()->terminating(function () use ($visitId, $ip): void {
                try {
                    $place = GeoIp::lookup($ip);
                    if ($place['country'] || $place['city']) {
                        PageVisit::query()->whereKey($visitId)->update($place);
                        VisitAnalytics::flush();
                    }
                } catch (Throwable) {
                }
            });
        } catch (Throwable) {
        }

        return $response;
    }

    private function shouldTrack(Request $request, Response $response): bool
    {
        if (! $request->isMethod('GET') || ! $response->isSuccessful()) {
            return false;
        }

        $ua = trim((string) $request->userAgent());
        if ($ua === '' || VisitAnalytics::isBot($ua)) {
            return false;
        }

        $path = trim($request->path(), '/');
        if ($path !== '' && (
            str_starts_with($path, 'admin')
            || str_starts_with($path, 'livewire')
            || str_starts_with($path, 'build')
            || str_starts_with($path, 'fonts')
            || str_starts_with($path, 'js')
            || str_starts_with($path, 'css')
            || str_starts_with($path, 'assets')
            || str_starts_with($path, 'referencia')
            || str_starts_with($path, 'storage')
            || str_starts_with($path, 'media')
            || $path === 'up'
            || $path === 'robots.txt'
            || $path === 'sitemap.xml'
            || $path === 'favicon.ico'
        )) {
            return false;
        }

        return ! preg_match('/\.(css|js|map|jpg|jpeg|png|gif|webp|avif|svg|ico|woff2?|ttf|eot|mp4)$/i', $path);
    }
}
