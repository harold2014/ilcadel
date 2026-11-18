import re
import urllib.request

urls = [
    "https://ilcadel.org/arbitraje-de-emergencia/",
    "https://ilcadel.org/conciliacion-ambas-partes-en-el-dia/",
    "https://ilcadel.org/poder-por-acta-ante-centro-de-conciliacion/",
    "https://ilcadel.org/intermediacion-electronica-con-el-poder-judicial/",
    "https://ilcadel.org/intermediacion-electronica-ante-diversas-entidades-del-estado/",
    "https://ilcadel.org/conciliacion-para-divorcio-rapido-2/",
    "https://ilcadel.org/audiencia-virtual-de-conciliacion/",
    "https://ilcadel.org/constitucion-de-empresas-en-linea/",
    "https://ilcadel.org/consulta-legal-y-arbitrajes-2/",
    "https://ilcadel.org/conciliacion-pre-judicial-2/",
    "https://ilcadel.org/conciliacion-en-accidentes-de-transito/",
    "https://ilcadel.org/conciliacion-en-accidentes-de-transito-2/",
]
pat = re.compile(r"https://ilcadel.org/wp-content/uploads/[^\"']+\.(?:webp|jpg|jpeg|png)", re.I)
for u in urls:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
    seen = []
    for m in pat.findall(html):
        name = m.split("/")[-1]
        if name not in seen:
            seen.append(name)
    print(u.split("/")[-2])
    print(" ", ", ".join(seen[:15]) or "(sin imagen)")
