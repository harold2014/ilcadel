<?php

namespace App\Support;

use App\Models\Setting;
use Throwable;

class SiteContent
{
    /**
     * @return array<string, string>
     */
    public static function identityDefaults(): array
    {
        return [
            'phone' => '(01) 510 1613',
            'phone_tel' => '+5115101613',
            'whatsapp_dg' => '51999835661',
            'whatsapp_dg_label' => '+51 999 835 661',
            'whatsapp_sg' => '51987298765',
            'whatsapp_sg_label' => '+51 987 298 765',
            'whatsapp_ca' => '18257475773',
            'whatsapp_ca_label' => '+1 825 747 5773',
            'email_mesa' => 'recepcionvirtual@ilcadel.org',
            'email_conciliacion' => 'franztp@ilcadel.org',
        ];
    }

    /**
     * @return array<string, string>
     */
    public static function identity(): array
    {
        $stored = [];

        try {
            $value = Setting::get('identity', []);
            if (is_array($value)) {
                $stored = $value;
            }
        } catch (Throwable) {
            $stored = [];
        }

        $merged = self::identityDefaults();
        foreach ($stored as $key => $value) {
            if (is_string($key) && array_key_exists($key, $merged)) {
                $merged[$key] = trim((string) $value);
            }
        }

        return $merged;
    }

    public static function apply(string $html): string
    {
        $defaults = self::identityDefaults();
        $current = self::identity();
        $map = [];

        foreach ($defaults as $key => $from) {
            $to = $current[$key] ?? $from;
            if ($to !== '' && $to !== $from) {
                $map[$from] = $to;
            }
        }

        if ($map === []) {
            return $html;
        }

        uksort($map, fn (string $a, string $b): int => strlen($b) <=> strlen($a));

        return strtr($html, $map);
    }
}
