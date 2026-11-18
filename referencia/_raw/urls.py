import json
from pathlib import Path
items = json.loads(Path(r"D:\Proyecto Ilcadel\web\referencia\catalogo-medios.json").read_text(encoding="utf-8"))
want = (
    "REGLAMENTO-PROCESAL-DE-ARBITRAJE-2026",
    "CODIGO-DE-ETICA-DEL-CENTRO",
    "REGLAMENTO-INTERNO-DEL-CENTRO",
    "REGLAMENTO-DE-PROCEDIMIENTO-DE-INCORPORACION",
    "licencia-de-funcionamiento",
    "37001",
    "9001-Issued",
    "Constancia-de-Registro",
    "Resolucion-autorizacion-MINJUS",
    "CONSTANCIA-INSCRIPCION-RENACE",
    "Cuadro-de-IA",
    "RELACION-DE-ARBITROS",
    "NOMINA-DE-ARBITROS",
    "Nomina-de-Peritos",
    "formato-solicitud-ante-arbitro",
    "SOLICITUD-DE-CONCILIACION",
    "Tarifario-del-Centro",
    "Tabla_Costos",
    "Reglamento-de-Costos-Arbitrales",
    "REGLAMENTO-DE-COSTOS-ADMINISTRATIVOS",
    "Ley-de-Conciliacion-26872",
    "Ley-31165.pdf",
    "DS-017-2021",
    "D.S.-008-2021",
    "RD-754-2021",
    "D.L.-1071",
    "CODIGO-CIVIL",
    "Ley-27444",
    "Constitucion-Politica",
    "Codigo-Procesal-Civil",
    "Ficha-Ruc",
    "copia-literal",
    "manual_usuario_mesa",
    "oficio-minjus",
    "Res.-autorizacion",
)
for i in items:
    name = i.get("archivo") or ""
    if any(w.lower() in name.lower() for w in want):
        if (i.get("kb") or 0) == 0 and name.lower().endswith(".pdf"):
            continue
        print(f"{i.get('kb'):>6}  {name}\n        {i.get('url')}")
