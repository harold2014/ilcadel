<?php

namespace App\Filament\Widgets;

use App\Support\VisitAnalytics;
use Filament\Widgets\ChartWidget;

class VisitsHourlyChart extends ChartWidget
{
    protected static ?int $sort = 2;

    protected ?string $heading = 'Tráfico de hoy';

    protected ?string $description = 'Visitas por hora';

    protected ?string $pollingInterval = '30s';

    protected ?string $maxHeight = '260px';

    protected int|string|array $columnSpan = 'full';

    protected function getData(): array
    {
        $hourly = VisitAnalytics::snapshot()['hourly_today'] ?? [];

        return [
            'datasets' => [
                [
                    'label' => 'Visitas',
                    'data' => collect($hourly)->pluck('visits')->all(),
                    'borderColor' => '#101F38',
                    'backgroundColor' => 'rgba(16, 31, 56, 0.16)',
                    'fill' => true,
                    'tension' => 0.35,
                    'pointRadius' => 2,
                ],
            ],
            'labels' => collect($hourly)->pluck('hour')->all(),
        ];
    }

    protected function getType(): string
    {
        return 'line';
    }

    protected function getOptions(): array
    {
        return [
            'plugins' => ['legend' => ['display' => false]],
            'scales' => ['y' => ['beginAtZero' => true, 'ticks' => ['precision' => 0]]],
        ];
    }
}
