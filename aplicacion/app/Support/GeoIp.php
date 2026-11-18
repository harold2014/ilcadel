<?php

namespace App\Support;

use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Http;

class GeoIp
{
    /**
     * @return array{country: ?string, region: ?string, city: ?string}
     */
    public static function lookup(string $ip): array
    {
        $empty = ['country' => null, 'region' => null, 'city' => null];
        $ip = trim($ip);

        if ($ip === '' || ! filter_var($ip, FILTER_VALIDATE_IP) || self::isPrivate($ip)) {
            return $empty;
        }

        try {
            return Cache::remember('geoip:'.$ip, now()->addDays(14), function () use ($ip, $empty) {
                $response = Http::timeout(2)
                    ->acceptJson()
                    ->get('http://ip-api.com/json/'.$ip, [
                        'fields' => 'status,country,regionName,city',
                        'lang' => 'es',
                    ]);

                if (! $response->ok() || ($response->json('status') !== 'success')) {
                    return $empty;
                }

                return [
                    'country' => self::clip($response->json('country')),
                    'region' => self::clip($response->json('regionName')),
                    'city' => self::clip($response->json('city')),
                ];
            });
        } catch (\Throwable) {
            return $empty;
        }
    }

    private static function isPrivate(string $ip): bool
    {
        return ! filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE);
    }

    private static function clip(mixed $value): ?string
    {
        $value = trim((string) $value);

        return $value !== '' ? mb_substr($value, 0, 80) : null;
    }
}
