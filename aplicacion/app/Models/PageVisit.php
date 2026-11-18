<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class PageVisit extends Model
{
    public $timestamps = false;

    protected $fillable = [
        'path',
        'referer',
        'ip_hash',
        'device',
        'section',
        'country',
        'region',
        'city',
        'created_at',
    ];

    protected function casts(): array
    {
        return [
            'created_at' => 'datetime',
        ];
    }

    public function placeLabel(): string
    {
        $parts = array_values(array_filter([
            $this->city ?: null,
            $this->country ?: null,
        ]));

        return $parts !== [] ? implode(', ', $parts) : '—';
    }
}
