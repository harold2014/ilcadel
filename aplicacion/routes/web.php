<?php

use App\Http\Controllers\ClaimController;
use App\Http\Controllers\SiteAssetController;
use App\Http\Controllers\SitePageController;
use Illuminate\Support\Facades\Route;

Route::get('/', [SitePageController::class, 'show'])->defaults('page', 'index');

Route::post('/reclamaciones', [ClaimController::class, 'store'])
    ->name('claims.store')
    ->middleware('throttle:10,1');

Route::get('/{page}.html', [SitePageController::class, 'show'])
    ->where('page', 'index|institucion|arbitraje|conciliacion|defensa-legal|certificaciones|contacto|galeria|mesa-de-partes|consulta|reclamaciones');

Route::get('/css/{path}', [SiteAssetController::class, 'css'])->where('path', '.*');
Route::get('/js/{path}', [SiteAssetController::class, 'js'])->where('path', '.*');
Route::get('/assets/{path}', [SiteAssetController::class, 'asset'])->where('path', '.*');
Route::get('/referencia/{path}', [SiteAssetController::class, 'referencia'])->where('path', '.*');
