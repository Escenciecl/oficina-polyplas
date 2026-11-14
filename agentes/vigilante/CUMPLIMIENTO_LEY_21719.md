# Cumplimiento Ley 21.719 — Tablero del Vigilante

**Rige desde:** 1 de diciembre de 2026 · **Diagnóstico inicial:** 13 de noviembre de 2026 (revisión en vivo de polyplas.cl, código del sitio y Tag Manager publicado)
**Estado (13-nov, noche):** 1 de 6 puntos en verde · 4 parciales · 1 sin cumplir

> ⚠️ Este tablero no es asesoría legal. Lo marcado "requiere revisión legal" debe confirmarlo un abogado.

| # | Punto | Estado |
|
## Avance 13-nov-2026 (noche)
**Punto 2 — Cookies: 🟢 publicado y verificado en vivo**
- Aviso nuevo: Rechazar todo / Aceptar todo / Configurar con el mismo peso; 3 categorías; mensaje corto y detalle en "Configurar".
- "Configurar cookies" en el pie de todas las páginas; retirar el consentimiento borra las cookies de esa categoría; la decisión dura 12 meses.
- Registro anónimo de cada decisión en Supabase (tabla `consentimientos`, sin IP ni datos personales).
- Política de privacidad, sección 4 (`#cookies`): tabla con cada cookie, proveedor, finalidad y duración.
- Tag Manager v154: **Google (GA4 y Ads) en modo avanzado** — sin cookies ni datos personales antes de aceptar, solo señales anónimas (verificado `gcs=G100`). **Meta, Hotjar, interceptor de WhatsApp, WEB_APP_URL y guardado de correo/teléfono del checkout bloqueados hasta aceptar** (verificado).
- Ya no tapa "Continuar a cortes".
- → *Requiere revisión legal:* modo avanzado de Google (señales sin cookies antes del consentimiento).

**Punto 5 — Seguridad:** hallazgo del 12-nov resuelto sin pérdida de datos (detalle solo en privado). CRM con usuarios propios de Supabase.

**Medición/Ads:** desde el 13-nov bajan las conversiones observadas en GA4/Ads (Google modela las faltantes en unos días) y Meta mide solo a quien acepta. La cifra oficial de ventas es el CRM.

---|---|---|
| 1 | Consentimiento válido (sin casillas premarcadas, opt-in para marketing) | 🟡 Parcial |
| 2 | Banner de cookies con rechazo real, categorías y bloqueo de scripts | 🟢 Cumple (13-nov) |
| 3 | Política de tratamiento de datos completa y visible | 🟡 Parcial |
| 4 | Canal y proceso ARSOP+ (30 días) | 🔴 No cumple |
| 5 | Seguridad y contratos con proveedores (DPA) | 🟡 Parcial (seguridad de la base de datos resuelta 13-nov; faltan DPA y doble factor) |
| 6 | Protocolo de respuesta ante brechas | 🟡 Parcial (no existe protocolo escrito) |

---

## 1. Consentimiento válido — 🟡 Parcial
**Bien:**
- El checkout no tiene casillas premarcadas. La casilla de Términos (tinas) parte desmarcada.
- No hay casilla de newsletter escondida ni aceptación de publicidad por comprar.

**Falta:**
- **No existe una casilla de opt-in para comunicaciones comerciales.** Hoy no hay forma de que el cliente
  dé su consentimiento para correos de ofertas, y por lo tanto no hay registro de quién aceptó.
- **Campañas de Brevo a clientes que no dieron opt-in explícito** (ej. campaña #29 de reactivación a
  empresas, 13-nov). Desde el 1-dic, enviar marketing sin consentimiento o sin una base legal clara es riesgo.
  → *Requiere revisión legal:* si a clientes empresa que ya compraron se les puede escribir por interés legítimo.
- Al crear cuenta: "Al crear tu cuenta aceptas nuestra política de privacidad" — sirve como aviso, **no** como
  consentimiento para marketing.

**Tareas:**
- [ ] Casilla desmarcada "Quiero recibir ofertas y novedades de Polyplas por correo" en checkout, cuenta y formularios B2B; guardar fecha, texto aceptado y origen.
- [ ] Brevo: separar la lista "con consentimiento" y enviar marketing solo a esa lista. Pausar campañas a contactos sin consentimiento desde el 1-dic (o antes, si el abogado lo indica).
- [ ] Doble confirmación (double opt-in) para el newsletter, recomendado.

## 2. Banner de cookies — 🔴 No cumple
**Bien:**
- Botones "Rechazar todo" y "Aceptar todo" al mismo nivel, con el mismo tamaño.
- Google Analytics y Google Ads parten con el consentimiento en "denegado" (modo de consentimiento de Google).

**No cumple:**
- **Sin categorías**: no se puede aceptar analítica y rechazar publicidad. Falta "Configurar" con necesarias / analíticas / publicitarias.
- **Scripts que cargan aunque el usuario no haya aceptado** (Tag Manager publicado, revisado 13-nov):
  - Meta Pixel (se inicia en todas las páginas).
  - Contentsquare (grabación y mapas de calor).
  - Rastreadores de clics hacia WhatsApp y correo que envían datos a una planilla externa.
  - Guardado de correo y teléfono del checkout en el navegador para conversiones mejoradas de Google Ads.
  - Google Analytics y Google Ads cargan y envían señales sin cookies (modo de consentimiento avanzado).
    → *Requiere revisión legal:* si basta con este modo o hay que bloquearlos por completo hasta aceptar (modo básico).
