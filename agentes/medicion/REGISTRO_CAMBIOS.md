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
