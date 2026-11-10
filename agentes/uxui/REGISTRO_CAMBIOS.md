# Registro de Cambios — Agente UX/UI

Cada cambio implementado se registra aquí con el archivo modificado, el motivo y el resultado medido.

| Fecha | Cambio | Archivo(s) | Afecta otras páginas | Aprobado por | Resultado 14d | Resultado 28d |
|-------|--------|-----------|----------------------|-------------|--------------|--------------|
| 2026-11-05 | exp-002: Total del carrito visible en header (desktop) | `04-carrito-y-pago.html`, `components/site/Cuenta.tsx`, `app/site.css` | Header en todas las páginas | Natalia | pendiente | pendiente |
| 2026-11-06 | fix(mobile): Precio del carrito oculto en mobile < 960px — `.pp-accion__txt { display:none }` escondía también el `<span>` del precio. Fix: `:has(.pp-accion__total)` lo muestra en naranja cuando hay items | `app/site.css` | Header en todas las páginas | Natalia | pendiente | pendiente |
| 2026-11-06 | fix: Modal checkout con 2+ productos mostraba el nombre del último producto agregado. Ahora eyebrow = "N productos en tu pedido" y título = "Tu pedido" | `04-carrito-y-pago.html` | Modal de checkout | Natalia | pendiente | pendiente |
| 2026-11-06 | fix: Toast de confirmación al agregar plancha extendido de 2.8s a 4s, y ahora incluye el total del pedido ("✓ Plancha agregada · Pedido: $XX.XXX") | `06-compra-planchas-de-acrilico-online-facil.html` | Configurador de planchas | Natalia | pendiente | pendiente |
| 2026-11-06 | fix: Communes excluidas (Pirque, etc.) mostraban doble aviso — banner amarillo Y aviso verde redundante. Se suprime el verde cuando la comuna está excluida | `04-carrito-y-pago.html` | Modal de checkout (sección envío) | Natalia | pendiente | pendiente |
| 2026-11-06 | fix: Texto de factura simplificado — se eliminó "Estos datos son para emitirla." (redundante, el título ya lo explica) | `04-carrito-y-pago.html` | Modal de checkout (sección datos) | Natalia | pendiente | pendiente |

| 2026-11-06 | track: conf_cortes_(iguales/distintos/ninguno) — ppPaso en selectCorteOption + trigger GTM v146 actualizado | `06-compra-planchas-de-acrilico-online-facil.html`, GTM trigger | Configurador de planchas | Natalia | pendiente | pendiente |
| 2026-11-06 | track: conf_elegir_opcion + conf_reco_modo + conf_continuar_recomendada — cajas de selección de plancha ahora se miden en GA4 (GTM v147) | GTM trigger | Configurador de planchas | Natalia | pendiente | pendiente |

> Agente activado el 2026-11-03.
> Regla: ningún cambio al checkout, header o footer sin aprobación explícita. Todo cambio de CSS incluye el bloque de código exacto en la propuesta.
> Medición pendiente: Agente Medición tiene tarea asignada (2026-11-06) para medir impacto de los cambios de checkout a 14 y 28 días.
> Revisión programada 2026-11-13: hipótesis conf_volver alto → cajas de selección de plancha. Medición + UX/UI + Natalia.