- **No se puede cambiar la decisión después**: no hay enlace "Configurar cookies" en el footer.
- El botón "Aceptar" tiene color de fondo y "Rechazar" solo borde → igualar el peso visual.

**Tareas:**
- [ ] Banner nuevo con 3 categorías y botones Aceptar / Rechazar / Configurar del mismo peso.
- [ ] En Tag Manager: cada etiqueta con su categoría de consentimiento (Meta y Ads = publicitarias; GA4, Contentsquare, rastreadores de clics = analíticas). No se activan sin consentimiento.
- [ ] Enlace "Configurar cookies" permanente en el footer.
- [ ] Registro anónimo de decisiones (cuántos aceptan / rechazan / ignoran), sin datos personales.

## 3. Política de tratamiento de datos — 🟡 Parcial
**Bien:** existe `/politica-de-privacidad-de-datos/` y está enlazada en el footer. Describe datos de contacto, facturación, B2B y navegación, y los usos principales.

**Falta:**
- Nombrar el **RUT** entre los datos recolectados (se pide en el checkout y en B2B).
- **Plazos de conservación** de cada tipo de dato.
- **Terceros con nombre y para qué**: Transbank (pago), Cloudflare (hosting), Supabase (base de datos / CRM), Brevo y otros proveedores de correo, Google (Analytics, Ads, Tag Manager), Meta, Contentsquare, couriers o transportistas, Google Apps Script/Sheets.
- **Transferencias internacionales** (varios proveedores guardan datos fuera de Chile). → *Requiere revisión legal.*
- **Responsable del tratamiento** con datos de contacto y **canal ARSOP** concreto (hoy dice "canal de atención o correo corporativo").
- Agregar los derechos de **portabilidad** y **bloqueo** (hoy solo acceso, rectificación, eliminación y oposición).
- La sección de cookies dice que se pueden configurar "en cualquier momento", pero hoy solo desde el navegador → alinear con el punto 2.
- Base de licitud de cada uso. → *Requiere revisión legal.*

**Tareas:**
- [ ] Reescribir la política con la estructura anterior (borrador del Vigilante → revisión legal → publicación).

## 4. Derechos ARSOP+ — 🔴 No cumple
**Falta:**
- Correo dedicado (propuesta: **privacidad@polyplas.cl**) visible en la política y el footer.
- Proceso interno: quién recibe, cómo se verifica la identidad, cómo se busca a la persona en el CRM, Supabase, Brevo, Google Sheets y correos, plazo de respuesta (máximo 30 días) y registro de cada solicitud.
- Formulario simple opcional "Ejercer mis derechos".

**Tareas:**
- [ ] Crear el correo y definir quién lo atiende.
- [ ] Procedimiento escrito ARSOP con plantilla de respuesta y registro de solicitudes.

## 5. Seguridad y contratos con proveedores — 🟡 Parcial
**Bien:** sitio con HTTPS; contraseñas de cuentas gestionadas por el proveedor de autenticación; el servidor verifica precios y despacho antes de cobrar.

**Falta:**
- **Hallazgo de seguridad pendiente** (postergado por la jefa el 12-nov, ver `agentes/tatis/PENDIENTES_POSTERGADOS.md`). Detalle solo en privado. **Debe resolverse antes del 1-dic.**
- Revisar los repositorios públicos para que no expongan datos ni configuraciones sensibles.
- Inventario de proveedores que procesan datos de clientes y su acuerdo de tratamiento (DPA):
  Supabase · Cloudflare · Transbank · Google (Analytics, Ads, Workspace, Apps Script) · Meta · Brevo · Contentsquare · proveedor de correo transaccional · courier.
- Control de accesos: quién tiene acceso al CRM, Supabase y Brevo; contraseñas y doble factor.
- Respaldos de la base de datos y prueba de restauración.

**Tareas:**
- [ ] Resolver el hallazgo de seguridad pendiente.
- [ ] Inventario de proveedores + aceptar o descargar el DPA de cada uno (casi todos lo ofrecen en sus términos).
- [ ] Doble factor en todas las cuentas con acceso a datos de clientes.

## 6. Protocolo ante brechas — 🟡 Parcial
**Falta:** protocolo escrito. Debe incluir: cómo se detecta, quién decide, qué se contiene primero, cómo se evalúa el riesgo, plantillas de aviso a la Agencia y a los afectados, plazo de notificación y registro del incidente.
→ *Requiere revisión legal:* plazo exacto que exige la ley (la jefa indica 72 horas como referencia).

**Tareas:**
- [ ] Protocolo de una página + plantillas de aviso + registro de incidentes.

---

## Orden de trabajo propuesto (antes del 1-dic)
1. Hallazgo de seguridad pendiente (punto 5) — es lo de mayor riesgo.
2. Banner con categorías y bloqueo de scripts en Tag Manager (punto 2).
3. Correo privacidad@ y proceso ARSOP (punto 4).
4. Casilla de opt-in y listas de Brevo con consentimiento (punto 1).
5. Política reescrita (punto 3) → revisión legal.
6. Protocolo de brechas e inventario de DPA (puntos 5 y 6).

## Impacto en Google Ads y medición
Bloquear Meta y Google Ads hasta el consentimiento **no reinicia el aprendizaje** (no se tocan acciones de conversión, puja ni campañas), pero **bajará la cantidad de conversiones medidas**. Medición y Ads deben saberlo antes de publicar para no leerlo como caída de ventas. Las ventas reales se siguen midiendo en el CRM.
