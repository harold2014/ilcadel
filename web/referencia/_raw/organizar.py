# -*- coding: utf-8 -*-
import json
import shutil
from pathlib import Path

ROOT = Path(r"D:\Proyecto Ilcadel\web\referencia")
IMG = ROOT / "imagenes"
catalog_path = ROOT / "catalogo-medios.json"
items = json.loads(catalog_path.read_text(encoding="utf-8"))

moves = {
    "RESOLUCION-DE-PROBLEMAS-CIVILES.webp": "servicios",
    "RESOLUCION-DE-PROBLEMAS-CIVILES2.webp": "servicios",
    "Resolucion-de-Divorcios.webp": "servicios",
    "regaju.webp": "certificaciones",
    "regaju2.webp": "certificaciones",
    "Escudo-Huacho.webp": "galeria",
}

by_name = {i["archivo"]: i for i in items}
for name, folder in moves.items():
    src = None
    for d in IMG.iterdir():
        if d.is_dir() and (d / name).exists():
            src = d / name
            break
    if not src:
        print("missing", name)
        continue
    dest = IMG / folder / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    if src.resolve() != dest.resolve():
        shutil.move(str(src), str(dest))
    if name in by_name:
        by_name[name]["carpeta"] = f"imagenes/{folder}/{name}"
    print("moved", name, "->", folder)

catalog_path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

docs = [i for i in items if not str(i.get("mime", "")).startswith("image/")]
docs.sort(key=lambda i: (i.get("titulo") or i.get("archivo") or "").lower())
lines = [
    "# Documentos de la web actual",
    "",
    "Catálogo de PDF, Word y Excel publicados en ilcadel.org. No se descargaron: siguen en la web actual y se traen solo cuando reemplacemos esa sección.",
    "",
    "| Archivo | Tipo | KB | URL |",
    "|---|---|---:|---|",
]
for i in docs:
    name = i.get("archivo") or ""
    mime = (i.get("mime") or "").split("/")[-1]
    kb = i.get("kb") or 0
    url = i.get("url") or ""
    lines.append(f"| {name} | {mime} | {kb} | {url} |")
lines.append("")
(ROOT / "documentos.md").write_text("\n".join(lines), encoding="utf-8")

groups = {}
for i in items:
    if not str(i.get("mime", "")).startswith("image/"):
        continue
    carpeta = (i.get("carpeta") or "").split("/")[1] if i.get("carpeta") else "otras"
    groups.setdefault(carpeta, []).append(i)

img_lines = [
    "# Imágenes locales",
    "",
    "Originales WebP de la mediateca (sin las copias redimensionadas de WordPress).",
    "",
]
order = ["marca", "hero", "fondos", "institucional", "servicios", "certificaciones", "equipo", "galeria", "iconos"]
for key in order:
    rows = sorted(groups.get(key, []), key=lambda r: r["archivo"].lower())
    img_lines.append(f"## {key}")
    img_lines.append("")
    img_lines.append("| Archivo | Px | KB | Uso en el título de WordPress |")
    img_lines.append("|---|---:|---:|---|")
    for r in rows:
        px = f"{r.get('ancho') or '—'}×{r.get('alto') or '—'}"
        titulo = (r.get("titulo") or "").replace("|", "/")
        img_lines.append(f"| `{r['carpeta']}` | {px} | {r.get('kb') or 0} | {titulo} |")
    img_lines.append("")
(ROOT / "imagenes.md").write_text("\n".join(img_lines), encoding="utf-8")
print("docs", len(docs), "image groups", {k: len(v) for k, v in groups.items()})
