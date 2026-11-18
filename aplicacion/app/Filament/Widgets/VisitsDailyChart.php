<?php

namespace App\Filament\Widgets;

use App\Support\VisitAnalytics;
use Filament\Widgets\ChartWidget;

class VisitsDailyChart extends ChartWidget
{
    protected static ?int $sort = 3;

    protected ?string $heading = 'Últimos 14 días';

    protected ?string $description = 'Páginas vistas y visitantes distintos';

    protected ?string $pollingInterval = '30s';

    protected ?string $maxHeight = '280px';

    protected int|string|array $columnSpan = 1;

    protected function getData(): array
    {
        $daily = VisitAnalytics::snapshot()['daily'] ?? [];

        return [
            'datasets' => [
                [
                    'label' => 'Visitas',
                    'data' => collect($daily)->pluck('visits')->all(),
                    'backgroundColor' => 'rgba(16, 31, 56, 0.85)',
                    'borderRadius' => 4,
                ],
                [
                    'label' => 'IPs únicas',
                    'data' => collect($daily)->pluck('unique')->all(),
                    'backgroundColor' => 'rgba(198, 163, 74, 0.9)',
                    'borderRadius' => 4,
                ],
            ],
            'labels' => collect($daily)->pluck('label')->all(),
        ];
    }

    protected function getType(): string
    {
        return 'bar';
    }

    protected function getOptions(): array
    {
        return [
            'scales' => ['y' => ['beginAtZero' => true, 'ticks' => ['precision' => 0]]],
        ];
    }
}
