# Pendientes postergados — Tatis

Lista de temas que la jefa decidió **dejar para después**. Tatis los recuerda en el cierre semanal
y los saca de la lista solo cuando la jefa los retome o los descarte.

| Fecha | Tema | Por qué se postergó | Retomar |
|-------|------|---------------------|---------|
| 2026-11-12 | **Seguridad de la base de datos (Supabase):** revisar los permisos de las tablas del chat/CRM y del stock y preparar un plan para protegerlas **sin romper el chat ni el CRM**. El detalle técnico está en la sesión con Claude del 12-nov (no se escribe aquí porque este repositorio es público). | Hoy no es prioridad (jefa, 12-nov) | Cuando la jefa lo indique. Recordar en cada cierre semanal |
| 2026-11-12 | **Seguridad de los repositorios de GitHub:** revisar qué información queda pública (por ejemplo, este repositorio de la oficina tiene cifras de venta) y qué conviene dejar privado. | Hoy no es prioridad (jefa, 12-nov) | Cuando la jefa lo indique. Recordar en cada cierre semanal |
| 2026-11-12 | **`lead_b2b` como evento clave en GA4** (solo GA4). **No se importa a Google Ads**: agregar acciones de conversión está prohibido por la regla de aprendizaje, y nada se toca en Ads sin autorización explícita de la jefa | GA4 solo permite marcarlo cuando llegue el primer lead real de las landings B2B | Apenas llegue el primer lead B2B |
| 2026-11-12 | **Fotos reales para las landings B2B** (bodega, planchas, blanco lechoso iluminado). Hoy usan las imágenes de pallets del catálogo | Esperando fotos de la jefa | Cuando la jefa las envíe |
| 2026-11-12 | **Reseñas de empresas clientes en Google Maps** y **registro en ChileProveedores** (requiere crear la cuenta: lo hace la jefa) | Lo debe hacer la jefa | Próximas 2 semanas |
| 2026-11-12 | **Revisar la descripción de Google Maps:** dice "fundada en 1996"; el sitio dice "desde 1997" | Dato a confirmar por la jefa | Cuando la jefa lo confirme |
| 2026-11-13 | **Prueba automática diaria del Vigilante:** revisa páginas, enlaces, filtros, "Compra rápida", el configurador hasta el checkout, cotiza por medidas, tinas, cúpulas, landings B2B y WhatsApp, en escritorio y celular. Falta: terminar la primera corrida completa (se detuvo a los 10 minutos), corregir lo que salga, programarla a diario a las 8:00 con aviso de "No funciona X" y abrir el PR. Está en el computador de la jefa, rama `vigilante-pruebas` (aún no subida a GitHub). Hallazgo ya confirmado: en la primera visita el aviso de cookies tapa el botón "Continuar a cortes" del configurador hasta que el cliente acepta o rechaza; se resuelve con el nuevo aviso de cookies (Ley 21.719) | La jefa la deja pendiente (13-nov) | Cuando la jefa lo indique. Recordar en cada cierre semanal |

- **Reactivar el despacho pagado** ($19.000 Zona 1 / $30.000 Zona 2) cuando llegue la tercera persona del equipo de despacho. Suspendido el 13-nov-2026 por la jefa. Cómo (una vez publicados los PR #14 de Polyplas-web y #1 del CRM): **CRM → pestaña Despachos → prender Zona 1 y/o Zona 2**. Después: pedido de prueba en cada zona, aviso a ventas y experimento nuevo. (El PR #13 se cerró: ya no hace falta.)

- **Ley 21.719 (rige el 1-dic-2026):** el Vigilante está a cargo del cumplimiento de los 6 puntos (tablero en `agentes/vigilante/CUMPLIMIENTO_LEY_21719.md`). OJO: el hallazgo de seguridad postergado el 12-nov ahora tiene plazo: debe resolverse antes del 1-dic.
