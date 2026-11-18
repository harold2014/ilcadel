<?php

namespace App\Filament\Resources\Claims\Schemas;

use Filament\Forms\Components\DatePicker;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Schema;

class ClaimForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            TextInput::make('code')->label('Código')->disabled()->dehydrated(false),
            Select::make('status')->label('Estado')->required()->options([
                'recibido' => 'Recibido',
                'en_atencion' => 'En atención',
                'respondido' => 'Respondido',
            ])->default('recibido'),
            TextInput::make('name')->label('Nombre')->required()->maxLength(160),
            TextInput::make('email')->label('Correo')->email()->required()->maxLength(160),
            Select::make('doc_type')->label('Documento')->required()->options([
                'DNI' => 'DNI',
                'CE' => 'Carné de extranjería',
                'RUC' => 'RUC',
                'Pasaporte' => 'Pasaporte',
            ]),
            TextInput::make('doc_number')->label('Número de documento')->required()->maxLength(20),
            DatePicker::make('claimed_on')->label('Fecha del reclamo')->required(),
            Textarea::make('message')->label('Detalle y pedido')->required()->rows(6)->columnSpanFull(),
            Textarea::make('response')->label('Respuesta')->rows(4)->columnSpanFull(),
        ]);
    }
}
