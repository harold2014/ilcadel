<?php

namespace App\Filament\Widgets;

use App\Support\VisitAnalytics;
use Filament\Widgets\ChartWidget;

class VisitsTopPagesChart extends ChartWidget
{
    protected static ?int $sort = 5;

    protected ?string $heading = 'Páginas más vistas';

    protected ?string $description = 'Últimos 7 días';

    protected ?string $pollingInterval = '30s';

    protected ?string $maxHeight = '280px';

    protected int|string|array $columnSpan = 1;

    protected function getData(): array
    {
        $pages = collect(VisitAnalytics::snapshot()['top_pages'] ?? [])->reverse()->values();
        if ($pages->isEmpty()) {
            $pages = collect([['page' => 'Sin datos', 'visits' => 0]]);
        }

        return [
            'datasets' => [
                [
                    'label' => 'Visitas',
                    'data' => $pages->pluck('visits')->all(),
                    'backgroundColor' => 'rgba(16, 31, 56, 0.85)',
                    'borderRadius' => 4,
                ],
            ],
            'labels' => $pages->pluck('page')->all(),
        ];
    }

    protected function getType(): string
    {
        return 'bar';
    }

    protected function getOptions(): array
    {
        return [
            'indexAxis' => 'y',
            'plugins' => ['legend' => ['display' => false]],
            'scales' => ['x' => ['beginAtZero' => true, 'ticks' => ['precision' => 0]]],
        ];
    }
}
