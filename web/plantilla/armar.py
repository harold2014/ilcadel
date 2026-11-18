# -*- coding: utf-8 -*-
"""Arma las páginas del menú con la información publicada en ilcadel.org."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
U = "https://ilcadel.org/wp-content/uploads/"
DOCS = {
    "reglamento2026": U + "2026/04/REGLAMENTO-PROCESAL-DE-ARBITRAJE-2026.docx.pdf",
    "etica": U + "2026/05/CODIGO-DE-ETICA-DEL-CENTRO-DE-ARBITRAJE-Y-ANEXO-UNICO.pdf",
    "interno": U + "2026/05/REGLAMENTO-INTERNO-DEL-CENTRO-DE-ARBITRAJE-Y-ANEXO-UNICO.pdf",
    "incorporacion": U + "2026/05/REGLAMENTO-DE-PROCEDIMIENTO-DE-INCORPORACION-DE-ARBITROS-Y-PERITOS-CON-ANEXO-UNICO.pdf",
    "licencia": U + "2026/05/licencia-de-funcionamiento-valido.pdf",
    "costos": U + "2026/04/Reglamento-de-Costos-Arbitrales-ILCADEL.doc.pdf",
    "costos_admin": U + "2026/10/REGLAMENTO-DE-COSTOS-ADMINISTRATIVOS.pdf",
    "tabla": U + "2026/10/Tabla_Costos_Arbitraje_y_Medios_Pago-2.pdf",
    "tarifario": U + "2026/10/Tarifario-del-Centro-de-Conciliacion-ILCADEL-1.pdf",
    "iso37001": U + "2025/12/INSTITUTO-LATINOAMERICANO-DE-CONCILIACION-ARBITRAJE-Y-DEFENSA-LEGAL-37001-Issued.doc.pdf",
    "iso9001": U + "2025/12/INSTITUTO-LATINOAMERICANO-DE-CONCILIACION-ARBITRAJE-Y-DEFENSA-LEGAL-9001-Issued.doc.pdf",
    "oece": U + "2026/10/Constancia-de-Registro-de-Incorporacion-IA-B-000059-2026.pdf",
    "minjus": U + "2026/04/Resolucion-autorizacion-MINJUS.pdf",
    "renace": U + "2026/05/CONSTANCIA-INSCRIPCION-RENACE.pdf",
    "cuadro": U + "2026/10/Cuadro-de-IA.-Inscritas-en-Regaju-Oece-2026.pdf",
    "arbitros": U + "2026/04/RELACION-DE-ARBITROS-1.pdf",
    "peritos": U + "2026/04/Nomina-de-Peritos-Acreditados-.pdf",
    "emergencia": U + "2025/12/formato-solicitud-ante-arbitro-de-emergencia.docx",
    "solicitud": U + "2025/12/SOLICITUD-DE-CONCILIACION.docx",
    "ley26872": U + "2025/12/Ley-de-Conciliacion-26872.pdf",
    "rd754": U + "2025/12/RD-754-2021-JUS-DGDPAJ-DCMA-Adecuacion-de-for.pdf",
    "oficio": U + "2025/12/oficio-minjus-autoriza-audiencia-virtual-y-otr.pdf",
    "res_conc": U + "2025/12/Res.-autorizacion-de-Centro-de-Conciliacion.pdf",
    "cpc": U + "2025/12/Codigo-Procesal-Civil.pdf",
    "constitucion": U + "2025/12/Constitucion-Politica-del-Peru.pdf",
    "copia": U + "2025/12/copia-literal-ilcadel-2022.pdf",
    "manual": U + "2026/05/manual_usuario_mesa_de_partes.pdf",
    "ley32069": U + "2026/03/Ley-32069-ley-de-contrataciones-publicas.pdf",
}
WA = "https://wa.me/51999835661"
IMG = "referencia/imagenes"

NAV = [
    ("institucion.html", "Institución", "institucion"),
    ("arbitraje.html", "Arbitraje", "arbitraje"),
    ("conciliacion.html", "Conciliación", "conciliacion"),
    ("defensa-legal.html", "Defensa Legal", "defensa"),
    ("certificaciones.html", "Certificaciones", "certificaciones"),
    ("contacto.html", "Contacto", "contacto"),
]


def nav_html(active):
    links = []
    for href, label, key in NAV:
        cls = ' class="is-active"' if key == active else ""
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{href}"{cls}{current}>{label}</a>')
    links.append('<a class="btn btn--navy nav__cta-mobile" href="mesa-de-partes.html">Mesa de Partes Virtual</a>')
    return "\n      ".join(links)


def page(filename, title, description, active, body):
    html = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | ILCADEL</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#101F38">
  <link rel="icon" href="assets/img/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
<a class="skip-link" href="#contenido">Saltar al contenido</a>
<div class="topbar">
  <div class="container topbar__inner">
    <div class="topbar__group">
      <span class="topbar__item"><a href="tel:+5115101613">(01) 510 1613</a></span>
      <span class="topbar__item"><a href="{WA}" target="_blank" rel="noopener">WhatsApp +51 999 835 661</a></span>
      <span class="topbar__item topbar__item--hide-sm">Lima · Huacho · Calgary</span>
    </div>
    <div class="topbar__group">
      <a href="reclamaciones.html">Libro de Reclamaciones</a>
      <a href="consulta.html">Consulta de Expedientes</a>
    </div>
  </div>
</div>
<header class="header" id="header">
  <div class="container header__inner">
    <a class="header__logo" href="index.html" aria-label="ILCADEL — Inicio">
      <img src="assets/img/logo.png" alt="ILCADEL — Instituto Latinoamericano de Conciliación, Arbitraje y Defensa Legal" width="432" height="144">
    </a>
    <button class="nav-toggle" type="button" aria-controls="nav" aria-expanded="false" aria-label="Abrir menú">
      <span class="nav-toggle__bars"></span>
    </button>
    <nav class="nav" id="nav" aria-label="Principal">
      {nav_html(active)}
    </nav>
    <a class="btn btn--navy header__cta" href="mesa-de-partes.html">Mesa de Partes Virtual</a>
  </div>
</header>
<main id="contenido">
{body}
</main>
<footer class="footer">
  <div class="container footer__inner">
    <div class="footer__grid">
      <div class="footer__col">
        <div class="footer__brand">ILCADEL<span>.</span></div>
        <p>Instituto Latinoamericano de Conciliación, Arbitraje y Defensa Legal. Constituido en 1990.</p>
      </div>
      <div class="footer__col">
        <div class="footer__title">Servicios</div>
        <a href="arbitraje.html">Arbitraje</a>
        <a href="conciliacion.html">Conciliación</a>
        <a href="defensa-legal.html">Defensa legal</a>
        <a href="contacto.html">Asesoría</a>
      </div>
      <div class="footer__col">
        <div class="footer__title">Institución</div>
        <a href="institucion.html#historia">Nuestra historia</a>
        <a href="institucion.html#equipo">Nuestro equipo</a>
        <a href="galeria.html">Galería</a>
        <a href="{DOCS['licencia']}" target="_blank" rel="noopener">Licencia municipal</a>
      </div>
      <div class="footer__col">
        <div class="footer__title">Atención</div>
        <a href="mesa-de-partes.html">Mesa de Partes Virtual</a>
        <a href="consulta.html">Consulta de expedientes</a>
        <a href="arbitraje.html#calculadora">Calculadora de arbitraje</a>
        <a href="https://www.facebook.com/ilcadel.org/" target="_blank" rel="noopener">Facebook</a>
      </div>
      <div class="footer__col">
        <a href="reclamaciones.html" class="libro">Libro de Reclamaciones</a>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span id="year">2026</span> ILCADEL. Todos los derechos reservados.</span>
      <nav aria-label="Legal">
        <a href="{DOCS['etica']}" target="_blank" rel="noopener">Código de Ética</a>
        <a href="certificaciones.html">Certificaciones</a>
      </nav>
    </div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/51987298765?text=Hola%20ILCADEL%2C%20quisiera%20hacer%20una%20consulta." target="_blank" rel="noopener" aria-label="Escribir por WhatsApp a Secretaría General">
  <svg aria-hidden="true" width="30" height="30" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2a9.9 9.9 0 0 0-8.5 15l-1.4 5 5.1-1.3A9.9 9.9 0 1 0 12.04 2zm5.8 14.1c-.24.68-1.4 1.3-1.94 1.35-.5.05-1.12.07-1.8-.11a16.4 16.4 0 0 1-1.63-.6 12.7 12.7 0 0 1-4.9-4.33c-.36-.48-.86-1.3-.86-2.47 0-1.17.6-1.75.83-1.99.22-.24.48-.3.64-.3h.46c.15 0 .35-.06.55.42.2.5.68 1.68.74 1.8.06.12.1.26.02.42-.08.16-.12.26-.24.4-.12.14-.25.31-.36.42-.12.12-.24.25-.1.49.14.24.62 1.02 1.33 1.65.92.82 1.69 1.07 1.93 1.19.24.12.38.1.52-.06.14-.16.6-.7.76-.94.16-.24.32-.2.54-.12.22.08 1.4.66 1.64.78.24.12.4.18.46.28.06.1.06.58-.18 1.25z"/></svg>
</a>
<script src="js/main.js" defer></script>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")
    print(filename)


def hero(kicker, h1, lead):
    return f"""  <header class="page-hero">
    <div class="container">
      <div class="kicker">{kicker}</div>
      <h1>{h1}</h1>
      <p>{lead}</p>
    </div>
  </header>"""


def card(title, text, image, href, label):
    img = f'<img class="service__photo" src="{IMG}/{image}" alt="">' if image else ""
    return f"""<article class="card service reveal">{img}
          <h3 class="service__title">{title}</h3>
          <p class="service__list">{text}</p>
          <a class="service__link" href="{href}">{label}</a>
        </article>"""


pages = {}

pages["institucion.html"] = (
    "Institución",
    "ILCADEL, constituido el 11 de febrero de 1990 en Huacho. Misión, visión, historia y equipo.",
    "institucion",
    hero("Institución", "Quiénes somos", "El Instituto Latinoamericano de Conciliación, Arbitraje y Defensa Legal es una institución especializada en la prevención y solución alternativa de controversias.")
    + """
  <section class="section">
    <div class="container about">
      <div class="about__media about__media--photo reveal">
        <img src="referencia/imagenes/institucional/QSOMOS.webp" alt="Balanza de la justicia, imagen institucional de ILCADEL">
      </div>
      <div class="prose reveal">
        <p>Constituido en 1990, ILCADEL cuenta con sede principal en Lima, una sede en Huacho y representación institucional en Calgary (Canadá).</p>
        <p>Durante más de dos décadas ha brindado asesoría y acompañamiento a personas naturales, personas jurídicas y entidades públicas en la resolución eficiente, imparcial y confidencial de sus conflictos. Opera con certificación ISO 9001 (gestión de la calidad) e ISO 37001 (gestión antisoborno).</p>
        <h3>Por qué elegir la institución</h3>
        <ul>
          <li>Respaldo oficial: acreditación del Ministerio de Justicia y Derechos Humanos e inscripción ante el OECE.</li>
          <li>Más de dos décadas dedicadas a la gestión de controversias.</li>
          <li>Procesos bajo ISO 9001 e ISO 37001.</li>
          <li>Audiencias presenciales, virtuales e híbridas.</li>
        </ul>
      </div>
    </div>
  </section>
  <section class="section section--gray">
    <div class="container">
      <div class="mv">
        <article class="card mv__item reveal">
          <div class="mv__title">Misión</div>
          <p>Brindar a personas, empresas y entidades del Estado mecanismos eficientes y confiables de solución de controversias, a través de la conciliación extrajudicial, el arbitraje institucional nacional e internacional y la defensa legal. Actuamos con imparcialidad, celeridad, confidencialidad y seguridad jurídica, en audiencias presenciales, virtuales e híbridas.</p>
        </article>
        <article class="card mv__item reveal">
          <div class="mv__title">Visión</div>
          <p>Ser la institución de referencia en América Latina en conciliación, arbitraje y resolución de disputas, reconocida por la solidez técnica de sus decisiones, la integridad de sus procedimientos y la excelencia de sus profesionales.</p>
        </article>
      </div>
    </div>
  </section>
  <section class="section" id="historia">
    <div class="container prose">
      <div class="eyebrow">Nuestra historia</div>
      <h2>Génesis y trayectoria</h2>
      <p>ILCADEL es una persona jurídica de derecho privado instituida mediante acta de fundación del 11 de febrero de 1990, en Huacho, capital de la región Lima. La constitución se formalizó por escritura pública del 12 de marzo de 1990, ante el notario de Lima Ricardo Ortiz de Zevallos Villarán, e inscrita en la Partida N.º 10000681 del Registro de Personas Jurídicas de la Oficina Registral de Huacho, Zona Registral IX, Sede Lima.</p>
      <p>Fue constituido por William Franz Tufiño Pijo, actual director general, abogado, conciliador extrajudicial y árbitro de derecho. Inició actividades como Asociación Civil Educativa «Instituto Latinoamericano de Especialización Profesional», con fines de enseñanza superior, actualización profesional, descentralización educativa y promoción de la paz.</p>
      <p>A partir de 2001 institucionalizó los medios alternativos de solución de conflictos y creó tres órganos adscritos: el Centro Latinoamericano de Conciliación, autorizado por el Ministerio de Justicia; el Centro de Arbitraje, para administrar arbitrajes de derecho; y el área de Defensa Legal, ante el Poder Judicial y otras entidades, en materia civil, administrativa, minera y energética, entre otras.</p>
      <p>En defensa legal ha patrocinado a la Comunidad Campesina de Llamac (Áncash) frente a la empresa minera Santa Luisa; a la Comunidad Campesina de Pachangara frente a Los Quenuales; y a la Comunidad Campesina de Tongos frente a Cheves S.A., entre otros casos.</p>
      <p>El 25 de abril de 2005 donó una camioneta Nissan Mistral a la Municipalidad Distrital de San Francisco de Asís de Yarusyacán (Pasco), aprobada por Resolución Ministerial N.º 457-2005-EF/15. El 25 de julio de 2007 donó una camioneta Ford F-150 a la Municipalidad Distrital El Carmen (Churcampa, Huancavelica).</p>
      <div class="actions">
        <a class="btn btn--outline-navy" href="__COPIA__" target="_blank" rel="noopener">Copia literal 2022</a>
        <a class="btn btn--outline-navy" href="galeria.html">Galería</a>
      </div>
    </div>
  </section>
  <section class="section section--gray" id="equipo">
    <div class="container">
      <div class="eyebrow">Nuestro equipo</div>
      <h2 class="section-title">Consejo y secretarías</h2>
      <div class="cards" style="margin-top:32px">
        <article class="card person reveal"><div class="person__role">Director general · Asociado fundador</div><strong>William Franz Tufiño Pijo</strong><p>Abogado, conciliador extrajudicial y árbitro de derecho. Director del Centro de Conciliación y secretario general de ese centro.</p></article>
        <article class="card person reveal"><div class="person__role">Directora del Centro de Arbitraje</div><strong>Yeliz Aysse Tufiño Calixto</strong><p>Abogada.</p></article>
        <article class="card person reveal"><div class="person__role">Presidente del Consejo Superior de Arbitraje</div><strong>Oswaldo Carlos Kubota Gave</strong></article>
        <article class="card person reveal"><div class="person__role">Consejo Superior de Arbitraje</div><strong>Luis Alfredo Yalan Ramirez</strong><p>Miembro.</p></article>
        <article class="card person reveal"><div class="person__role">Consejo Superior de Arbitraje</div><strong>Viviana Acuna Goveya</strong><p>Miembro.</p></article>
        <article class="card person reveal"><div class="person__role">Secretario general</div><strong>Fredy Cristobal Dominguez Broncano</strong></article>
        <article class="card person reveal"><div class="person__role">Secretario arbitral</div><strong>Steve Bryan Alim Cuadrado Castro</strong></article>
        <article class="card person reveal"><div class="person__role">Secretaria arbitral técnica</div><strong>Lucia Mabell Reyes Melgar</strong></article>
      </div>
      <div class="prose" style="margin-top:40px">
        <h3>Abogados del Centro de Conciliación</h3>
        <ul>
          <li>Jose Abelardo Alvarado Alegre — Reg. N.° 54759, Colegio de Abogados de Lima.</li>
          <li>Juan Chirhuana Juarez — Reg. N.° 41469, Colegio de Abogados de Lima.</li>
          <li>William Franz Tufiño Pijo — Reg. N.° 4408, Colegio de Abogados de La Libertad.</li>
          <li>Arabela Xiomara Guillen Rengifo.</li>
        </ul>
        <h3>Conciliadores extrajudiciales</h3>
        <ul>
          <li>Juan Chirhuana Juarez — Reg. 24850 y Reg. 2633. Asuntos de familia.</li>
          <li>William Franz Tufiño Pijo — Reg. N.° 15682 y Reg. 463. Asuntos de familia.</li>
          <li>Arabela Xiomara Guillen Rengifo.</li>
        </ul>
        <h3>Secretaría arbitral</h3>
        <ul>
          <li>Lucia Mabell Reyes Melgar.</li>
          <li>Steve Bryan Cuadrado Castro.</li>
          <li>Yeliz Aysee Tufiño Calixto.</li>
          <li>Santino Victor Hugo Rios Guerrero.</li>
          <li>Sonia Amelia Salas Navarro.</li>
          <li>Arabela Xiomara Guillen Rengifo.</li>
        </ul>
        <div class="actions">
          <a class="btn btn--outline-navy" href="__ARBITROS__" target="_blank" rel="noopener">Nómina de árbitros</a>
          <a class="btn btn--outline-navy" href="__PERITOS__" target="_blank" rel="noopener">Nómina de peritos</a>
        </div>
      </div>
    </div>
  </section>
