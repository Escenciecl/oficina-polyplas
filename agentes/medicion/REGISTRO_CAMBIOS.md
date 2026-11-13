# Registro de Cambios — Agente Medición

Cada fix implementado se registra aquí con el tag/evento afectado y cómo se verificó.

| Fecha | Fix | Archivo/Tag GTM | Evento afectado | Aprobado por | Verificado con | Resultado |
|-------|-----|----------------|----------------|-------------|---------------|-----------|

> Agente activado el 2026-11-03.
>
> Bugs conocidos pendientes de diagnóstico (Paso 0):
> 1. Evento `purchase` llega a GA4 con `value = $0` en filas individuales aunque el total acumulado muestra ingresos reales.
> 2. Compras por transferencia probablemente no disparan el evento `purchase` → subestima conversiones en todos los canales.
> 3. `click_asistencia_flotante` no lleva parámetro de producto de origen → Ads no puede atribuir el chat a una keyword.
>
> Para iniciar el Paso 0 necesito: acceso a GTM (o captura del contenedor exportado) + vista GA4 DebugView en una sesión de compra de prueba.
| 2026-11-12 | Plan de medición y experimentación de landings B2B (con CRO): 15 eventos b2b_*, embudo de formulario campo a campo, lead_id para cerrar el ciclo hasta la venta, 6 experimentos priorizados. NO usa generate_lead (conversión principal de Ads) | Pendiente jefa | — |
| 2026-11-12 | Medición B2B publicada (PR #6): 15 eventos b2b_* + lead_id + tabla b2b_leads (solo inserción). Pendiente: GTM y GA4 (pasos en el plan, sección 9) y lead_b2b como conversión secundaria en Ads | ✅ Sitio · ⏳ GTM/GA4 | Línea base 6 semanas (hasta 2026-12-24) |
| 2026-11-12 | GTM publicado y GA4 configurado (12 dimensiones, 2 métricas; cupo 47/50). Eventos b2b_* llegando en Tiempo real. Pendiente: marcar lead_b2b como evento clave con el primer lead real, y después importarlo a Ads como secundaria | ✅ | — |
| 2026-11-13 | DETECTADO (sin corregir): con el despacho por zonas, el valor de purchase incluye el despacho y la línea DESPACHO llega como artículo (nombre distinto por comuna). Afecta GA4 en carrito, página de gracias y servidor. Propuesta: value solo productos + parámetro shipping + shipping_tier por zona | 04-carrito-y-pago.html · 30-gracias · webpay-return.js · transferencia-confirmar.js | purchase, add_shipping_info | Pendiente jefa | Revisión de código | — |
| 2026-11-13 | FIX en PR #12: purchase con value solo productos + shipping aparte, sin DESPACHO en artículos (carrito, gracias, servidor Webpay y transferencia); shipping_tier por zona (despacho_z1/z2/gratis). OJO: informes que filtraban shipping_tier='despacho' deben usar los nuevos valores desde la publicación | 04-carrito-y-pago.html · 30-gracias · webpay-return.js · transferencia-confirmar.js · webpay-init.js · transferencia-init.js | purchase, add_shipping_info, add_payment_info, pedido_transferencia | Jefa (pendiente merge) | Pruebas unitarias + prueba real TR-73549525 como caso | Pendiente |
| 2026-11-13 | AUDITORÍA de marcaje planchas (/categoria-producto/planchas-acrilico/ y /acrilico-a-medida/): recorrido en vivo con pp_debug + GTM publicado + GA4 (1–13 nov). Embudo principal OK. Hallazgos: GA4 registra 12 compras vs 21 ventas reales (Supabase: 18 Webpay + 3 transferencias), causa probable consentimiento por defecto 'denied'; /acrilico-a-medida/ sin view_item; conf_plano_listo 8,5 por usuario (GTM HTML); 6 eventos sin etiqueta GTM (whatsapp_comprobante, planchas_filtro_url y 4 de calculadora antigua); item_id distinto vista vs carro; 13 dimensiones MonsterInsights sin uso ocupan cupo (47/50) | GTM · GA4 · pp-track · 14-planchas-a-medida | varios | Pendiente jefa | Prueba en vivo + GA4 + Supabase | Pendiente |
