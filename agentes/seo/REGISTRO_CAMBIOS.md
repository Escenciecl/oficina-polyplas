# Registro de Cambios — Agente SEO

Cada cambio implementado se registra aquí con fecha, URL afectada y resultado medido a 14/28/56 días.

| Fecha | Cambio | URLs afectadas | Riesgo | Aprobado por | Resultado 14d | Resultado 28d | Resultado 56d |
|-------|--------|---------------|--------|-------------|--------------|--------------|--------------|
| 2026-11-03 | Optimizar title + meta description | /categoria-producto/tinas-de-hidromasaje/ | Medio | Jefe | — | — | — |
| 2026-11-04/05 | Optimizar title + meta description (exp-002) | /categoria-producto/planchas-acrilico/ | Bajo | Jefa | revisar 2026-11-18 | — | — |

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
