<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('page_visits', function (Blueprint $table) {
            $table->id();
            $table->string('path');
            $table->string('referer')->nullable();
            $table->string('ip_hash', 64);
            $table->string('device', 20)->nullable();
            $table->string('section', 40)->nullable();
            $table->string('country', 80)->nullable();
            $table->string('region', 80)->nullable();
            $table->string('city', 80)->nullable();
            $table->timestamp('created_at')->useCurrent();
            $table->index('created_at');
            $table->index('ip_hash');
            $table->index('section');
        });

        Schema::create('page_visit_ips', function (Blueprint $table) {
            $table->id();
            $table->string('ip_hash', 64)->unique();
            $table->timestamp('first_seen')->useCurrent();
            $table->timestamp('last_seen')->useCurrent();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('page_visit_ips');
        Schema::dropIfExists('page_visits');
    }
};
