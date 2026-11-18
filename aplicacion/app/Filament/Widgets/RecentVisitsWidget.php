<?php

namespace App\Filament\Widgets;

use App\Models\PageVisit;
use App\Support\VisitAnalytics;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Filament\Widgets\TableWidget;

class RecentVisitsWidget extends TableWidget
{
    protected static ?int $sort = 9;

    protected int|string|array $columnSpan = 'full';

    protected ?string $pollingInterval = '20s';

    public function table(Table $table): Table
    {
        return $table
            ->query(PageVisit::query())
            ->heading('Últimas visitas')
            ->columns([
                TextColumn::make('created_at')
                    ->label('Cuándo')
                    ->since()
                    ->sortable(),
                TextColumn::make('section')
                    ->label('Página')
                    ->formatStateUsing(fn (?string $state, PageVisit $record): string => VisitAnalytics::pageLabel($state ?: (string) $record->path))
                    ->badge()
                    ->color('success'),
                TextColumn::make('device')
                    ->label('Dispositivo')
                    ->formatStateUsing(fn (?string $state): string => VisitAnalytics::deviceLabel($state))
                    ->badge()
                    ->color(fn (?string $state): string => match ($state) {
                        'mobile' => 'warning',
                        'tablet' => 'info',
                        'desktop' => 'success',
                        default => 'gray',
                    }),
                TextColumn::make('country')
                    ->label('Lugar')
                    ->formatStateUsing(fn (?string $state, PageVisit $record): string => $record->placeLabel()),
                TextColumn::make('referer')
                    ->label('Origen')
                    ->formatStateUsing(fn (?string $state): string => VisitAnalytics::refererLabel($state))
                    ->toggleable(),
            ])
            ->defaultSort('id', 'desc')
            ->paginated([8, 20])
            ->defaultPaginationPageOption(8);
    }
}