""",
)

def wa(text):
    from urllib.parse import quote
    return WA + "?text=" + quote(text)


ARB = [
    ("Arbitrajes de Contrataciones Públicas", "Resuelve conflictos con el Estado en contratos de bienes, servicios, consultorías y obras públicas.", "servicios/Contrataciones-Publicas-1.webp", "Arbitrajes en Contrataciones Públicas"),
    ("Arbitrajes de Derecho Privado", "Conflictos civiles, comerciales, deudas, desalojos y controversias inmobiliarias y de construcción, con calidad de cosa juzgada.", "servicios/Derecho-Privado-1.webp", "Arbitrajes de Derecho Privado"),
    ("Arbitrajes de Emergencia", "Órdenes cautelares antes de la constitución del tribunal arbitral, cuando hay riesgo de daño irreparable o hay que preservar el estado de cosas.", "servicios/Emergencia.webp", "Arbitrajes de Emergencia"),
    ("Seguros, societario, consumo y laboral", "Controversias de seguros, socios, consumidores y asuntos laborales de personal de dirección con convenio arbitral.", "servicios/Consulta-legal-y-arbitrajes-.webp", "Arbitrajes de Seguros, Societarios, de Consumo y Laborales"),
    ("Arbitraje marítimo", "Comercio marítimo, navegación y operaciones portuarias: fletamentos, sobrestadías, conocimientos de embarque, seguros y concesiones portuarias.", "servicios/Arbitraje-maritimo.webp", "Arbitraje Marítimo"),
    ("Ejecución de garantías y remates", "Hipotecas, garantías mobiliarias, fideicomisos y remates.", "servicios/Audiencia-Virtual-de-conciliacion.webp", "Arbitrajes de Ejecución de Garantías y Remates"),
    ("Arbitraje internacional", "Disputas entre partes de distintos países sobre contratos, operaciones e inversiones. D.L. N.° 1071 y Convención de Nueva York de 1958.", "servicios/Arbitraje-internacional.webp", "Arbitraje Internacional"),
]
CON = [
    ("Conciliación de ambas partes en el día", "Audiencia presencial o virtual el mismo día cuando las dos partes están de acuerdo.", "servicios/conciliacion-pre-judicial.webp", "Conciliación para Ambas Partes en el Día"),
    ("Conciliación para divorcio rápido", "Acuerdos sobre alimentos, tenencia, régimen de visitas y liquidación de sociedad de gananciales.", "servicios/Resolucion-de-Divorcios.webp", "Conciliación para Divorcio Rápido"),
    ("Conciliación en accidentes de tránsito", "Acuerdos sobre daños y responsabilidades, con soluciones económicas entre las partes.", "servicios/accidente.webp", "Conciliación en Accidentes de Tránsito"),
    ("Poder por acta", "Facultades ante el secretario general del centro para actuar en un proceso de conciliación.", "servicios/acta.webp", "Poder por Acta ante Centro de Conciliación"),
]

pages["arbitraje.html"] = (
    "Centro de Arbitraje",
    "Centro de Arbitraje ILCADEL. Alternativa privada al Poder Judicial, con laudo vinculante. REGAJU, RENACE e ISO.",
    "arbitraje",
    hero("Centro de Arbitraje", "Tu tranquilidad jurídica en manos de especialistas.", "Alternativa privada, especializada y definitiva al Poder Judicial para controversias civiles y comerciales. El laudo arbitral es vinculante y tiene el mismo valor legal que una sentencia firme.")
    + """
  <section class="section section--gray">
    <div class="container">
      <div class="cards">
