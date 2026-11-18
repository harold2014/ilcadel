<?php

namespace App\Filament\Widgets;

use App\Support\VisitAnalytics;
use Filament\Widgets\ChartWidget;

class VisitsDevicesChart extends ChartWidget
{
    protected static ?int $sort = 4;

    protected ?string $heading = 'Dispositivos';

    protected ?string $description = 'Últimos 7 días';

    protected ?string $pollingInterval = '30s';

    protected ?string $maxHeight = '280px';

    protected int|string|array $columnSpan = 1;

    protected function getData(): array
    {
        $devices = VisitAnalytics::snapshot()['devices'] ?? [];
        if ($devices === []) {
            $devices = [['device' => 'otro', 'visits' => 0]];
        }

        return [
            'datasets' => [
                [
                    'label' => 'Visitas',
                    'data' => collect($devices)->pluck('visits')->all(),
                    'backgroundColor' => ['#101F38', '#C6A34A', '#0B1526', '#3D5A80', '#E2C070'],
                ],
            ],
            'labels' => collect($devices)->pluck('device')->map(fn ($device) => VisitAnalytics::deviceLabel((string) $device))->all(),
        ];
    }

    protected function getType(): string
    {
        return 'doughnut';
    }
}
