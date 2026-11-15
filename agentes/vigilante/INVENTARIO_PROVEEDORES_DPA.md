# Inventario de proveedores que tratan datos de clientes (Ley 21.719)

Para cada proveedor hay que **aceptar o descargar su acuerdo de tratamiento de datos (DPA)** y guardar
una copia (PDF) en la carpeta privada de Polyplas (no en este repositorio). Casi todos lo ofrecen dentro de
sus términos o en la configuración de la cuenta. Aceptar estos acuerdos lo hace la jefa con su cuenta.

| Proveedor | Para qué | Datos | Ubicación | DPA (dónde) | Estado | Doble factor |
|---|---|---|---|---|---|---|
| Supabase | Base de datos: pedidos, chat, cuentas, formularios | Contacto, RUT, direcciones, compras | Brasil (sa-east-1) | supabase.com/legal/dpa (se firma en el panel) | ⬜ Pendiente | ⬜ |
| Cloudflare | Hosting del sitio y funciones de pago | Datos en tránsito, registros técnicos | Global | Incluido en los términos (cloudflare.com/cloudflare-customer-dpa) | ⬜ Pendiente | ⬜ |
| Transbank (Webpay) | Pagos con tarjeta | Datos de pago (no los vemos) | Chile | Contrato de comercio Webpay | ⬜ Revisar contrato | ⬜ |
| Brevo | Correos de pedidos y de ofertas | Correo, nombre, historial de envíos | UE (Francia) | Incluido en términos (brevo.com/legal/termsofuse — Anexo DPA) | ⬜ Pendiente | ⬜ |
| Google (Analytics, Ads, Tag Manager) | Medición y anuncios | Identificadores de navegación; correo/teléfono cifrados al comprar (si acepta) | EE. UU. y otros | Aceptar "Términos de protección de datos" en Analytics y Ads (Administrar > Configuración de la cuenta) | ⬜ Pendiente | ⬜ |
| Google (Gmail, Sheets, Apps Script) | Correo polyplaschile@ y planillas de seguimiento | Contacto, mensajes | EE. UU. y otros | Cuenta personal de Gmail: evaluar pasar a Google Workspace (tiene DPA) | ⬜ Evaluar | ⬜ |
| Meta (Píxel) | Medición y anuncios (solo con consentimiento) | Identificadores de navegación | EE. UU. y otros | Términos de herramientas comerciales de Meta (Business Manager) | ⬜ Pendiente | ⬜ |
| Contentsquare / Hotjar | Mapas de calor (solo con consentimiento) | Navegación | UE | DPA en el panel de Contentsquare | ⬜ Pendiente | ⬜ |
| Hosting de correo polyplas.cl (cPanel) | Correos ventas@ y contacto@ | Mensajes de clientes | Por confirmar | Términos del proveedor de hosting | ⬜ Confirmar proveedor | ⬜ |
| GitHub | Código del sitio y CRM (sin datos de clientes) | Ninguno de clientes | EE. UU. | No aplica (verificar que no se suban datos) | ✅ No aplica | ⬜ |
| Transportistas / couriers | Entregas | Nombre, teléfono, dirección | Chile | Acuerdo simple de confidencialidad | ⬜ Pendiente | — |

## Control de accesos (revisar cada 3 meses)
- Usuarios del CRM (tabla `equipo` en Supabase): Natalia (jefa), contacto@polyplas.cl. Quitar a quien deje la empresa el mismo día.
- Activar **doble factor** en: Supabase, Cloudflare, Google (polyplaschile@gmail.com y cuentas de Ads/Analytics), Brevo, GitHub, Meta Business, cPanel.
- Activar en Supabase *Leaked password protection* (Authentication > Settings).
- Respaldos de la base de datos: Supabase hace respaldos diarios en planes pagados; en plan gratuito, exportar mensualmente (pendiente definir).