""" + "\n".join(card(t, d, img, wa(f"Hola, estoy interesado en el servicio de {asunto} y quisiera recibir más información"), "Solicitar asesoría") for t, d, img, asunto in ARB) + """
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container prose">
      <h2>Materias que administramos</h2>
      <ul>
        <li>Contrataciones con el Estado, Ley N.° 32069: nulidad y resolución contractual, ampliaciones de plazo, adicionales, penalidades, valorizaciones, liquidaciones e indemnizaciones.</li>
        <li>Civil y comercial: incumplimientos, suma de dinero, compraventa, mutuo, locación, obra privada, distribución, franquicia y consorcios.</li>
        <li>Construcción e infraestructura: obra, concesiones, FIDIC, APP y proyectos mineros y energéticos.</li>
        <li>Inmobiliario y desalojos, otorgamiento de escritura, saneamiento, división y partición.</li>
        <li>Ejecución de garantías y remates.</li>
        <li>Seguros y reaseguros, consumo, societario, sucesiones y patrimonio familiar.</li>
        <li>Laboral de personal de dirección, con convenio arbitral posterior al cese.</li>
        <li>Marítimo e internacional, en procedimiento ordinario, sumarísimo o de emergencia.</li>
      </ul>
      <h2>Arbitraje de emergencia</h2>
      <p>Procedimiento expedito para medidas cautelares cuando hay peligro inminente, la demora causa perjuicio o hay que preservar el estado de cosas. El centro designa un árbitro de emergencia. La orden puede ser conservatoria, aseguratoria o provisional, y tiene carácter ejecutivo.</p>
      <p><a href="__EMERGENCIA__">Formato de solicitud ante árbitro de emergencia</a>.</p>
      <h2>Cláusula arbitral</h2>
      <blockquote class="clause">Toda desavenencia, litigio o controversia que pudiera derivarse de este contrato, convenio o acto jurídico, incluidas las de su nulidad o invalidez, serán resueltas a través del arbitraje, mediante fallo definitivo, de conformidad con los Reglamentos del Centro de Arbitraje del Instituto Latinoamericano de Conciliación, Arbitraje y Defensa Legal, a cuya administración, reglamentos y decisión se someten las partes en forma incondicional, declarando conocerlas y aceptarlas en su integridad, incluida la designación de árbitros.</blockquote>
      <h2 id="calculadora">Costos</h2>
      <p>Los costos institucionales se aplican según el tarifario vigente: gastos administrativos, honorarios del árbitro, secretaría arbitral e IGV. La calculadora en línea, con sus tramos de cuantía, entra al administrar el sitio. Mientras tanto están publicados el tarifario y la tabla de medios de pago.</p>
      <div class="actions">
        <a class="btn btn--navy" href="__TABLA__" target="_blank" rel="noopener">Tabla de costos</a>
        <a class="btn btn--outline-navy" href="__COSTOS__" target="_blank" rel="noopener">Reglamento de costos</a>
        <a class="btn btn--outline-navy" href="__REGLAMENTO__" target="_blank" rel="noopener">Reglamento procesal 2026</a>
      </div>
    </div>
  </section>
  <section class="section section--gray">
    <div class="container prose">
      <h2>Comunicado</h2>
      <p>A las entidades del Estado, en especial las de Lima Provincias, municipalidades, empresas, consorcios y cámaras de comercio:</p>
      <p>El Centro de Arbitraje de ILCADEL es la única institución arbitral registrada en REGAJU-OECE con sede en la provincia de Huaura, y una de las dos de Lima Provincias. Es la única de esa región habilitada para controversias de contratos que superen las 2.000 UIT, por una trayectoria institucional superior a cinco años. En Lima, seis centros atienden controversias por encima de ese monto; ILCADEL es uno de ellos.</p>
      <p>También está inscrito en RENACE del Ministerio de Justicia, registro N.° CA00006.</p>
      <p>La Dirección General invita a incorporar al Centro de Arbitraje de ILCADEL en los convenios arbitrales y en las cláusulas de solución de controversias.</p>
      <div class="actions">
        <a class="btn btn--outline-navy" href="__CUADRO__" target="_blank" rel="noopener">Ver cuadro REGAJU</a>
        <a class="btn btn--outline-navy" href="certificaciones.html">Acreditaciones</a>
        <a class="btn btn--outline-navy" href="institucion.html#equipo">Órgano del centro</a>
      </div>
    </div>
  </section>
