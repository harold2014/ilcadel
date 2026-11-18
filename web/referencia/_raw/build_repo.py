# -*- coding: utf-8 -*-
"""Download ILCADEL images and page contexts into web/referencia."""
import json
import os
import re
import html
import urllib.request
from pathlib import Path

ROOT = Path(r"D:\Proyecto Ilcadel\web\referencia")
RAW = ROOT / "_raw"
IMG = ROOT / "imagenes"
CTX = ROOT / "contextos"

UA = {"User-Agent": "ILCADEL-referencia/1.0 (local archive)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def strip_html(s):
    s = re.sub(r"(?is)<script.*?>.*?</script>", " ", s or "")
    s = re.sub(r"(?is)<style.*?>.*?</style>", " ", s or "")
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    s = re.sub(r"(?is)</p>", "\n\n", s)
    s = re.sub(r"(?is)</h[1-6]>", "\n\n", s)
    s = re.sub(r"(?is)</li>", "\n", s)
    s = re.sub(r"(?is)<li[^>]*>", "- ", s)
    s = re.sub(r"(?is)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = s.replace("\xa0", " ")
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.strip()


def folder_for(name):
    n = name.lower()
    if any(k in n for k in ("logotipo", "logo", "favicon", "cropped")):
        return "marca"
    if n.startswith("elemento"):
        return "hero"
    if any(k in n for k in ("fondo", "concatc")):
        return "fondos"
    if any(k in n for k in ("qsomos", "imagen-qsomos")):
        return "institucional"
    if any(k in n for k in ("iso", "minjus", "oece", "renace", "resolucion", "certificado", "escudo")):
        return "certificaciones"
    if "william" in n or "dr-" in n:
        return "equipo"
    if any(k in n for k in ("fotografia", "noticia", "huacho")):
        return "galeria"
    if n in ("w.webp",):
        return "iconos"
    return "servicios"


def main():
    items = []
    for fn in ["media-1.json", "media-2.json"]:
        items += json.loads((RAW / fn).read_text(encoding="utf-8"))

    catalog = []
    for i in items:
        mime = i.get("mime_type") or ""
        url = i.get("source_url") or ""
        name = url.split("/")[-1]
        md = i.get("media_details") or {}
        entry = {
            "id": i.get("id"),
            "archivo": name,
            "url": url,
            "mime": mime,
            "alt": i.get("alt_text") or "",
            "titulo": (i.get("title") or {}).get("rendered") or "",
            "ancho": md.get("width"),
            "alto": md.get("height"),
            "kb": (md.get("filesize") or 0) // 1024,
            "fecha": (i.get("date") or "")[:10],
            "slug": i.get("slug"),
        }
        if mime.startswith("image/"):
            folder = folder_for(name)
            dest_dir = IMG / folder
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / name
            entry["carpeta"] = f"imagenes/{folder}/{name}"
            if not dest.exists() or dest.stat().st_size == 0:
                try:
                    data = get(url)
                    dest.write_bytes(data)
                    entry["descargada"] = True
                    entry["bytes"] = len(data)
                except Exception as e:
                    entry["descargada"] = False
                    entry["error"] = str(e)
            else:
                entry["descargada"] = True
                entry["bytes"] = dest.stat().st_size
        else:
            entry["carpeta"] = None
            entry["descargada"] = False
            entry["nota"] = "documento catalogado, no descargado"
        catalog.append(entry)

    (ROOT / "catalogo-medios.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    pages = json.loads((RAW / "pages.json").read_text(encoding="utf-8"))
    CTX.mkdir(parents=True, exist_ok=True)
    page_index = []
    for p in pages:
        slug = p["slug"]
        if slug == "sample-page":
            continue
        url = f"https://ilcadel.org/wp-json/wp/v2/pages/{p['id']}?_fields=id,slug,link,title,content,excerpt"
        try:
            data = json.loads(get(url).decode("utf-8"))
        except Exception as e:
            page_index.append({"slug": slug, "error": str(e)})
            continue
        title = html.unescape((data.get("title") or {}).get("rendered") or slug)
        text = strip_html((data.get("content") or {}).get("rendered") or "")
        link = data.get("link") or p.get("link")
        md = f"# {title}\n\n- URL actual: {link}\n- Slug: `{slug}`\n- ID WordPress: {p['id']}\n\n## Texto\n\n{text if text else '_(sin texto en el contenido de la página; el diseño puede estar solo en el constructor visual)_'}\n"
        (CTX / f"{slug}.md").write_text(md, encoding="utf-8")
        page_index.append({
            "slug": slug,
            "titulo": title,
            "url": link,
            "chars": len(text),
            "archivo": f"contextos/{slug}.md",
        })
        print("page", slug, len(text))

    (ROOT / "catalogo-paginas.json").write_text(
        json.dumps(page_index, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    imgs = [c for c in catalog if c.get("carpeta")]
    print("images", len(imgs), "ok", sum(1 for c in imgs if c.get("descargada")))
    print("pages", len(page_index))


if __name__ == "__main__":
    main()
