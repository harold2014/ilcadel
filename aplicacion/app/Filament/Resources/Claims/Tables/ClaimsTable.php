<?php

namespace App\Filament\Resources\Claims\Tables;

use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;

class ClaimsTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('code')->label('Código')->searchable()->sortable(),
                TextColumn::make('claimed_on')->label('Fecha')->date('d/m/Y')->sortable(),
                TextColumn::make('name')->label('Nombre')->searchable(),
                TextColumn::make('doc_type')->label('Documento')->badge(),
                TextColumn::make('status')->label('Estado')->badge()->formatStateUsing(fn (string $state): string => match ($state) {
                    'en_atencion' => 'En atención',
                    'respondido' => 'Respondido',
                    default => 'Recibido',
                }),
                TextColumn::make('email')->label('Correo')->toggleable(),
            ])
            ->defaultSort('id', 'desc')
            ->recordActions([
                EditAction::make(),
            ]);
    }
}