""",
)

pages["conciliacion.html"] = (
    "Centro de Conciliación",
    "Centro de Conciliación Extrajudicial de ILCADEL, autorizado por el Ministerio de Justicia. Materias, actas y tarifario.",
    "conciliacion",
    hero("Centro de Conciliación", "Autorizado por el Ministerio de Justicia.", "Veinticinco años de conciliación extrajudicial. El acta con acuerdo es título de ejecución y tiene valor similar al de una sentencia firme.")
    + """
  <section class="section">
    <div class="container prose">
      <p>La conciliación extrajudicial es la vía más eficaz, rápida y económica para solucionar un conflicto con otra persona, empresa o entidad estatal, frente a la demora y el costo de un proceso judicial. Está regulada por la Ley N.° 26872, modificada por el D.L. N.° 1070, y por su reglamento.</p>
      <p>En numerosas materias es requisito de procedibilidad: si falta el acta, el juez puede declarar improcedente la demanda.</p>
    </div>
  </section>
  <section class="section section--gray">
    <div class="container">
      <div class="cards">
""" + "\n".join(card(t, d, img, wa(f"Hola, estoy interesado en el servicio de {asunto} y quisiera recibir más información"), "Solicitar asesoría") for t, d, img, asunto in CON) + """
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container prose">
      <h2>Materias civiles</h2>
      <ul>
        <li>Resolución e incumplimiento de contrato, otorgamiento de escritura pública, rectificación de áreas y linderos.</li>
        <li>Ofrecimiento de pago, desalojo, división y partición, indemnización, retracto y petición de herencia.</li>
        <li>Interdicto de retener y recobrar, deudas, obligaciones de dar, hacer y no hacer.</li>
        <li>Mejor derecho de propiedad y posesión, convocatoria a junta o asamblea, reivindicación y cobro de mejoras.</li>
        <li>Asuntos vecinales y materias contractuales de contrataciones del Estado.</li>
      </ul>
      <h2>Asuntos de familia</h2>
      <p>Alimentos, tenencia, régimen de visitas, exoneración o reducción de alimentos y liquidación de sociedad de gananciales. Con la Ley N.° 29876, estas materias y otras de libre disposición derivadas de la relación familiar pueden conciliarse.</p>
      <h2>Cuándo no es exigible</h2>
      <p>La conciliación no es exigible, y en esos casos es facultativa, en procesos de ejecución, tercería, prescripción adquisitiva, retracto, convocatoria a asamblea, impugnación de acuerdos de junta general y nulidad de la Ley General de Sociedades, indemnización derivada de delitos o daños ambientales, y procesos contencioso-administrativos.</p>
      <h2>Cuándo no procede</h2>
      <ul>
        <li>Si la parte emplazada domicilia en el extranjero.</li>
        <li>Procesos contencioso-administrativos, cautelares, de ejecución, de garantías constitucionales y tercerías.</li>
        <li>Violencia familiar.</li>
        <li>Derechos y bienes de incapaces, artículos 43 y 44 del Código Civil.</li>
      </ul>
      <h2>Valor del acta</h2>
      <ul>
        <li>Acuerdo total: mérito de sentencia firme e inapelable y cosa juzgada. Se ejecuta por el proceso de ejecución.</li>
        <li>Inasistencia de la parte invitada a dos audiencias: presunción legal relativa de verdad y multa judicial de 2 a 10 URP.</li>
        <li>Inasistencia de ambas partes: falta de interés para obrar. El juez declara improcedente la demanda.</li>
        <li>Falta de acuerdo, con ambas partes: puede constar la reconvención, con la misma presunción a favor de quien asistió.</li>
        <li>Decisión motivada del conciliador, si el invitado acude y no firma: habilita la demanda y deja constancia de la conducta.</li>
      </ul>
      <p>Costo mínimo publicado: S/ 300. El monto varía según cuantía, materia, número de invitados y lugar de notificación. Para audiencia virtual hay que indicar en la solicitud el correo y el celular de la parte invitada.</p>
      <p>Consultas del centro: <a href="mailto:franztp@ilcadel.org">franztp@ilcadel.org</a>.</p>
      <div class="actions">
        <a class="btn btn--navy" href="__TARIFARIO__" target="_blank" rel="noopener">Tarifario</a>
        <a class="btn btn--outline-navy" href="__SOLICITUD__" target="_blank" rel="noopener">Solicitud de conciliación</a>
        <a class="btn btn--outline-navy" href="__LEY__" target="_blank" rel="noopener">Ley N.° 26872</a>
        <a class="btn btn--outline-navy" href="mesa-de-partes.html">Mesa de partes</a>
      </div>
    </div>
  </section>
