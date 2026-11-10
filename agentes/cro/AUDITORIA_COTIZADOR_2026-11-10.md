# Auditoría del cotizador de planchas y de la caída de ventas — 10 nov 2026

Agente: CRO · Tarea: `cro::1793917050740` · Aprobada por la jefa el 2026-11-10 con alcance ampliado
(revisar también ventas grandes y cierres por WhatsApp).

## Resumen en 4 líneas
1. **La venta web de acrílico no cayó: subió.** Semana del 2 nov: 8 órdenes por $871.442, 46% sobre el promedio semanal de sep–oct ($596.096).
2. **La caída está en el mesón y en WhatsApp**, que no pasan por el cotizador. Mesón semana 2 nov: $3,83M vs $7,06M promedio de octubre (−46%). WhatsApp: $0,32M vs $2,11M (−85%).
3. **No sabemos qué pasa con 9 de cada 10 leads de WhatsApp de acrílico**: 247 de 266 conversaciones desde el 1 sep no tienen resultado registrado. 74% vienen de Google Ads.
4. **El cotizador funciona, pero es frágil y no se pudo medir por paso**: no hay acceso a GA4 desde esta sesión.

Conclusión: arreglar el cotizador no recupera los $2,3M de la caída. Lo que más mueve la meta hoy es **saber qué pasa con los leads de WhatsApp y del mesón**.

---

## 1. Datos (Supabase, proyecto `polyplas chat`)

Fuente: tabla `conversations`. Solo cifras agregadas, sin datos personales.
Semanas de lunes a domingo. Período: 31 ago – 9 nov 2026.

### 1.1 Venta web (Webpay) — solo acrílico

| Semana | Órdenes acrílico | Monto acrílico | Órdenes > $300.000 (todo el sitio) |
|---|---|---|---|
| 31 ago | 5 | $747.445 | 0 |
| 7 sep | 6 | $767.944 | 1 |
| 14 sep | 4 | $454.910 | 0 |
| 21 sep | 8 | $1.403.189 | 1 |
| 28 sep | 3 | $201.824 | 0 |
| 5 oct | 6 | $488.424 | 0 |
| 12 oct | 7 | $693.873 | 1 |
| 19 oct | 3 | $330.939 | 0 |
| 26 oct | 4 | $276.318 | 0 |
| **2 nov** | **8** | **$871.442** | 1 |
| 9 nov (en curso) | 1 | $47.160 | 0 |

Promedio 31 ago – 26 oct: 5,1 órdenes y $596.096 por semana.
La web casi nunca trae ventas grandes: 4 en 10 semanas. Las ventas grandes de acrílico se cierran por mesón y WhatsApp.

### 1.2 Ventas cerradas por canal (todos los productos)

| Semana | Mesón | WhatsApp |
|---|---|---|
| 31 ago | $2.334.569 | $2.272.701 |
| 7 sep | $2.991.049 | $401.335 |
| 14 sep | $3.476.522 | $1.922.882 |
| 21 sep | $4.258.201 | $1.526.294 |
| 28 sep | $4.837.779 | $2.760.468 |
| 5 oct | $3.824.846 | $3.504.861 |
| 12 oct | $6.882.731 | $1.325.184 |
| 19 oct | $10.191.750 | $2.719.766 |
| 26 oct | $7.350.219 | $874.033 |
| **2 nov** | **$3.832.030** | **$323.085** |

Promedio octubre (4 semanas): mesón $7.062.387 y WhatsApp $2.105.961.
Ojo: las ventas de mesón se cargan con ~7 días de atraso (mediana). La semana del 2 nov ya tiene cierres hasta el viernes 6, así que está casi completa. La del 9 nov todavía no tiene mesón cargado.
Limitación: las ventas de mesón no indican producto, así que no se puede separar cuánto de la caída es acrílico.

### 1.3 Leads de WhatsApp que vienen de la página de acrílico

Desde el 1 sep: **266 conversaciones** iniciadas desde `/categoria-producto/planchas-acrilico/` (sin contar órdenes web).
- **19 marcadas como venta cerrada** (7%). Volumen estable: 19 a 32 por semana. No llegan menos leads.
- **247 sin resultado registrado** (93%): no se sabe si compraron en el mesón, si no compraron o si nadie las siguió.
- **198 de 266 (74%) traen `gclid`**: son leads pagados por Google Ads.
- Por intención declarada: "consulta" 189 (14 cerradas), "cotización" 50 (**1 cerrada**), "compra" 15 (2 cerradas), "stock" 6 (2), "precio" 5 (0).
- El campo `cotizacion_enviada` está en falso en las 1.835 conversaciones: no se usa.

Lo más llamativo: **50 personas pidieron cotización desde la página de acrílico y solo 1 quedó registrada como venta.**

### 1.4 Problema de datos encontrado
Las órdenes web están **duplicadas** en `conversations`: 198 filas para 115 órdenes distintas (`webpay_orden`). Cualquier suma de venta web hecha directo sobre esa tabla sale inflada. En este informe se contó cada orden una sola vez.

---

## 2. Recorrido del cotizador (revisión del código publicado en Polyplas-web)

No se pudo recorrer el sitio en vivo ni ver GA4 desde esta sesión. La revisión es sobre el código.

