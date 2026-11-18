# Recorrido del configurador de planchas en celular — 18 nov 2026

Agentes: UX/UI + CRO. Lo levantó la jefa: el flujo no deja llevar más de una plancha completa y se puede quedar bloqueado.
Se recorrió en celular, en la vista previa de `main` (cro-exp013-orden-facturacion.polyplas-web.pages.dev), sin pagar.
Dato de contexto (GA4, 21-oct a 17-nov): en celular solo el 41 % de quienes ven la plancha arma el pedido (80 % en computador).

## Hallazgos

| # | Qué pasa | Por qué | Gravedad |
|---|---|---|---|
| 1 | **"Sin cortes" no deja elegir cuántas planchas.** Hay que volver con "Atrás" hasta el carrito o usar "Agregar al carro y seguir comprando". | El selector "CANTIDAD DE PLANCHAS" existe (`#ppCorteSinCorteContent`), pero está oculto con CSS: "la cantidad se elige en el Resumen". Ese Resumen ya no aparece, porque "Continuar" va directo a "Datos y envío". Pasa lo mismo en acrílico, PET, PETG y policarbonato. | Alta: frena las compras de varias planchas (ticket) |
| 2 | **"Iguales" o "Distintos" + "Continuar" sin piezas = no pasa nada.** No hay mensaje y la persona queda bloqueada. | La validación no muestra error, y en celular los campos de Ancho/Alto/Cantidad quedan bajo la barra inferior fija (y=359 con pantalla de 562). | Alta: bloqueo silencioso |
| 3 | **El carrito muestra la tarjeta "A regiones · flete por pagar en destino" con planchas.** | La tarjeta sale siempre, pero las planchas no van a regiones. | Media: promete algo que no hay |
| 4 | **El paso 1 tiene un botón "Atrás"** sin paso anterior. | — | Baja |

## Propuesta
Ver `uxui::1795040000000` en la bandeja.

## Compromiso de UX/UI y CRO
Recorrer el flujo completo en celular y computador cada lunes (planchas, cúpulas, tinas: configurador, carrito y pago, sin pagar) y traer los hallazgos a la bandeja, sin esperar a que la jefa los encuentre.
