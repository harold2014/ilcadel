<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Str;

class Claim extends Model
{
    protected $fillable = [
        'code',
        'public_token',
        'name',
        'email',
        'doc_type',
        'doc_number',
        'claimed_on',
        'message',
        'status',
        'response',
        'responded_at',
    ];

    protected function casts(): array
    {
        return [
            'claimed_on' => 'date',
            'responded_at' => 'datetime',
        ];
    }

    protected static function booted(): void
    {
        static::creating(function (Claim $claim): void {
            $claim->public_token ??= (string) Str::uuid();
            $claim->code ??= static::nextCode();
            $claim->status ??= 'recibido';
        });

        static::updating(function (Claim $claim): void {
            if ($claim->isDirty('status') && $claim->status === 'respondido' && ! $claim->responded_at) {
                $claim->responded_at = now();
            }
        });
    }

    public static function nextCode(): string
    {
        $year = now()->year;
        $last = static::query()->where('code', 'like', "LR-{$year}-%")->orderByDesc('id')->value('code');
        $sequence = 1;

        if (is_string($last) && preg_match('/(\d+)$/', $last, $matches)) {
            $sequence = ((int) $matches[1]) + 1;
        }

        return sprintf('LR-%d-%05d', $year, $sequence);
    }

    public function statusLabel(): string
    {
        return match ($this->status) {
            'en_atencion' => 'En atención',
            'respondido' => 'Respondido',
            default => 'Recibido',
        };
    }
}
