# Revisión UX/UI: landings B2B POP y letreros luminosos — 12 nov 2026

Autor: Agente UX/UI · Páginas: `/acrilico-para-exhibidores-pop/` y `/acrilico-para-letreros-luminosos/`
Método: **revisión heurística** en escritorio (1413 px) y celular (390 px) sobre producción.
Todavía no hay datos de GA4 ni de ContentSquare (las páginas son de hoy). A los 28 días se valida con datos de scroll y exposición del formulario.

## Lo que funciona
- La jerarquía es clara: H1 → dolor → solución → material → ficha → proceso → FAQ → formulario.
- No hay scroll horizontal en celular; las tablas se leen bien a 390 px.
- El formulario valida los campos obligatorios y arma bien el mensaje de WhatsApp.
- Buen contraste: el texto del "costo" (#9a3412 sobre blanco) supera AA.

## Problemas, por prioridad

### P1 — Fricción en el formulario y en el camino hacia él
| # | Problema | Evidencia | Propuesta |
|---|----------|-----------|-----------|
| 1 | **Teléfono y Correo más bajos** que el resto de los campos | 36 px vs 46 px (el tema fija la altura en `tel` y `email`; es el mismo error que tenían los selectores) | Igualar a 46 px |
| 2 | **Las opciones de reunión parecen casillas** (cuadradas): sugieren que se pueden marcar varias | `appearance:none`, `border-radius:3px` | Botones redondos y la opción elegida resaltada en azul |
| 3 | **El formulario está muy abajo** | Celular: empieza al 64% de una página de ~9.000 px (unas 7 pantallas de scroll). Escritorio: un solo botón, arriba | Botón "Agendar reunión" después de los dolores y después de la ficha + **botón fijo abajo en celular** |
| 4 | **Widgets globales que compiten o tapan** | La pestaña roja "Cómo comprar online" contradice el mensaje B2B ("no es compra online") y en celular **tapa el borde derecho de los campos**. El chat verde tapa contenido abajo a la derecha | Ocultar "Cómo comprar online" en estas 2 páginas. Mantener el chat |
| 5 | **No hay confirmación después de enviar** | Se abre WhatsApp y, al volver, la página sigue igual. Si el navegador bloquea la ventana, no hay ningún aviso | Mensaje "Listo, se abrió WhatsApp. ¿No se abrió? Toca aquí" con el enlace directo |

### P2 — Diseño y consistencia
| # | Problema | Propuesta |
|---|----------|-----------|
| 6 | Dolores: 5 tarjetas en una grilla de 2 → la última queda sola, con un hueco | La quinta tarjeta a lo ancho completo |
| 7 | Hero sin imagen: solo texto | Foto real de la bodega o de las planchas (en letreros: opal iluminado). **Requiere fotos de la jefa** |
| 8 | Formulario largo (12 campos, 5 obligatorios) en una sola columna en celular | Agrupar en 3 bloques con subtítulo: "Tu empresa" · "Tu consumo" · "La reunión" |
| 9 | Letreros: un dolor dice "blanco lechoso PA" y el resto de la página dice "opal" | Unificar a "opal" |
| 10 | La cabecera fija ocupa ~170 px en celular (20% de la pantalla) | Es global del sitio, fuera del alcance de estas landings; revisar aparte |

## Medición a 28 días (con CRO)
- Exposición del formulario (% que llega a `#reunion`) por dispositivo.
- Clics en los botones "Agendar reunión" por posición (hero, intermedios, fijo).
- `lead_b2b` / sesiones de la página.