""",
)

pages["defensa-legal.html"] = (
    "Defensa Legal",
    "Defensa legal de ILCADEL ante el Poder Judicial, el Ministerio Público y entidades públicas y privadas.",
    "defensa",
    hero("Defensa legal", "Protegemos tus intereses frente a entidades públicas y privadas.", "Defensa de personas naturales y jurídicas ante el Poder Judicial, el Ministerio Público, SAT, SUNARP, SUNAT, ONP y empresas privadas.")
    + f"""
  <section class="section">
    <div class="container about">
      <div class="about__media about__media--photo reveal">
        <img src="{IMG}/servicios/Consultas-Legales.webp" alt="Consulta legal">
      </div>
      <div class="prose reveal">
        <p>El patrocinio cubre las distintas áreas del derecho y, en asuntos de derechos humanos, niñez y personas vulnerables, también organismos internacionales y arbitrajes internacionales.</p>
        <h3>Áreas</h3>
        <ul>
          <li>Civil: contratos, sucesiones, propiedad y obligaciones.</li>
          <li>Familia: alimentos, divorcio, tenencia y régimen de visitas.</li>
          <li>Laboral: despidos, beneficios sociales y accidentes de trabajo.</li>
          <li>Comercial y empresarial: contratos, cobranzas y sociedades.</li>
          <li>Procedimientos administrativos y sancionadores.</li>
          <li>Patrocinio judicial y arbitral.</li>
        </ul>
        <p>La primera orientación informativa es gratuita. Los honorarios se pactan por escrito según complejidad, cuantía y especialidad. Hay planes de pago y, en casos calificados, tarifas reducidas.</p>
        <div class="actions">
          <a class="btn btn--navy" href="{wa('Hola, estoy interesado en el servicio de Consultas Legales y quisiera recibir más información')}">Solicitar asesoría</a>
          <a class="btn btn--outline-navy" href="contacto.html">Escribir al instituto</a>
        </div>
      </div>
    </div>
  </section>