| Pregunta de la ficha | Resultado |
|---|---|
| ¿Cuántos pasos hasta pagar? | 4 + Webpay: 1 Medida y espesor → 2 Cortes → 3 Datos y envío → 4 Resumen y pago. Razonable. |
| ¿Se ve el precio antes del carrito? | Sí. Franja fija abajo con el precio en paso 1 y resumen, también en celular. |
| ¿Se puede comprar sin registrarse? | Sí. No hay inicio de sesión ni creación de cuenta en el pago. |
| ¿Mensajes de error confusos? | Se corrigieron el 6 nov (RUT con autoformato, error de RUT empresa con ejemplo). Sin evidencia de otros. |
| ¿Botón final visible en celular? | Hay reglas específicas para celular y precio del carrito en el header desde el 6 nov. Falta comprobarlo en un teléfono real. |

### Riesgos encontrados
1. **El cotizador está hecho de parches sobre parches.** El archivo tiene 12.530 líneas, 7 observadores que corrigen lo que hace otro código, 61 temporizadores y 654 reglas `!important`. Conviven dos numeraciones de pasos ("Paso 1 de 4" en el asistente nuevo y un stepper antiguo de 5 pasos con material/medida/espesor/color/agregar). Cada cambio nuevo tiene riesgo de romper otro. En 7 días hubo más de 10 arreglos al flujo.
2. **Posible error de medición en `conf_pedido`:** la documentación dice que se dispara al llegar al paso "Pedido", pero en el stepper antiguo se dispara desde el paso 3 ("Elige el espesor"). Se repite igual en PET, PETG y policarbonato. Hay que verificar con `?pp_debug=1` cuál de los dos flujos ve el cliente hoy.
3. **Después de pagar con retiro en tienda**, se le pide al cliente coordinar el retiro enviando el comprobante por WhatsApp. Es un paso extra post-venta (no afecta la conversión, sí la experiencia).

### Qué no se pudo revisar
- **Embudo por paso en GA4** (cuánta gente pasa de medida → cortes → datos → pago). Los 12 eventos existen. Falta acceso a GA4 para leerlos.
- Comparación antes/después de los cambios del 6 y 9 nov: requiere GA4.

---

## 3. Propuestas que salen de esta auditoría

Ordenadas por (impacto × confianza) / (esfuerzo × riesgo). Cada una entra a la bandeja para aprobación.

### P1 — Registrar el resultado de cada lead de WhatsApp (Medición + quien atiende el chat)
- **Qué:** al cerrar cada conversación, marcar `venta_cerrada` (sí/no), monto y, si no compró, el motivo (precio, stock, plazo, no respondió).
- **Por qué:** 93% de los leads de acrílico no tiene resultado. 74% los paga Google Ads. Sin esto no se puede saber por qué cayó WhatsApp ni subir las ventas offline a Ads (pendiente desde el 9 nov).
- **Impacto:** no vende por sí solo, pero es lo que permite explicar la caída y entrenar mejor a Ads. Esfuerzo bajo (proceso), riesgo nulo.

### P2 — Seguir las 50 solicitudes de cotización de acrílico sin cierre (CRO + atención)
- **Qué:** revisar las cotizaciones pedidas desde la página de acrílico en las últimas 4 semanas y recontactar las que no tienen respuesta ni venta.
- **Por qué:** 50 pidieron cotización y solo 1 figura como venta.
- **Impacto estimado** (supuestos a la vista; ticket WhatsApp promedio 31 ago – 1 nov = $17.307.524 / 56 ventas ≈ $309.000):
  - Conservador: 2 ventas recuperadas ≈ $618.000
  - Esperado: 4 ventas ≈ $1.236.000
  - Optimista: 8 ventas ≈ $2.472.000
- Esfuerzo: 2–3 horas. Riesgo: bajo (contactar a quien pidió cotización).

### P3 — Embudo por paso del cotizador en GA4 (Medición)
- **Qué:** sacar en GA4 el embudo conf_medida → conf_espesor → conf_ir_pago → begin_checkout → purchase, antes y después del 6 y del 9 nov, separado por celular y escritorio.
- **Requisito:** acceso a GA4. Por decisión de la jefa (10 nov) no se conectan herramientas externas: el embudo se saca desde GA4 en el navegador de la jefa, o la jefa exporta el informe y lo comparte.
- **Por qué:** es la parte de la auditoría original que quedó sin datos.

### P4 — Verificar el evento `conf_pedido` en las 4 líneas de planchas (UX/UI + Medición)
- **Qué:** con `?pp_debug=1`, confirmar en qué paso se dispara hoy. Si se dispara al elegir espesor, corregirlo para que se dispare en "Pedido".
- Esfuerzo: 30 min. Riesgo: bajo.

### P5 — Ordenar la deuda técnica del cotizador antes de más arreglos (UX/UI)
- **Qué:** inventariar los parches (observadores, temporizadores, `!important`), sacar el stepper antiguo si ya no se usa y dejar una sola numeración de pasos.
- **Por qué:** cada arreglo nuevo arriesga romper otro paso del flujo que hoy vende bien.
- Esfuerzo: alto (varios días). Riesgo: medio, requiere pruebas en celular y escritorio antes de publicar. Prioridad: después de P1–P4.

### P6 — Limpiar las órdenes web duplicadas en Supabase (Medición)
- **Qué:** encontrar por qué cada orden Webpay se guarda dos veces (una con `sku`, otra con `module` y planos de corte) y dejar una sola.
- **Por qué:** cualquier reporte de venta web hecho sobre esa tabla sale inflado.
- Esfuerzo: 1 hora de diagnóstico. Requiere aprobación antes de tocar la base de datos.

---

## 4. Pregunta abierta para la jefa
La caída más grande es del **mesón** (−46% vs octubre), y ahí no hay datos de producto. ¿Hubo algo distinto esa semana (feriado, menos personal, quiebre de stock de PA 5–6 mm)? Esa respuesta sirve más que cualquier dato del sitio.
