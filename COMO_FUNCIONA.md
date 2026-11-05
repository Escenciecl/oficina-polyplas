# Cómo funciona el sistema de agentes Polyplas

Guía completa: qué es cada parte, cómo se toman decisiones y cómo se publican cambios en el sitio.

---

## 1. Los dos repositorios

El sistema vive en dos repositorios de GitHub separados:

| Repositorio | URL | Para qué sirve |
|-------------|-----|----------------|
| `oficina-polyplas` | https://escenciecl.github.io/oficina-polyplas/ | La interfaz 3D donde ves a los agentes trabajar |
| `Polyplas-web` | https://github.com/Escenciecl/Polyplas-web | El código real del sitio polyplas.cl |

Cuando un agente propone un cambio y tú lo apruebas, **el cambio va a Polyplas-web** — no a la oficina. La oficina es solo la interfaz de gestión.

---

## 2. La oficina 3D — qué puedes hacer ahí

**Acceso:** https://escenciecl.github.io/oficina-polyplas/

### Lo que puedes hacer en la oficina:
- **Moverte** con flechas, WASD o clic en el piso
- **Acercarte a un agente** para ver su nombre y en qué está trabajando hoy
- **Revisar propuestas** en la **Bandeja del Jefe** (panel derecho)
- **Aprobar o rechazar** propuestas con un clic
- **Ver el historial** de cambios ya aplicados (botón "Ver qué cambió →")
- **Subir de piso** con el botón del elevador (segundo piso: PMs de producto)

### Lo que NO pasa automáticamente en la oficina:
Los agentes NO publican cambios solos cuando tú apruebas. La aprobación en la oficina **solo registra tu decisión en queue.json**. Los cambios en el sitio se ejecutan manualmente en Claude Code (ver sección 4).

---

## 3. Los agentes — quién hace qué

### Piso 1 — Equipo de marketing y datos

| Agente | Rol | Qué propone |
|--------|-----|-------------|
| **Vigilante** | Monitor del sitio | Alertas si algo falla en polyplas.cl |
| **SEO** | Posicionamiento web | Titles, metas, fichas técnicas, contenido que rankea |
| **CRO** | Conversión | Cambios para que más visitas se conviertan en ventas |
| **Ads** | Google Ads | Términos negativos, ajuste de campañas, copies de anuncio |
| **UX/UI** | Experiencia de usuario | Mejoras de diseño y usabilidad del sitio |
| **Intel** | Competencia | Análisis de precios y propuestas de valor vs competidores |
| **Medición** | Analytics | Revisión de GA4, eventos de conversión, alertas de datos |
| **Tatis** | Documentación | Registra todo en Confluence, crea minutas de cierre |

### Piso 2 — PMs de producto (estrategia de categoría)

| Agente | Especialidad |
|--------|-------------|
| **PM Planchas** | Acrílico AA/PA, PET, PETG, Policarbonato, Corte a medida |
| **PM Social** | Estrategia Instagram @polyplaschile |
| **PM Baños** | Tinas de hidromasaje, Cascos, Complementos |
| **PM Cúpulas** | Cúpulas de acrílico, iluminación cenital |

Los PMs de producto **no ejecutan cambios solos** — entregan insumos al equipo de piso 1 (ej: PM Baños le da a SEO los ganchos de venta de cada modelo de tina).

---

## 4. El flujo completo — de propuesta a publicación

```
Agente propone → tú apruebas en la oficina → vienes a Claude Code → se ejecuta → se publica
```

### Paso a paso:

**Paso 1 — La propuesta aparece en la oficina**
Los agentes presentan propuestas en la Bandeja del Jefe (panel derecho de la oficina 3D). Cada propuesta dice qué va a cambiar y por qué.

**Paso 2 — Tú apruebas o rechazas**
Con un clic en la oficina. Esto graba tu decisión en `tasks/queue.json` con estado `"pendiente"`.

**Paso 3 — Vienes a Claude Code**
Aquí (en este chat) dices: `"ejecuta lo aprobado"` o `"ejecuta [nombre de la tarea]"`.

**Paso 4 — Claude lee queue.json y ejecuta**
Claude Code lee el archivo de cola, ve qué está aprobado y pendiente, hace los cambios en los archivos del sitio, y sube todo a GitHub.

**Paso 5 — El sitio se actualiza**
Polyplas-web está conectado a Vercel/despliegue automático. Unos minutos después del push, el cambio está en polyplas.cl.

**Paso 6 — La tarea se marca como completada**
queue.json se actualiza con estado `"completada"` y queda visible en el historial de la oficina ("Ver qué cambió →").

---

## 5. Cómo comunicarte con los agentes

### Desde la oficina 3D
Los agentes tienen respuestas pre-programadas. Útil para ver en qué están trabajando o aprobar propuestas, pero las respuestas no son IA real.

### Desde Claude Code (este chat) — recomendado para feedback real
Dile a Claude: `"hablar con [nombre del agente]"` y Claude responde desde el rol de ese agente, usando su ROL.md como base.

Ejemplos:
- `"hablar con PM Baños — qué propones para la ficha de la Tina Kuyen?"` → responde como PM Baños con estrategia de venta
- `"hablar con SEO — revisa el título de la página de cúpulas"` → responde como SEO con análisis y propuesta
- `"hablar con CRO — hay un problema de fricción en el cotizador"` → responde como CRO con soluciones concretas

