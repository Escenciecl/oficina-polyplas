# Procedimiento para responder solicitudes de derechos (ARSOP+) — Ley 21.719

**Canal:** formulario https://polyplas.cl/ejercer-mis-derechos/ y correo polyplaschile@gmail.com.
**Plazo legal:** responder en un máximo de **30 días corridos** desde la recepción.

## Cómo llega una solicitud
- Por el formulario: queda guardada en Supabase (tabla `solicitudes_derechos`, con folio `DER-XXXXXX` y fecha límite),
  llega un aviso a polyplaschile@gmail.com y la persona recibe un acuse con su folio.
- Por correo, WhatsApp o teléfono: se registra igual en Supabase (agregar fila) para no perder el plazo.

## Pasos
1. **Revisar el día que llega** y cambiar el estado a `en_proceso`.
2. **Confirmar identidad:** el correo debe coincidir con el de sus compras/chat/cuenta. Si no coincide o pide
   datos sensibles (RUT, direcciones), pedir un respaldo simple por correo (estado `identidad_pendiente`).
3. **Buscar a la persona** (por correo, nombre, RUT y teléfono) en: CRM/Supabase (`conversations`, `messages`,
   `clientes`, `compras`, `b2b_leads`, `consentimientos_ofertas`), Brevo, Google Sheets de seguimiento, Gmail/correos
   de ventas, y WhatsApp.
4. **Responder según el derecho:**
   - *Acceso / portabilidad:* enviar un resumen de los datos (o un archivo CSV) y para qué se usan.
   - *Rectificación:* corregir en todos los sistemas y confirmar.
   - *Supresión:* borrar o anonimizar en todos los sistemas, **salvo** lo que la ley obliga a guardar (boletas/facturas: 6 años) — explicarlo.
   - *Oposición a ofertas:* darlo de baja en Brevo y marcar `retirado_en` en `consentimientos_ofertas`.
   - *Bloqueo:* marcar el registro y no usarlo mientras se revisa.
5. **Responder por correo** desde polyplaschile@gmail.com, citando el folio.
6. **Cerrar en Supabase:** estado `respondida`, `respondida_en`, resumen en `respuesta` y quién la atendió (`responsable`).

## Plantilla de acuse (si llega por correo)
> Hola [nombre]: recibimos tu solicitud de [derecho] el [fecha] (folio [DER-...]). Te responderemos a más
> tardar el [fecha + 30 días]. Si necesitamos confirmar tu identidad, te escribiremos a este correo. — Polyplas
