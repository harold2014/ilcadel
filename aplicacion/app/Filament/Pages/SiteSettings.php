<?php

namespace App\Filament\Pages;

use App\Models\Setting;
use App\Support\SiteContent;
use BackedEnum;
use Filament\Actions\Action;
use Filament\Forms\Components\TextInput;
use Filament\Notifications\Notification;
use Filament\Pages\Page;
use Filament\Schemas\Components\Actions;
use Filament\Schemas\Components\EmbeddedSchema;
use Filament\Schemas\Components\Form;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;

class SiteSettings extends Page
{
    protected static string|\UnitEnum|null $navigationGroup = 'Configuración';

    protected static ?string $navigationLabel = 'Datos del sitio';

    protected static ?string $title = 'Datos del sitio';

    protected static ?int $navigationSort = 1;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedCog6Tooth;

    protected string $view = 'filament.pages.site-settings';

    /** @var array<string, mixed>|null */
    public ?array $data = [];

    public function mount(): void
    {
        $this->form->fill(SiteContent::identity());
    }

    public function form(Schema $schema): Schema
    {
        return $schema
            ->components([
                TextInput::make('phone')->label('Teléfono de la central')->required()->maxLength(40)
                    ->helperText('Así se lee en la web. Ejemplo: (01) 510 1613'),
                TextInput::make('phone_tel')->label('Teléfono para llamar')->required()->maxLength(40)
                    ->helperText('Con código de país, sin espacios. Ejemplo: +5115101613'),
                TextInput::make('whatsapp_dg_label')->label('WhatsApp Dirección General')->required()->maxLength(40),
                TextInput::make('whatsapp_dg')->label('Número Dirección General')->required()->maxLength(20)
                    ->helperText('Solo dígitos, con código de país. Ejemplo: 51999835661'),
                TextInput::make('whatsapp_sg_label')->label('WhatsApp Secretaría General')->required()->maxLength(40),
                TextInput::make('whatsapp_sg')->label('Número Secretaría General')->required()->maxLength(20),
                TextInput::make('whatsapp_ca_label')->label('WhatsApp sede Canadá')->required()->maxLength(40),
                TextInput::make('whatsapp_ca')->label('Número sede Canadá')->required()->maxLength(20),
                TextInput::make('email_mesa')->label('Correo de mesa de partes')->email()->required()->maxLength(160),
                TextInput::make('email_conciliacion')->label('Correo de conciliación')->email()->required()->maxLength(160),
            ])
            ->statePath('data');
    }

    public function content(Schema $schema): Schema
    {
        return $schema->components([
            Form::make([EmbeddedSchema::make('form')])
                ->id('form')
                ->livewireSubmitHandler('save')
                ->footer([
                    Actions::make([
                        Action::make('save')->label('Guardar')->submit('save'),
                    ]),
                ]),
        ]);
    }

    public function save(): void
    {
        $state = $this->form->getState();
        foreach (['whatsapp_dg', 'whatsapp_sg', 'whatsapp_ca'] as $key) {
            $digits = preg_replace('/\D+/', '', (string) ($state[$key] ?? ''));
            $state[$key] = $digits !== '' ? $digits : SiteContent::identityDefaults()[$key];
        }

        Setting::put('identity', $state);

        Notification::make()->success()->title('Datos del sitio guardados')->send();
    }
}
