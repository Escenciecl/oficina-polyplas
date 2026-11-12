# Plan de medición y experimentación: landings B2B

Autores: Agente de Medición + Agente CRO · 12 nov 2026 · Estado: **propuesta, pendiente de aprobación de la jefa**
Páginas: `/acrilico-para-exhibidores-pop/` (landing `pop`) y `/acrilico-para-letreros-luminosos/` (landing `letreros`)

---

## 1. Preguntas que esta medición tiene que responder

| # | Pregunta | Para decidir… |
|---|----------|---------------|
| 1 | ¿Quién llega? (fuente, búsqueda, dispositivo, landing) | En qué canal y en qué palabras invertir |
| 2 | ¿Hasta dónde lee y qué secciones ve? | Qué mover arriba, qué cortar |
| 3 | ¿Qué botón lleva al formulario? (hero, intermedios, fijo) | Dónde poner el llamado |
| 4 | ¿Dónde se abandona el formulario? (campo por campo) | Qué campos sacar o simplificar |
| 5 | ¿Cuántos envían el formulario y **cuántos mandan de verdad el WhatsApp**? | Si el paso por WhatsApp pierde leads |
| 6 | ¿Cuántos leads terminan en reunión → cotización → primer pedido → cuenta recurrente? | El retorno real hacia la meta de 2 cuentas de $5M |

Las preguntas 1 a 5 se responden en GA4. La 6 necesita cerrar el ciclo fuera de GA4 (sección 4).

---

## 2. Reglas (no negociables)

1. **No usar `generate_lead`.** Es conversión principal de Google Ads; usarlo cambiaría lo que optimiza la campaña y puede reiniciar el aprendizaje.
   Todo lo B2B usa eventos con prefijo `b2b_` y la conversión propia `lead_b2b`, que ya existe.
2. **Nunca enviar datos personales a GA4** (nombre, empresa, RUT, teléfono, correo, texto del comentario): lo prohíben las políticas de Google.
   Solo se envían categorías (industria, rango de consumo, tipo de reunión) y si un campo se llenó (sí/no).
3. **Consentimiento:** si la persona rechaza las cookies, GA4 no registra nada. Los números de GA4 van a ser **menores** que los leads reales; por eso el ciclo cerrado de la sección 4 es la fuente de verdad.
4. **`lead_b2b` en Google Ads, solo como conversión secundaria** (observación). Así no afecta las pujas ni el aprendizaje. Se decide con el Agente Ads.

---

## 3. Eventos

**Parámetros que llevan todos los eventos `b2b_*`:**
`landing` (`pop` | `letreros`) · `variante` (`control` o el nombre de la variante de un experimento) · `lead_id` (solo desde que se empieza el formulario; ver sección 4).

### 3.1 Página y lectura

| Evento | Cuándo se dispara | Parámetros propios | Responde |
|--------|-------------------|--------------------|----------|
| `b2b_landing_view` | Al cargar la página | `referrer_tipo` (orgánico, Ads, directo, interno, otro) | P1 |
| `b2b_scroll` | Al llegar al 25, 50, 75 y 90% de la página, una vez cada uno | `profundidad` | P2 |
| `b2b_section_view` | Cuando una sección está al menos 50% visible durante 1 segundo (una vez por sección) | `seccion` (hero, dolores, cta_dolores, material, ficha, cta_ficha, proceso, faq, formulario), `orden` (1–9) | P2: es la "tasa de exposición" de cada zona |
| `b2b_faq_open` | Al abrir una pregunta frecuente | `pregunta` (texto corto fijo) | P2: qué dudas tienen |
| `b2b_link_click` | Clic en un enlace interno (la otra landing, guías) | `destino` | P2 |

### 3.2 Llamados a la acción

| Evento | Cuándo | Parámetros | Responde |
|--------|--------|------------|----------|
| `b2b_cta_click` | Clic en cualquier botón "Agendar reunión" | `cta_posicion` (hero, post_dolores, post_ficha, fijo_movil) | P3 |
| `click_asistencia_flotante` | Ya existe (chat global) | — (se segmenta por página) | Si el chat compite con el formulario |

