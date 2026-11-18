<?php

namespace Tests\Feature;

use App\Models\Claim;
use App\Models\PageVisit;
use App\Models\Setting;
use App\Support\VisitAnalytics;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class SiteTest extends TestCase
{
    use RefreshDatabase;

    public function test_homepage_is_served_and_records_one_visit(): void
    {
        $response = $this->get('/');

        $response->assertOk();
        $response->assertSee('ILCADEL', false);
        $response->assertSee('csrf-token', false);

        $this->assertSame(1, PageVisit::query()->count());
        $this->assertSame('inicio', PageVisit::query()->value('section'));
        $this->assertSame(1, VisitAnalytics::snapshot()['total_visits']);
    }

    public function test_stylesheets_are_served_without_counting_a_visit(): void
    {
        $this->get('/css/styles.css')->assertOk();

        $this->assertSame(0, PageVisit::query()->count());
    }

    public function test_bots_are_not_counted(): void
    {
        $this->withHeader('User-Agent', 'curl/8.0')->get('/')->assertOk();

        $this->assertSame(0, PageVisit::query()->count());
    }

    public function test_unknown_page_is_not_found(): void
    {
        $this->get('/no-existe.html')->assertNotFound();
        $this->assertSame(0, PageVisit::query()->count());
    }

    public function test_claim_is_stored_from_the_public_form(): void
    {
        $response = $this->postJson('/reclamaciones', [
            'nombre' => 'Ana Pérez',
            'correo' => 'ana@example.com',
            'tipo' => 'DNI',
            'documento' => '12345678',
            'fecha' => '2026-11-17',
            'mensaje' => 'Solicito la constancia de mi expediente.',
        ]);

        $response->assertOk();
        $response->assertJsonPath('ok', true);

        $claim = Claim::query()->first();
        $this->assertNotNull($claim);
        $this->assertSame('Ana Pérez', $claim->name);
        $this->assertSame('recibido', $claim->status);
        $this->assertStringStartsWith('LR-', $claim->code);
        $this->assertSame(0, PageVisit::query()->count());
    }

    public function test_published_phone_can_be_replaced_from_settings(): void
    {
        Setting::put('identity', [
            'phone' => '(01) 999 0000',
        ]);

        $this->get('/')
            ->assertOk()
            ->assertSee('(01) 999 0000', false)
            ->assertDontSee('(01) 510 1613', false);
    }
}
