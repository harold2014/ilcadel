<?php

namespace App\Http\Controllers;

use App\Support\SiteContent;
use Symfony\Component\HttpFoundation\Response;

class SiteAssetController extends Controller
{
    public function css(string $path): Response
    {
        return $this->file('css', $path);
    }

    public function js(string $path): Response
    {
        return $this->file('js', $path);
    }

    public function asset(string $path): Response
    {
        return $this->file('assets', $path);
    }

    public function referencia(string $path): Response
    {
        return $this->file('referencia', $path);
    }

    private function file(string $directory, string $path): Response
    {
        $path = str_replace('\\', '/', $path);
        abort_if($path === '' || str_contains($path, '..'), 404);

        $base = realpath((string) config('site.root'));
        abort_unless($base !== false, 404);

        $root = realpath($base.DIRECTORY_SEPARATOR.$directory);
        abort_unless($root !== false, 404);

        $full = realpath($root.DIRECTORY_SEPARATOR.str_replace('/', DIRECTORY_SEPARATOR, $path));
        abort_unless($full !== false && str_starts_with($full, $root.DIRECTORY_SEPARATOR), 404);

        $types = [
            'css' => 'text/css; charset=UTF-8',
            'js' => 'text/javascript; charset=UTF-8',
            'mjs' => 'text/javascript; charset=UTF-8',
            'html' => 'text/html; charset=UTF-8',
            'webp' => 'image/webp',
            'jpg' => 'image/jpeg',
            'jpeg' => 'image/jpeg',
            'png' => 'image/png',
            'svg' => 'image/svg+xml',
            'gif' => 'image/gif',
            'ico' => 'image/x-icon',
            'mp4' => 'video/mp4',
            'webm' => 'video/webm',
            'woff' => 'font/woff',
            'woff2' => 'font/woff2',
            'pdf' => 'application/pdf',
            'doc' => 'application/msword',
            'docx' => 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        ];
        $extension = strtolower(pathinfo($full, PATHINFO_EXTENSION));
        $headers = isset($types[$extension]) ? ['Content-Type' => $types[$extension]] : [];

        if (in_array($extension, ['css', 'js', 'mjs', 'html', 'svg'], true)) {
            return response(SiteContent::apply((string) file_get_contents($full)), 200, $headers);
        }

        return response()->file($full, $headers);
    }
}