### 3.3 Formulario (el embudo fino)

| Evento | Cuándo | Parámetros | Responde |
|--------|--------|------------|----------|
| `b2b_form_view` | El formulario está 50% visible durante 1 s | `llego_por` (scroll, cta_hero, cta_dolores, cta_ficha, cta_fijo) | P3 |
| `b2b_form_start` | Primer foco en cualquier campo | `primer_campo` | P4 |
| `b2b_field_done` | Al salir de un campo **con** contenido (una vez por campo) | `campo` (nombre técnico), `campo_orden`, `bloque` (empresa, consumo, reunion) | P4: dónde se detienen |
| `b2b_form_error` | Clic en enviar con obligatorios vacíos | `campos_faltantes` (lista de nombres técnicos), `intento` (1, 2, 3…) | P4 |
| `lead_b2b` *(ya existe, se amplía)* | Envío válido | `industria`, `consumo`, `tipo_reunion` (ya están) + `fabrica`, `opcionales_llenos` (0–6), `con_comentario` (sí/no), `segundos_formulario`, `intentos`, `cta_origen` | P5, P6 |
| `b2b_whatsapp_bloqueado` | El navegador bloqueó la ventana de WhatsApp | — | P5 |
| `b2b_whatsapp_reintento` | Clic en "¿No se abrió? Toca aquí" | — | P5 |
| `b2b_form_abandon` | La persona sale de la página después de empezar el formulario y sin enviarlo | `ultimo_campo`, `campos_llenos`, `segundos_formulario` | P4 |

**El embudo que se arma en GA4 (Exploraciones → Embudo), por landing y por dispositivo:**
`b2b_landing_view` → `b2b_section_view (dolores)` → `b2b_form_view` → `b2b_form_start` → `b2b_field_done (consumo)` → `lead_b2b`

---

## 4. Cerrar el ciclo: del formulario a la cuenta de $5M

GA4 llega hasta el envío del formulario; no sabe si la persona apretó "enviar" en WhatsApp ni si compró después.

**Propuesta:**
1. Cada formulario genera un **código de lead** corto (ej. `B2B-7K3Q`) que va en el mensaje de WhatsApp **y** en el evento `lead_b2b`.
2. La jefa registra cada lead que llega en una tabla del CRM (Supabase), con estas columnas:

| lead_id | fecha | landing | industria | consumo | ¿llegó el WhatsApp? | reunión agendada | reunión hecha | cotización ($) | primer pedido ($) | 2ª compra en 90 días | motivo de pérdida |
|---------|-------|---------|-----------|---------|---------------------|------------------|---------------|----------------|-------------------|----------------------|-------------------|

3. Con el `lead_id` se cruza la tabla con GA4: se sabe **qué fuente, qué landing y qué variante** trajo cada reunión y cada venta.

**Recomendación de CRO (decisión de la jefa):** además de abrir WhatsApp, guardar el formulario en Supabase al enviarlo. Hoy, si la persona no aprieta "enviar" en WhatsApp, el lead se pierde sin rastro.
Requiere actualizar la política de privacidad, porque se guardarían datos de contacto.

---

## 5. Configuración en GA4 y GTM (la hace Medición)

1. **GTM:** una sola etiqueta "GA4 – Eventos B2B" con un activador para todo evento que empiece con `b2b_` más `lead_b2b`, que reenvíe los parámetros.
2. **GA4 → Dimensiones personalizadas** (alcance evento): `landing`, `variante`, `seccion`, `cta_posicion`, `campo`, `bloque`, `industria`, `consumo`, `tipo_reunion`, `fabrica`, `llego_por`, `lead_id`, `campos_faltantes`, `ultimo_campo`. Son 14 de las 50 disponibles.
   Métricas personalizadas: `segundos_formulario`, `opcionales_llenos`.
