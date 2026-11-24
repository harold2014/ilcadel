<?php

namespace App\Http\Controllers;

use App\Support\SiteContent;
use Illuminate\Http\Response;

class SitePageController extends Controller
{
    private const PAGES = [
        'index',
        'institucion',
        'arbitraje',
        'conciliacion',
        'defensa-legal',
        'academia-juridica',
        'equipo',
        'certificaciones',
        'contacto',
        'galeria',
        'mesa-de-partes',
        'consulta',
        'reclamaciones',
    ];

    public function show(string $page = 'index'): Response
    {
        $page = strtolower($page);
        abort_unless(in_array($page, self::PAGES, true), 404);

        $root = realpath((string) config('site.root'));
        abort_unless($root !== false, 404);

        $file = $root.DIRECTORY_SEPARATOR.$page.'.html';
        abort_unless(is_file($file), 404);

        $html = SiteContent::apply((string) file_get_contents($file));
        $token = e(csrf_token());
        $csrf = "<meta name=\"csrf-token\" content=\"{$token}\">";
        if (preg_match('/<meta\s+charset=[^>]*>/i', $html) === 1) {
            $html = preg_replace('/(<meta\s+charset=[^>]*>)/i', '$1'."\n  ".$csrf, $html, 1) ?? $html;
        } else {
            $html = preg_replace('/<head([^>]*)>/i', '<head$1>'."\n  ".$csrf, $html, 1) ?? $html;
        }

        return response($html, 200, [
            'Content-Type' => 'text/html; charset=UTF-8',
        ]);
    }
}
