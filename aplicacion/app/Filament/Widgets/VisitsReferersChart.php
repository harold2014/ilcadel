<?php

namespace App\Filament\Widgets;

use App\Support\VisitAnalytics;
use Filament\Widgets\ChartWidget;

class VisitsReferersChart extends ChartWidget
{
    protected static ?int $sort = 6;

    protected ?string $heading = 'Origen del tráfico';

    protected ?string $description = 'Últimos 7 días';

    protected ?string $pollingInterval = '30s';

    protected ?string $maxHeight = '280px';

    protected int|string|array $columnSpan = 1;

    protected function getData(): array
    {
        $referers = collect(VisitAnalytics::snapshot()['top_referers'] ?? [])->reverse()->values();
        if ($referers->isEmpty()) {
            $referers = collect([['referer' => 'Sin datos', 'visits' => 0]]);
        }

        return [
            'datasets' => [
                [
                    'label' => 'Visitas',
                    'data' => $referers->pluck('visits')->all(),
                    'backgroundColor' => 'rgba(198, 163, 74, 0.9)',
                    'borderRadius' => 4,
                ],
            ],
            'labels' => $referers->pluck('referer')->all(),
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