""",
)

pages["certificaciones.html"] = (
    "Certificaciones",
    "Acreditaciones MINJUSDH, RENACE, REGAJU-OECE, ISO 9001 e ISO 37001 de ILCADEL.",
    "certificaciones",
    hero("Certificaciones", "Acreditaciones y certificaciones institucionales", "Constancias oficiales del centro de conciliación, del centro de arbitraje y de los sistemas de gestión.")
    + f"""
  <section class="section">
    <div class="container">
      <div class="cards">
        <article class="card person reveal"><div class="person__role">MINJUSDH</div><strong>Centro de Conciliación Extrajudicial</strong><p>Resolución Directoral N.° 1424-2008-JUS/DNJCMA.</p><a href="{DOCS['minjus']}">Ver resolución</a></article>
        <article class="card person reveal"><div class="person__role">RENACE · MINJUSDH</div><strong>Registro N.° CA00006</strong><p>Decreto Supremo N.° 016-2025-JUS.</p><a href="{DOCS['renace']}">Ver constancia</a></article>
        <article class="card person reveal"><div class="person__role">REGAJU · OECE</div><strong>Constancia N.° IA-B-000059-2026</strong><p>5 de octubre de 2026. Vigencia indeterminada. Contratos cuyo monto original supere 2.000 UIT.</p><a href="{DOCS['oece']}">Ver constancia</a></article>
        <article class="card person reveal"><div class="person__role">ISO 9001</div><strong>Gestión de la calidad</strong><p>Sistema de gestión certificado.</p><a href="{DOCS['iso9001']}">Ver certificado</a></article>
        <article class="card person reveal"><div class="person__role">ISO 37001</div><strong>Gestión antisoborno</strong><p>Sistema de gestión certificado.</p><a href="{DOCS['iso37001']}">Ver certificado</a></article>
        <article class="card person reveal"><div class="person__role">Municipalidad</div><strong>Licencia de funcionamiento</strong><p>Licencia municipal vigente de la sede.</p><a href="{DOCS['licencia']}">Ver licencia</a></article>
      </div>
      <div class="resources">
        <a class="card resource reveal" href="{DOCS['reglamento2026']}"><span><span class="resource__title">Reglamento Procesal de Arbitraje 2026</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['interno']}"><span><span class="resource__title">Reglamento interno</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['etica']}"><span><span class="resource__title">Código de Ética</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['incorporacion']}"><span><span class="resource__title">Incorporación de árbitros y peritos</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['cuadro']}"><span><span class="resource__title">Cuadro de instituciones REGAJU 2026</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['ley26872']}"><span><span class="resource__title">Ley de Conciliación N.° 26872</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['cpc']}"><span><span class="resource__title">Código Procesal Civil</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['constitucion']}"><span><span class="resource__title">Constitución Política del Perú</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['rd754']}"><span><span class="resource__title">R.D. 754-2021-JUS, formatos de actas</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['oficio']}"><span><span class="resource__title">Oficio MINJUS, audiencia virtual</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['res_conc']}"><span><span class="resource__title">Resolución de autorización del centro</span><span class="resource__meta">PDF</span></span></a>
        <a class="card resource reveal" href="{DOCS['copia']}"><span><span class="resource__title">Copia literal ILCADEL 2022</span><span class="resource__meta">PDF</span></span></a>
      </div>
    </div>
  </section>
