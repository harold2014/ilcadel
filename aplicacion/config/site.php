<?php

return [

    /*
    | Carpeta con el HTML público (index.html, css, js, assets, referencia).
    | Vacío: la carpeta web hermana de esta aplicación.
    */
    'root' => (static function () {
        $configured = env('SITE_ROOT');
        if (! is_string($configured) || trim($configured) === '') {
            return dirname(base_path()).DIRECTORY_SEPARATOR.'web';
        }

        $configured = trim($configured);
        $absolute = str_starts_with($configured, '/') || preg_match('/^[A-Za-z]:[\\\\\\/]/', $configured) === 1;

        return $absolute ? $configured : base_path($configured);
    })(),

    'admin_name' => env('ADMIN_NAME', 'ILCADEL'),
    'admin_email' => env('ADMIN_EMAIL'),
    'admin_password' => env('ADMIN_PASSWORD'),

];
