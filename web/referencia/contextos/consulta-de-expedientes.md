# Consulta de expedientes

Sección del mismo sitio. En la web actual el botón de la cabecera y el enlace del pie abren https://sistemas.ilcadel.org/ en otra dirección. En la página nueva la búsqueda queda dentro de ILCADEL, con el mismo menú, logo y pie.

El alta, la edición y el archivo de expedientes los hace el personal en un panel interno. Eso no es una página pública y no se replica como sitio aparte.

## Búsqueda pública

Título: Búsqueda de Expediente. Bajada: «Ingrese los 5 primeros dígitos del expediente».

| Campo | Comportamiento |
|---|---|
| N.° de Expediente | Obligatorio. Solo los 5 primeros dígitos. Ejemplo publicado: `00001-2005-0-1817-JR-CO-06` se consulta como `00001`. Placeholder `00001`. |
| Verificación | Obligatorio. Código en un recuadro oscuro; hay botón para generar otro. Se copia en el campo «Código». |
| Consultar Expediente | Envía la búsqueda. La pantalla indica campos obligatorios y sesión de 10 minutos. |

Cabecera de esa pantalla, hoy: Inicio, Manual, FAQ.

## Resultado

Si el expediente existe, la pantalla se llama «Resultado de la consulta» y abre tres bloques:

1. **Reporte de expediente.** Número, fecha de inicio, órgano jurisdiccional, especialidad, árbitro, secretario arbitral, etapa procesal, ubicación, proceso y materia.
2. **Partes procesales.** Demandante y demandado, persona natural o jurídica.
3. **Seguimiento.** Actos, resoluciones, notificaciones y PDF descargables.

## Manual y FAQ

- Manual de uso público: mismos tres pasos (5 dígitos, código, consultar) y las tres secciones del resultado. Versión indicada en pantalla: Manual de Usuario v1.0, mayo 2026.
- Preguntas frecuentes de la institución: [preguntas-frecuentes.md](preguntas-frecuentes.md).
