# Registro de Cambios — Agente SEO

Cada cambio implementado se registra aquí con fecha, URL afectada y resultado medido a 14/28/56 días.

| Fecha | Cambio | URLs afectadas | Riesgo | Aprobado por | Resultado 14d | Resultado 28d | Resultado 56d |
|-------|--------|---------------|--------|-------------|--------------|--------------|--------------|
| 2026-11-03 | Optimizar title + meta description | /categoria-producto/tinas-de-hidromasaje/ | Medio | Jefe | — | — | — |
| 2026-11-04/05 | Optimizar title + meta description (exp-002) | /categoria-producto/planchas-acrilico/ | Bajo | Jefa | revisar 2026-11-18 | — | — |
| 2026-11-10 | Nueva página SEO transaccional (exp-009) | /acrilico-transparente/ (nueva) | Bajo | Jefe | revisar 2026-11-24 | revisar 2026-12-08 | — |

**Detalle del cambio 2026-11-03:**
- Title: "Tinas de Hidromasaje y Jacuzzi 1 y 2 Personas desde $479.990" → "Tinas de Hidromasaje y Jacuzzi desde $479.990 · Retiro hoy en Santiago"
- Meta: agrega "Importador directo, 29 años", "1 año de garantía", pone "Jacuzzi" primero
- Rama: `agente/seo-tinas-meta` — commit d1d6b84
- Medir: CTR en GSC a 14 días. Control: /categoria-producto/planchas-acrilico/ (sin cambios)

**Detalle del cambio 2026-11-04/05 (exp-002):**
- Title final: "Planchas de Acrílico a Medida · Transparente, Colores y Espejo | Polyplas"
- Meta final: "Planchas de acrílico AA transparente, traslúcido y de colores. Corte a medida en Santiago — importador directo con los mejores precios. Retiro hoy · Despacho gratis RM desde $350.000."
- Commits en Polyplas-web: c2ab296 (04-nov) y 0a665a8 (05-nov)
- Baseline: 8.525 impresiones en 28 días, CTR 1,4%. Objetivo: CTR ≥ 2,5%.
- Registrado por Tatis el 2026-11-10 al cerrar la propuesta seo::1793917050737, que había quedado abierta en la bandeja.
- Ojo: esta URL era el control del cambio de tinas del 03-nov; desde el 04-nov ya no sirve como control.

**Detalle del cambio 2026-11-10 (exp-009):**
- Keyword objetivo: "acrílico transparente" — 1.270 impresiones/mes, CTR 0.3% (4 clics), posición media sin página propia
- Página nueva: /acrilico-transparente/ — H1, tabla espesores con precios reales (data-crm-desde), usos industriales, comparativa vs vidrio, 5 FAQs
- Schema: BreadcrumbList + FAQPage (candidato a rich results)
- WhatsApp con ref pp-at01 para tracking de leads por canal
- Commit: 07ae94d en Polyplas-web
- Objetivo: posición top 6 y CTR ≥ 3% en 56 días → ~38 clics/mes adicionales
- Medir: GSC impressiones + CTR + posición en /acrilico-transparente/. Control: /guia-de-acrilicos/ (sin cambios)
| 2026-11-12 | 2 landings B2B nuevas (PR #2 Polyplas-web): /acrilico-para-exhibidores-pop/ y /acrilico-para-letreros-luminosos/. Title + description + FAQPage. Riesgo bajo (solo páginas nuevas). Próximo: enlaces internos desde categoría planchas (riesgo medio, aparte) y medir impresiones a 28 y 56 días | ✅ Publicado 2026-11-12 | Medir 2026-12-10 y 2027-01-07 |
| 2026-11-12 | Enlace interno desde /categoria-producto/planchas-acrilico/ (bloque "¿Compras acrílico por volumen para tu empresa?") a las 2 landings B2B (PR #5). Riesgo medio: contenido nuevo en una página que posiciona; no se tocó título, URL ni módulos existentes. Control: posición y CTR de la categoría a 14 y 28 días | ✅ Publicado 2026-11-12 | Medir 2026-11-26 y 2026-12-10 |
| 2026-11-12 | Estrategia SEO landings B2B (ESTRATEGIA_SEO_LANDINGS_B2B_2026-11-12.md). Indexación solicitada para las 2 landings en Search Console. Hallazgo: 0 búsquedas de "opal", "letreros" o "exhibidores"; las empresas buscan "fábrica/empresa/proveedor de acrílicos" y "blanco lechoso" (posición 7-14, CTR 0%). Plan de 7 acciones | Pendiente jefa | Medir 26-nov, 10-dic y 7-ene |
