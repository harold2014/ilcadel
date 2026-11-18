<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Crea el acceso del panel. El correo y la clave salen del .env del servidor.
     */
    public function run(): void
    {
        $email = config('site.admin_email');
        $password = config('site.admin_password');

        if (! is_string($email) || ! is_string($password) || $email === '' || $password === '') {
            $this->command?->warn('No se creó el administrador. Completa ADMIN_EMAIL y ADMIN_PASSWORD en .env y vuelve a ejecutar db:seed.');

            return;
        }

        $user = User::query()->firstOrNew(['email' => $email]);
        $user->name = (string) config('site.admin_name');
        if (! $user->exists) {
            $user->password = $password;
            $user->email_verified_at = now();
        }
        $user->save();
    }
}
