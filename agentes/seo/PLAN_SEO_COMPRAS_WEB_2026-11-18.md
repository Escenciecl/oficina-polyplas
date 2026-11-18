# Plan SEO: compras web orgánicas de planchas de acrílico

Autor: Agente SEO · 18 nov 2026 · Encargo de la jefa: "agente SEO, encárgate del plan"
Meta de largo plazo: **$1.000.000 por semana en compras web que llegan desde Google orgánico, solo planchas de acrílico, estable** (promedio de 4 semanas).
Esta meta es solo de compras web. La meta del ROL ($3,6M nov → $5,5M feb) incluye ventas cerradas por contacto y se mantiene aparte.

---

## 1. Punto de partida (datos al 17-nov)

| Dato | Valor | Fuente |
|---|---|---|
| Compras web orgánicas (todos los productos) | 2 · 2 · 0 · 0 · 5 · 3 por semana (5-oct a 15-nov) → ~2/semana | GA4, Organic Search, evento purchase |
| Ingresos orgánicos | ~$138.000/semana (6 semanas) | GA4 |
| Tasa de compra orgánica | 1,3 % (Ads: 0,7 %) | GA4, 25-ago a 17-nov |
| Ticket orgánico | ~$98.000 | GA4 ($2,16M / 22 compras) |
| Búsquedas con "acrílico" | 17,2 mil impr. y 227 clics en 13 semanas · pos 10,2 · CTR 1,3 % | Search Console |
| Categoría planchas | ~2.000 impr./semana · pos 8,2 · CTR 1,8 % | Search Console 4-16 nov |
| Búsquedas largas (espesor, color, precio, medida) | 268 búsquedas · ~125 impr./semana · CTR 3,8 % | Search Console |
| Fichas de producto gratis (Merchant Center) | 153 productos aprobados · 272 clics de producto en 28 días · acrílico al menos 107 de esos | Merchant Center |

Notas de medición:
- GA4 pierde compras cuando el cliente rechaza cookies (16-nov: 1 compra orgánica real no contada). Desde el 16-nov se cuenta con `metadata.atribucion.canal` en `pedidos_web` (Supabase), por número de pedido.
- Con ~2 compras/semana un solo pedido mueve todo: se mira siempre el promedio de 4 semanas.

## 2. La fórmula

Ingresos SEO = visitas de búsquedas de acrílico × % de compra × ticket.
Solo subiendo posiciones no se llega: aunque estuviéramos top 3 en todo lo que hoy aparece, serían ~150-250 visitas/semana. Hay que mover las tres palancas.

## 3. Acciones e impacto (por semana)

Cálculo: clics extra = impresiones × (CTR objetivo − CTR actual); compras = clics × 1,3 %; ingreso = compras × $98.000. CTR objetivo según la curva del propio sitio (pos 2-4 ≈ 8-9 % en cúpulas).

| # | Qué | Conservador | Esperado | Optimista | Esfuerzo | Confianza |
|---|---|---:|---:|---:|---|---|
| 1 | "Planchas de acrílico" al top 3-5 (categoría dueña única) | $56.000 | $107.000 | $184.000 | 3-4 días + autoridad | Media |
| 2 | Compra orgánica 1,3 % → 2 % (celular, precio y entrega arriba, confianza) | $40.000 | $75.000 | $110.000 | 1-2 semanas con CRO/UX | Media |
| 3 | Fichas de producto en Google (Merchant Center) | $25.000 | $64.000 | $127.000 | 1 día diagnóstico + 2-3 días | Baja |
| 4 | Ticket $98.000 → $128.000 (volumen, plancha grande, cortes) | $30.000 | $60.000 | $90.000 | 1 semana con CRO | Media |
| 5 | Páginas por espesor y color (2-3, 4-6, 8-10 mm; blanco lechoso; espejo) | $15.000 | $37.000 | $70.000 | 1 día por página | Media |
| 6 | /acrilico-transparente/ dueña de "acrílico transparente" | $11.000 | $20.000 | $34.000 | 1-2 días | Media |
| 7 | Autoridad: +20 reseñas Maps, 5-10 enlaces buenos | sostiene 1, 5, 6 | | | continuo | Alta (largo plazo) |

Combinado (las palancas se multiplican): **conservador ~$350.000 · esperado ~$670.000 · optimista ~$1.240.000 por semana.**
Dependencia fuera de SEO: bajo $200.000 solo hay retiro. Reactivar el despacho pagado (decisión jefa) es probablemente la mayor mejora de conversión.

## 4. Metas por etapa

| Etapa | Ingresos SEO acrílico/semana (prom. 4 sem.) | Señal |
|---|---:|---|
| Feb 2027 | $300.000 | Top 5 en "planchas de acrílico" y "acrílico transparente"; compra orgánica ≥ 2 % |
| Jun 2027 | $600.000 | Páginas por espesor/color en top 5; fichas de producto con compras medidas |
| Dic 2027 | $1.000.000 | ~10 compras/semana estables 3 meses |

