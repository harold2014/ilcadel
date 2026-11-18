# ILCADEL — sitio web

Sitio estático (HTML + CSS + JS) del Instituto Latinoamericano de Conciliación, Arbitraje y Defensa Legal. Sin framework, sin build step y sin dependencias npm.

## Estructura

```
web/
├── index.html          # Entrada del sitio
├── css/styles.css      # Estilos
├── js/main.js          # Interacciones
├── assets/img/         # Imágenes usadas en runtime (logo, hero)
├── brand/              # Fuentes de marca y prototipo (no servir en producción)
│   ├── Logotipo.png
│   ├── logotipodoc.docx
│   └── prototipocliente.jpeg
├── docs/               # Notas de trabajo del proyecto
└── README.md
```

## Cómo abrir / trabajar

1. Abrir la carpeta `d:\Proyecto Ilcadel\web` en el editor.
2. Previsualizar con un servidor local estático desde esa carpeta, por ejemplo:
   - VS Code / Cursor: extensión Live Server, o
   - PowerShell: `python -m http.server 8080` y visitar `http://localhost:8080`
3. Editar `index.html`, `css/styles.css` y `js/main.js`. Las rutas relativas (`css/`, `js/`, `assets/`) deben quedar como están.

No hay `.env`, git ni backend en este working tree. `brand/` es material de diseño de referencia; no enlazarlo desde el HTML.

## Contenido

La información publicada está en las páginas del menú (`institucion.html`, `arbitraje.html`, `conciliacion.html`, `defensa-legal.html`, `certificaciones.html`, `mesa-de-partes.html`, `consulta.html`, `reclamaciones.html`, `contacto.html`, `galeria.html`). El archivo de origen sigue en `referencia/`.

La consulta de expedientes es una página del mismo sitio. El envío de mesa de partes, reclamos y la lectura del registro quedan para conectarlos cuando el sitio sea administrable.
