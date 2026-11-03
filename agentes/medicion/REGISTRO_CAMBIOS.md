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
