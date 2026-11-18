<?php

namespace App\Http\Controllers;

use App\Models\Claim;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class ClaimController extends Controller
{
    public function store(Request $request): JsonResponse
    {
        $data = $request->validate([
            'nombre' => ['required', 'string', 'max:160'],
            'correo' => ['required', 'email', 'max:160'],
            'tipo' => ['required', 'in:DNI,CE,RUC,Pasaporte'],
            'documento' => ['required', 'string', 'max:20'],
            'fecha' => ['required', 'date'],
            'mensaje' => ['required', 'string', 'max:4000'],
        ], [
            'nombre.required' => 'Ingresa tu nombre completo.',
            'correo.required' => 'Ingresa un correo electrónico válido.',
            'correo.email' => 'Ingresa un correo electrónico válido.',
            'tipo.in' => 'Elige un tipo de documento.',
            'documento.required' => 'Ingresa el número de documento.',
            'fecha.required' => 'Indica la fecha del reclamo.',
            'fecha.date' => 'Indica la fecha del reclamo.',
            'mensaje.required' => 'Cuéntanos el detalle de la reclamación.',
        ]);

        $claim = Claim::query()->create([
            'name' => $data['nombre'],
            'email' => $data['correo'],
            'doc_type' => $data['tipo'],
            'doc_number' => $data['documento'],
            'claimed_on' => $data['fecha'],
            'message' => $data['mensaje'],
        ]);

        return response()->json([
            'ok' => true,
            'code' => $claim->code,
            'message' => 'Recibimos tu reclamo '.$claim->code.'. Quedó registrado en el libro de reclamaciones.',
        ]);
    }
}
