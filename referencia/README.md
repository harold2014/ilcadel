# Repositorio de la web actual

Copia de trabajo de [ilcadel.org](https://ilcadel.org/), tomada el 17 de noviembre de 2026. Sirve para construir la página nueva sin volver a adivinar textos, fotos ni enlaces.

Esta carpeta **no se pisa**. Cuando llegue información nueva, se aplica en el sitio (`web/index.html` y `web/assets/`) y este archivo queda como referencia de lo que hoy está publicado.

## Cómo está ordenado

| Ruta | Qué guarda |
|---|---|
| [mapa.md](mapa.md) | Secciones, menú, sedes, teléfonos y la decisión sobre consulta de expedientes |
| [contextos/](contextos/) | Texto de cada página, en Markdown |
| [imagenes/](imagenes/) | 77 imágenes originales (WebP), por tema |
| [imagenes.md](imagenes.md) | Índice de esas imágenes |
| [documentos.md](documentos.md) | PDF, Word y Excel publicados (solo enlace, sin descargar) |
| `catalogo-medios.json` | Ficha técnica de cada archivo de la mediateca |
| `catalogo-paginas.json` | Lista de páginas de WordPress |

## Qué entra en la página nueva

La web pública es un solo sitio. Mesa de partes, centros, certificaciones, equipo, historia, descargas, galería, libro de reclamaciones y **consulta de expedientes** son secciones de esa misma página.

Hoy el botón «Consulta de Expedientes» abre `sistemas.ilcadel.org`. En la página nueva esa búsqueda vive dentro del sitio. El detalle del formulario público está en [contextos/consulta-de-expedientes.md](contextos/consulta-de-expedientes.md). El panel donde el personal carga expedientes no es una página pública.

## Cómo reemplazar después

1. Elegir una sección en [mapa.md](mapa.md).
2. Leer su contexto y la imagen que usa.
3. Cambiar solo esa parte en el sitio nuevo.
4. Dejar intacto el archivo de esta carpeta, para poder comparar con lo publicado.