""",
)

pages["mesa-de-partes.html"] = (
    "Mesa de Partes Virtual",
    "Mesa de Partes Virtual de ILCADEL. Solicitudes de conciliación, arbitraje, anexos y escritos, las 24 horas.",
    "",
    hero("Mesa de Partes Virtual", "Presenta tu solicitud a cualquier hora.", "Conciliación, arbitraje, anexos y escritos. Atención 24 horas, los 7 días. También puedes pedir audiencia virtual. Ley N.° 31170.")
    + f"""
  <section class="section">
    <div class="container" style="display:flex;flex-wrap:wrap;gap:48px;align-items:flex-start">
      <div class="prose" style="flex:1 1 320px">
        <p>Completa el formulario. El archivo de la solicitud va en PDF y no debe pasar de 20 MB. Si el escrito o los anexos pesan más, envíalos a <a href="mailto:recepcionvirtual@ilcadel.org">recepcionvirtual@ilcadel.org</a>.</p>
        <p><a href="{DOCS['manual']}">Manual de usuario de la mesa de partes</a>.</p>
        <p><a href="{DOCS['solicitud']}">Modelo de solicitud de conciliación</a>.</p>
      </div>
      <form class="form reveal" data-success="Recibimos los datos de tu solicitud. Adjunta el PDF y envíalo a recepcionvirtual@ilcadel.org si aún no está en el registro. El envío directo desde esta mesa se conecta al administrar el sitio." novalidate>
        <div class="field field--full">
          <label for="m-nombre">Nombres y apellidos o razón social</label>
          <input id="m-nombre" name="nombre" type="text" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field">
          <label for="m-doc">DNI o RUC</label>
          <input id="m-doc" name="documento" type="text" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field">
          <label for="m-mail">Correo electrónico</label>
          <input id="m-mail" name="correo" type="email" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field field--full">
          <label for="m-pdf">Solicitud en PDF (máximo 20 MB)</label>
          <input id="m-pdf" name="solicitud" type="file" accept="application/pdf,.pdf" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field field--full">
          <label for="m-msg">Detalle</label>
          <textarea id="m-msg" name="mensaje" rows="4" required></textarea>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="form__footer">
          <span class="form__note">Solo se aceptan PDF.</span>
          <button type="submit" class="btn btn--navy">Presentar solicitud</button>
        </div>
        <p class="form__status" role="status"></p>
      </form>
    </div>
  </section>
""",
)

pages["consulta.html"] = (
    "Consulta de Expedientes",
    "Consulta de expedientes de ILCADEL, en el mismo sitio. Número de expediente y verificación.",
    "",
    hero("Consulta de expedientes", "Busca un expediente del instituto.", "Ingresa los cinco primeros dígitos del número. Esta consulta es una sección de ILCADEL, no un sitio aparte.")
    + """
  <section class="section">
    <div class="container" style="display:flex;flex-wrap:wrap;gap:48px;align-items:flex-start">
      <form class="form reveal" id="consultaForm" data-success="Anotamos el número y el código. El resultado del expediente se mostrará en esta misma página cuando el registro quede unido al sitio." novalidate>
        <div class="field field--full">
          <label for="e-num">N.° de expediente</label>
          <input id="e-num" name="expediente" type="text" inputmode="numeric" maxlength="5" pattern="[0-9]{5}" placeholder="00001" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <p class="form__note" style="grid-column:1/-1">Ejemplo: 00001-2005-0-1817-JR-CO-06 se consulta como 00001.</p>
        <div class="field">
          <label for="e-cod">Código de verificación</label>
          <input id="e-cod" name="codigo" type="text" autocomplete="off" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="form__footer">
          <span class="form__note">Campos obligatorios. La sesión de consulta publicada dura 10 minutos.</span>
          <button type="submit" class="btn btn--navy">Consultar expediente</button>
        </div>
        <p class="form__status" role="status"></p>
      </form>
      <div class="prose" style="flex:1 1 360px">
        <h2>Qué muestra el resultado</h2>
        <ul>
          <li>Reporte: número, fecha de inicio, órgano, especialidad, árbitro, secretario arbitral, etapa, ubicación, proceso y materia.</li>
          <li>Partes: demandante y demandado, persona natural o jurídica.</li>
          <li>Seguimiento: actos, resoluciones, notificaciones y PDF.</li>
        </ul>
        <p>El código de verificación y la lectura del registro se unen a esta misma pantalla cuando el expediente se administre desde el sitio. Hasta ese momento el formulario ya recoge el número y el código con las reglas publicadas.</p>
      </div>
    </div>
  </section>
""",
)

pages["reclamaciones.html"] = (
    "Libro de Reclamaciones",
    "Libro de reclamaciones de ILCADEL.",
    "",
    hero("Libro de reclamaciones", "Deja constancia de tu reclamo.", "Nombre, documento, fecha y el detalle de lo que pides como consumidor.")
    + """
  <section class="section">
    <div class="container">
      <form class="form reveal" data-success="Recibimos tu reclamo. El libro virtual queda registrado en la administración del sitio; si necesitas respuesta inmediata escribe a recepcionvirtual@ilcadel.org." novalidate>
        <div class="field">
          <label for="r-nombre">Nombre</label>
          <input id="r-nombre" name="nombre" type="text" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field">
          <label for="r-mail">Correo electrónico</label>
          <input id="r-mail" name="correo" type="email" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field">
          <label for="r-tipo">Tipo de documento</label>
          <select id="r-tipo" name="tipo">
            <option>DNI</option>
            <option>CE</option>
            <option>RUC</option>
            <option>Pasaporte</option>
          </select>
        </div>
        <div class="field">
          <label for="r-num">N.° de documento</label>
          <input id="r-num" name="documento" type="text" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field">
          <label for="r-fecha">Fecha de reclamo</label>
          <input id="r-fecha" name="fecha" type="date" required>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="field field--full">
          <label for="r-det">Detalle de la reclamación y pedido del consumidor</label>
          <textarea id="r-det" name="mensaje" rows="5" required></textarea>
          <span class="field__error" aria-live="polite"></span>
        </div>
        <div class="form__footer">
          <span class="form__note">También puedes escribir a recepcionvirtual@ilcadel.org.</span>
          <button type="submit" class="btn btn--navy">Enviar reclamo</button>
        </div>
        <p class="form__status" role="status"></p>
      </form>
    </div>
  </section>
