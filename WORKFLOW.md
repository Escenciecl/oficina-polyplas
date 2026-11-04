# Workflow de la Oficina Polyplas

Cómo funciona el equipo de agentes, cómo aprobar cambios y cómo pedir reportes.

---

## Regla de oro
**Ningún agente puede tocar el sitio sin tu aprobación explícita.**
Proponen → tú revisas → tú apruebas → se ejecuta.

---

## Cómo aprobar un cambio

1. Ves una propuesta en la **Bandeja del jefe** (la oficina 3D)
2. Vienes a Claude Code y dices: `"aprobé [propuesta] del agente [X]"`
3. Te muestro el diff exacto del archivo que cambia
4. Dices `"dale al sitio"`
5. Se sube a producción y queda registrado en `REGISTRO_CAMBIOS.md` del agente

Cada cambio viaja en su propia rama (`agente/nombre-del-cambio`) antes de llegar a `main`.

---

## Cadencia de reportes

### Diario — Reunión de cierre
Di **`"reunión de cierre"`** al terminar tu jornada.

Responden los tres agentes de seguimiento diario:

| Agente | Qué reporta |
|--------|-------------|
| **Vigilante** | ¿El sitio está funcionando? Alertas del día |
| **SEO** | Qué hice hoy para aumentar conversiones web orgánicas |
| **Ads** | Ritmo de gasto vs presupuesto, alertas de campaña |

Formato: 3 líneas por agente. Máximo 5 minutos.

**Tatis documenta cada reunión de cierre** en Confluence bajo "📋 Reuniones y Reportes" — crea la página `Cierre YYYY-MM-DD` dentro de la misma sesión.

### Semanal — Lunes
Di **`"reporte semanal"`** el lunes al inicio de la jornada.

Responden los tres agentes de análisis semanal:

| Agente | Qué reporta |
|--------|-------------|
| **CRO** | Funnel de la semana: tasa de cada etapa, caídas, alertas |
| **UX/UI** | Bugs activos, estado de cambios en curso |
| **Intel** | Movimientos de competencia: precios, catálogo, promociones |

Puedes pedir el reporte de un agente específico: `"reporte semanal CRO"`.

### Mensual — Primer lunes del mes
Di **`"reporte mensual"`**.

Responden todos los agentes activos con:
- Resultados del mes (lo que funcionó y lo que no)
- Top 3 propuestas para el mes siguiente
- Una métrica que mejoró y una que no

---

## Cómo alimentar a los agentes con datos frescos

Los agentes no acceden solos a GA4, GSC o Google Ads — tú les traes los datos:

| Dato | Cómo entregarlo |
|------|----------------|
| GA4 | Screenshot de la vista que corresponde |
| Google Search Console | Screenshot del panel de rendimiento |
| Google Ads | Screenshot del resumen de campaña |
| Competencia | El agente Intel hace búsqueda web directamente |

Sin datos frescos los agentes reportan sobre lo que saben (análisis anterior).
Con datos frescos el reporte es real y accionable.

---

## Cómo acercarte a un agente en la oficina

En la escena 3D, cuando te acercas a un agente aparece su nombre y en qué está trabajando ahora.
Si quieres hablar con él directamente: ven a Claude Code y di `"hablar con [nombre del agente]"`.

---

## Registro de todo lo aprobado

Cada cambio al sitio queda en:
- `agentes/[agente]/REGISTRO_CAMBIOS.md` — qué se cambió, cuándo y qué resultó
- El historial de git en `Polyplas-web` — el diff exacto, la rama y el commit

---

## Agentes activos (nov 2026)

| Agente | Estado | Reporte |
|--------|--------|---------|
| Vigilante | Real | Diario |
| SEO | Real | Diario + Semanal |
| CRO | Real | Semanal |
| Ads | Real | Diario |
| UX/UI | Real | Semanal |
| Intel | Real | Semanal |
| Medición | Real | Semanal + después de cada cambio al sitio |
| Tatis | Real | Diario (documentación) |

---

## Confluence — documentación del equipo

Espacio: **Proyecto Marketing & Producto (PMP)**
URL base: https://moralesgarcianat.atlassian.net/wiki/spaces/PMP/folder/40206337

| Sección | ID | Para qué |
|---------|-----|---------|
| 📋 Reuniones y Reportes | 40271873 | Cierre diario + reportes semanales |
| 🤖 Historial por Agente | 40304641 | CV de cada agente: propuestas, hallazgos, logros |
| ✅ Cambios Implementados | 40337409 | Tabla viva de cambios con resultados a 14 y 28 días |
| 📊 KPIs y Evolución | 40337431 | Panel mensual con línea base nov 2026 |

**Tatis** mantiene estas páginas actualizadas. Para revisar avances, ve directamente a Confluence.

---

## Memoria entre sesiones (Confluence → oficina)

La oficina recuerda lo aprobado gracias a `memoria.json` (en este repo), que es una copia de lo que Tatis documenta en Confluence.

**Al abrir la oficina:** se hace una reunión de inicio. Los agentes van a la sala y aparece la minuta de la sesión anterior: qué se aprobó y publicó, qué se trabajó y qué quedó pendiente. Las propuestas ya decididas no vuelven a la bandeja.

**Al iniciar una sesión con Claude:** di **`"sincroniza la oficina"`**. Claude:
1. Lee el último `Cierre YYYY-MM-DD` y `✅ Cambios Implementados` en Confluence.
2. Si pegas el texto del botón **Copiar para sincronizar** de la minuta, registra esas decisiones en Confluence.
3. Actualiza `memoria.json`: `sesionAnterior` (minuta) y `propuestas` (`aprobada`, `rechazada` o `hecha`).
4. Agrega a `index.html` las propuestas nuevas de los agentes.

**Al cerrar la sesión ("reunión de cierre"):** Tatis crea el `Cierre YYYY-MM-DD` en Confluence y Claude deja esa minuta en `memoria.json` para la próxima vez.