## 5. Calendario 90 días

| Cuándo | Qué |
|---|---|
| 18-24 nov | Diagnóstico Merchant Center (hecho 18-nov, ver §6). Propuesta categoría fase 1 (ver §7). |
| 24 nov | Revisión /acrilico-transparente/ → decidir página dueña de cada búsqueda. |
| Sem. 2-3 | Categoría fase 1 publicada. Primera página por espesor. Pedido de reseñas a cada comprador. |
| 2 dic | Revisión a 28 días de exp-002 → recién ahí se puede tocar el title de la categoría (fase 2). |
| Diciembre | Conversión y ticket en celular (con CRO y UX/UI). 2 páginas más por espesor/color. |
| Lunes | Seguimiento en el Panel Polyplas: compras orgánicas por número de pedido, clics y posición de 10 búsquedas fijas. |

Búsquedas fijas a seguir: planchas de acrilico · plancha de acrílico · acrilico transparente · plancha acrilica transparente · lamina de acrilico · venta de planchas de acrilico · acrilico 3mm · acrilico blanco lechoso · acrilico espejo · acrilico a medida.

## 6. Diagnóstico Merchant Center (18-nov)

- Cuenta activa, **153 productos aprobados**, 0 rechazados, 0 en anuncios (todo el tráfico es gratuito/orgánico).
- Últimos 28 días: **272 clics de producto (-52 %)**, 15,6 mil impresiones (-57,5 %), CTR 1,7 %. La caída viene de receptáculos (90×90 -186, 80×80 -120, esquinero -83), **no de acrílico**.
- Acrílico en el top de productos: transparente 4 mm 2,40×1,20 AA (41, nuevo), blanco lechoso 8 mm 2,40×1,80 (21), transparente 2 mm 1,80×1,20 AA (16), blanco lechoso 8 mm 2,40×1,20 (15), transparente 2 mm 1,87×1,27 PA (14). **Las fichas ya traen ~25-30 clics/semana de acrílico: tanto como la categoría.**
- Problemas:
  1. **Sin fuente de conversión**: GA4 no está vinculado a Merchant Center → no vemos qué fichas venden.
  2. ~~104 clics con categoría "Desconocido"~~ → revisado: vienen de los 3 productos que Google encontró solo en el sitio, no del feed.
  3. ~~48 láminas sin descripción~~ → revisado: el feed de acrílico (Google Sheet `polyplas_merchant_center`, 138 planchas) tiene categoría, tipo AA/PA, descripciones de ~410 caracteres, precio, stock y enlace a la variante. No requiere cambios.
  4. Merchant Center pide crear una llave de acceso para tareas clave (vincular, cambiar URL). Eso lo hace la jefa.
- Competidores que aparecen junto a nuestras fichas: novoacril.cl (25 %), tiendamicrogeo.cl (23 %), abingraf.cl (13 %).

## 7. Auditoría de la categoría /categoria-producto/planchas-acrilico/ (18-nov)

| Punto | Estado |
|---|---|
| Title | "Planchas de Acrílico a Medida · Transparente, Colores y Espejo \| Polyplas" (73 caracteres; Google corta ~60). **No se toca hasta el 2-dic** (exp-002 en medición). |
| H1 | "Planchas de Acrílico Transparente y de Colores" → compite con /acrilico-transparente/ por "transparente". |
| Módulos duplicados | `_estructura.html` incluye **dos veces** `08-lo-que-dicen-nuestros-clientes.html` y `09-guia-de-compra-atencion-y-politicas.html` → testimonios, FAQ y datos estructurados repetidos (2 Product con aggregateRating, IDs HTML repetidos). |
| Módulo 07 | `_estructura.html` llama a `07-caracteristicas-tecnicas-de-nuestras-pla.html`, que fue borrado a propósito (el armado lo ignora). Sin problema. |
| FAQ (datos estructurados) | "Contamos **with** stock" (error de tipeo). "1 corte gratuito de adaptación… cortes adicionales 10 %": misma duda pendiente con la jefa que en /acrilico-transparente/ (la regla es iguales gratis, distintas +10 %). No se toca sin la jefa. |
| Enlaces a /acrilico-transparente/ | 1 solo, en el módulo 075. |
| Indexación | index, follow · canonical propio · OK |

## 8. Registro

Propuestas en la bandeja (tasks/queue.json): categoría fase 1 y Merchant Center fase 1. Nada se publica sin aprobación.

## 9. Avance

- 18-nov: jefa aprueba las dos propuestas. Categoría fase 1 → PR #42 (Polyplas-web), build OK, pendiente de merge por la jefa. Merchant Center → feed revisado y en buen estado; pendiente la llave de acceso y el vínculo GA4 (jefa).
