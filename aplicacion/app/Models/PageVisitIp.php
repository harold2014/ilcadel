<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class PageVisitIp extends Model
{
    public $timestamps = false;

    protected $fillable = ['ip_hash', 'first_seen', 'last_seen'];

    protected function casts(): array
    {
        return [
            'first_seen' => 'datetime',
            'last_seen' => 'datetime',
        ];
    }

    protected static function booted(): void
    {
        static::creating(function (PageVisitIp $row): void {
            $row->first_seen ??= now();
            $row->last_seen ??= now();
        });
    }
}