Cuando el feedback de la conversación cambia algo importante del rol (ej: una regla de negocio que el agente no sabía), dile a Claude: `"actualiza el ROL.md de [agente]"` y queda guardado permanentemente.

---

## 6. Estructura de archivos del sistema

### En `oficina-polyplas/`
```
oficina-polyplas/
├── index.html              — La oficina 3D completa (HTML + Three.js)
├── WORKFLOW.md             — Reglas de flujo y cadencia de reportes
├── COMO_FUNCIONA.md        — Esta guía
├── memoria.json            — Contexto de sesión anterior para los agentes
├── tasks/
│   └── queue.json          — Cola de propuestas (pendiente / completada)
└── agentes/
    ├── seo/
    │   ├── ROL.md          — Quién es el agente, qué sabe, qué reglas sigue
    │   └── REGISTRO_CAMBIOS.md — Historial de cambios que hizo este agente
    ├── cro/
    ├── ads/
    ├── intel/
    ├── medicion/
    ├── tatis/
    ├── uxui/
    ├── copy/               — PM Baños
    ├── soporte/            — PM Cúpulas
    ├── email/              — PM Planchas
    └── social/             — PM Social
```

### En `Polyplas-web/`
```
Polyplas-web/
├── content/modulos/        — Módulos HTML de cada página del sitio
│   ├── 10-tinas/           — Página categoría tinas
│   ├── 40-producto-tina-*/
│   │   └── _pagina.json    — SEO: titulo, descripcion, og tags, schema.org
│   ├── 05-planchas-pet/
│   └── 06-planchas-petg/
├── app/site.css            — CSS global del sitio
└── components/site/        — Componentes React reutilizables
```

---

## 7. queue.json — la cola de trabajo

Vive en `oficina-polyplas/tasks/queue.json`. Cada tarea tiene esta estructura:

```json
{
  "id": "cro-001",
  "agente": "CRO",
  "titulo": "Agregar tabla comparativa en página de tinas",
  "descripcion": "Qué hace el cambio y por qué",
  "estado": "pendiente",    ← puede ser: pendiente / completada / rechazada
  "antes": "Sin tabla",
  "despues": "Tabla con 5 modelos y precios"
}
```

**Cómo ver qué está pendiente:**
Dile a Claude: `"qué está aprobado y pendiente de ejecutar"` — Claude lee queue.json y te da la lista.

---

## 8. Cómo mejorar el sistema

### Corregir información de un agente
Si un agente tiene un dato incorrecto (ej: precio equivocado, regla de negocio que cambió):
1. Dile a Claude: `"el agente PM Baños tiene mal el plazo de entrega de tinas — son 3 a 5 días hábiles"`
2. Claude actualiza el `ROL.md` del agente y lo pushea

### Crear un nuevo agente
1. Dile a Claude: `"crea un nuevo agente [nombre] con este rol: [descripción]"`
2. Claude crea la carpeta en `agentes/`, el `ROL.md`, el `REGISTRO_CAMBIOS.md`, y actualiza `index.html` y `WORKFLOW.md`
3. El agente aparece en la oficina 3D en el próximo reload

### Reemplazar un agente existente
Exactamente lo mismo que crear uno nuevo, indicando cuál se reemplaza (ej: "reemplaza al agente Email con este nuevo PM de Planchas").

### Agregar una propuesta al queue manualmente
Si tienes una idea que quieres ejecutar sin pasar por la oficina:
Dile a Claude: `"agrega al queue esta tarea: [descripción del cambio que quieres]"` y Claude la agrega directamente.

---

## 9. Reglas técnicas que debes conocer

### Push al repositorio
Los pushes se hacen siempre con:
```
git push --verbose https://github.com/Escenciecl/[repo].git main
```
El flag `--verbose` evita un error intermitente del servidor (`commit_refs_rules`). No uses `git push origin main` a secas.

### Conflictos en queue.json
Si la oficina 3D también actualizó queue.json mientras Claude trabajaba, puede haber conflicto. Claude lo resuelve automáticamente con rebase. No tienes que hacer nada.

### ¿Cuándo se publican los cambios en el sitio?
Polyplas-web se despliega automáticamente cada vez que Claude hace push. El cambio tarda 1 a 3 minutos en aparecer en polyplas.cl.

---

## 10. Resumen rápido para el día a día

| Qué quieres hacer | Cómo hacerlo |
|-------------------|-------------|
| Ver propuestas de agentes | Abrir la oficina 3D → Bandeja del Jefe |
| Aprobar un cambio | Clic en "Aprobar" en la oficina 3D |
| Ejecutar lo aprobado | Venir a Claude Code → `"ejecuta lo aprobado"` |
| Ver qué cambió en el sitio | Oficina 3D → "Ver qué cambió →" |
| Hablar con un agente | Claude Code → `"hablar con [agente]"` |
| Corregir un dato del agente | Claude Code → `"actualiza ROL.md de [agente]: [corrección]"` |
| Crear o reemplazar un agente | Claude Code → `"crea agente [nombre] con rol: [descripción]"` |
| Ver tareas pendientes | Claude Code → `"qué está pendiente de ejecutar"` |
