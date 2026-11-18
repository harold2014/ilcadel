<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('settings', function (Blueprint $table) {
            $table->id();
            $table->string('key')->unique();
            $table->json('value');
            $table->timestamps();
        });

        Schema::create('claims', function (Blueprint $table) {
            $table->id();
            $table->string('code', 20)->unique();
            $table->uuid('public_token')->unique();
            $table->string('name');
            $table->string('email');
            $table->string('doc_type', 20);
            $table->string('doc_number', 20);
            $table->date('claimed_on');
            $table->text('message');
            $table->string('status', 20)->default('recibido');
            $table->text('response')->nullable();
            $table->timestamp('responded_at')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('claims');
        Schema::dropIfExists('settings');
    }
};
