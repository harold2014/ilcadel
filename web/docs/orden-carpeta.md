# Orden de la carpeta (2026-11-17)

## Antes

- `web/` ya tenía el sitio (`index.html`, `css/`, `js/`, `assets/`).
- En el padre `d:\Proyecto Ilcadel\` había sueltos: `Logotipo.png`, `logotipodoc.docx`, `prototipocliente.jpeg`.

## Después

- Runtime intacto: no se movió `index.html`, `css/`, `js/` ni `assets/`.
- Fuentes de marca y prototipo → `web/brand/`.
- Notas → `web/docs/`.
- Copia de la web publicada (textos e imágenes de ilcadel.org) → `web/referencia/`. No es runtime.
- README en la raíz de `web/`.

## Convención

| Carpeta     | Rol                                      |
|-------------|------------------------------------------|
| `css/`, `js/`, `index.html` | Código de la app estática     |
| `assets/`   | Assets referenciados por el sitio        |
| `brand/`    | Originales / prototipo (no runtime)      |
| `docs/`     | Documentación de trabajo                 |
| `referencia/` | Archivo de ilcadel.org (no runtime)    |