3. **Evento clave en GA4:** `lead_b2b`. En Google Ads, solo como **secundaria**.
4. **Control de calidad:** probar con `?pp_debug=1`, revisar en "DebugView" de GA4 que cada evento llegue una sola vez y sin datos personales, en escritorio y en celular.

---

## 6. Plan de experimentos (después de la línea base)

**Realidad del tráfico:** las páginas son nuevas y el SEO tarda de 2 a 4 meses. Con poco tráfico, una prueba A/B que mida leads finales no alcanza significancia.
Ejemplo: si la tasa de inicio del formulario es 5% y queremos detectar una mejora a 7,5% (+50%), con 95% de confianza y 80% de potencia se necesitan **~1.470 visitas por variante**.

**Por eso:**
- **Semanas 1–6:** solo medir. Sin experimentos. Se construye la línea base por landing y por dispositivo.
- **Métrica principal de los experimentos:** `b2b_form_start` / sesiones (sucede mucho más que el lead). Métrica de control: `lead_b2b` / sesiones (que no baje).
- **Método:** reparto aleatorio 50/50 en el navegador, guardado para que la misma persona vea siempre la misma versión, con el parámetro `variante` en todos los eventos. Mínimo 28 días por prueba.
- **Hasta tener ~1.500 visitas por variante:** se compara antes y después, usando la otra landing como grupo de control, y el resultado se informa como "no concluyente" si no alcanza los umbrales.

**Lista de hipótesis (CRO), en orden de prioridad:**

| # | Hipótesis | Cambio | Métrica principal |
|---|-----------|--------|-------------------|
| E1 | Pedir menos compromiso trae más leads | "Agenda una reunión con muestras" vs **"Pide la ficha técnica y los certificados"** (y en la llamada se agenda la reunión) | `lead_b2b` / sesiones |
| E2 | Un formulario más corto se completa más | 12 campos vs **5 obligatorios + "lo demás lo conversamos por WhatsApp"** | `lead_b2b` / `b2b_form_start` |
| E3 | Una foto real da confianza | Hero solo con texto vs **foto de la bodega o de las planchas** | `b2b_cta_click (hero)` / sesiones |
| E4 | El formulario arriba capta al que ya sabe lo que quiere | Formulario solo al final vs **formulario corto en el hero** | `b2b_form_start` / sesiones |
| E5 | El dolor más urgente debe ir primero | Orden actual vs **"Peak de temporada" como primer dolor** en POP (noviembre–diciembre) | `b2b_section_view (cta_dolores)` y `b2b_cta_click` |
| E6 | El texto del botón fijo en celular | "Agendar reunión con muestras" vs **"Ver muestras en mi taller"** | `b2b_cta_click (fijo_movil)` |

---

## 7. Reporte

- **Semanal (Medición):** sesiones, embudo por landing y dispositivo, leads, errores del formulario (campos que más faltan), WhatsApp bloqueado.
- **Mensual (CRO + B2B):** leads → reuniones → cotizaciones → pedidos con `lead_id`, avance hacia las 2 cuentas de $5M y estado de los experimentos.

## 8. Implementación

| Paso | Quién | Esfuerzo |
|------|-------|----------|
| Código de eventos en las 2 landings (un módulo compartido) | Claude | 2–3 h |
| Código de lead en el mensaje de WhatsApp | Claude | 30 min |
| Etiqueta y activador en GTM, dimensiones en GA4 | Medición (necesita acceso a GTM y GA4) | 1 h |
| Tabla de seguimiento de leads en Supabase | Claude + jefa | 1 h |
| Guardar el formulario en Supabase (opcional) | Claude, si la jefa aprueba | 2 h + política de privacidad |
| Control de calidad en DebugView | Medición | 1 h |

**Decisiones de la jefa:** (1) aprobar el plan · (2) ¿guardar el formulario en Supabase? · (3) ¿`lead_b2b` como conversión secundaria en Google Ads?