""",
)

pages["contacto.html"] = (
    "Contacto",
    "Sedes de ILCADEL en Lima, Huacho y Calgary, y formulario de consulta.",
    "contacto",
    """
  <section class="section section--navy" id="contacto">
    <div class="container contact">
      <div class="contact__info reveal">
        <div>
          <div class="eyebrow">Contacto</div>
          <h2 class="section-title">Conversemos sobre tu caso</h2>
          <p class="lead" style="color:#DCE2EE;margin-top:12px">Para recibir una respuesta del equipo, deja tus datos. La primera orientación informativa es gratuita.</p>
        </div>
        <div class="sedes">
          <div><div class="sede__name">Oficina Lima</div>Jr. Huancavelica 421, Of. 203, Lima</div>
          <div><div class="sede__name">Sede central</div>Av. Domingo Mandamiento 299, Int. H, Hualmay, Huacho, Huaura, Lima</div>
          <div><div class="sede__name">Sede Huacho</div>Av. Salaverry 568, 2.° piso, Huacho</div>
          <div><div class="sede__name">Sede Canadá</div>25 Chapala Bay SE, Calgary, Alberta T2X 3M4</div>
        </div>
        <div class="phones">
          <div>Central: <a href="tel:+5115101613">(01) 510 1613</a></div>
          <div>Dirección General: <a href="https://wa.me/51999835661" target="_blank" rel="noopener">+51 999 835 661</a></div>
          <div>Secretaría General: <a href="https://wa.me/51987298765" target="_blank" rel="noopener">+51 987 298 765</a></div>
          <div>Canadá: <a href="https://wa.me/18257475773" target="_blank" rel="noopener">+1 825 747 5773</a></div>
          <div>Mesa de partes: <a href="mailto:recepcionvirtual@ilcadel.org">recepcionvirtual@ilcadel.org</a></div>
        </div>
      </div>
      <form class="form reveal" id="contactForm" novalidate>
        <div class="field"><label for="c-nombre">Nombre</label><input id="c-nombre" name="nombre" required><span class="field__error" aria-live="polite"></span></div>
        <div class="field"><label for="c-tel">Celular</label><input id="c-tel" name="telefono" type="tel" required><span class="field__error" aria-live="polite"></span></div>
        <div class="field"><label for="c-mail">Correo electrónico</label><input id="c-mail" name="correo" type="email" required><span class="field__error" aria-live="polite"></span></div>
        <div class="field">
          <label for="c-area">Área de consulta</label>
          <select id="c-area" name="area">
            <option>Arbitraje</option>
            <option>Arbitraje de emergencia</option>
            <option>Conciliación</option>
            <option>Defensa legal</option>
            <option>Junta de resolución de disputas</option>
            <option>Administración</option>
            <option>Otros</option>
          </select>
        </div>
        <div class="field field--full"><label for="c-msg">Mensaje</label><textarea id="c-msg" name="mensaje" rows="4" required></textarea><span class="field__error" aria-live="polite"></span></div>
        <div class="form__footer">
          <span class="form__note">Al enviar aceptas el tratamiento de tus datos conforme a la Ley N.° 29733.</span>
          <button type="submit" class="btn btn--gold">Enviar</button>
        </div>
        <p class="form__status" role="status"></p>
      </form>
    </div>
  </section>
""",
)

pages["galeria.html"] = (
    "Galería",
    "Galería de ILCADEL y notas sobre el valor del arbitraje y del acta de conciliación.",
    "",
    hero("Galería", "Fotos y el marco de nuestro trabajo.", "La Constitución reconoce la función jurisdiccional del arbitraje. El acta de conciliación con acuerdo tiene valor de cosa juzgada.")
    + f"""
  <section class="section">
    <div class="container">
      <div class="gallery">
        <figure class="reveal"><img src="{IMG}/galeria/Fotografia1.webp" alt="Fotografía institucional 1"></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Fotografia2.webp" alt="Fotografía institucional 2"></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Fotografia3.webp" alt="Fotografía institucional 3"></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Fotografia4.webp" alt="Fotografía institucional 4"></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Fotografia5.webp" alt="Fotografía institucional 5"></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Huacho.webp" alt="Huacho, sede de origen de ILCADEL"><figcaption>Huacho, donde se fundó el instituto en 1990.</figcaption></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Noticia1.webp" alt=""></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Noticia2.webp" alt=""></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Noticia3.webp" alt=""></figure>
        <figure class="reveal"><img src="{IMG}/galeria/Noticia4.webp" alt=""></figure>
      </div>
      <div class="prose" style="margin-top:48px">
        <h2>El arbitraje y el acta</h2>
        <p>El artículo 139 de la Constitución otorga facultad jurisdiccional privada al arbitraje. El proceso se desarrolla con autonomía, sin intervención de otra autoridad. El laudo tiene valor similar al de una sentencia judicial firme.</p>
        <p>El acta de conciliación con acuerdo también tiene ese valor y calidad de cosa juzgada. Si una parte incumple, se ejecuta mediante un proceso de ejecución.</p>
      </div>
    </div>
  </section>
""",
)

REPL = {
    "__COPIA__": DOCS["copia"],
    "__ARBITROS__": DOCS["arbitros"],
    "__PERITOS__": DOCS["peritos"],
    "__EMERGENCIA__": DOCS["emergencia"],
    "__TABLA__": DOCS["tabla"],
    "__COSTOS__": DOCS["costos"],
    "__REGLAMENTO__": DOCS["reglamento2026"],
    "__CUADRO__": DOCS["cuadro"],
    "__TARIFARIO__": DOCS["tarifario"],
    "__SOLICITUD__": DOCS["solicitud"],
    "__LEY__": DOCS["ley26872"],
}

for filename, (title, description, active, body) in pages.items():
    for token, url in REPL.items():
        body = body.replace(token, url)
    page(filename, title, description, active, body)

