# Checklist de funcionamiento — Vigilante

Formato de reporte cuando algo falla: **"No funciona [botón/filtro] en [página]: [qué pasa]."**
Probar en escritorio y celular. Nunca pagar ni enviar formularios reales. GA4/Ads desactivados en la pestaña de prueba. Respaldar y restaurar el carrito.

## A. Todo el sitio (diario, automático)
- [ ] Las páginas del sitemap responden 200 (hoy: 48).
- [ ] Sin enlaces internos rotos.
- [ ] Menú (Planchas, Cúpulas, Baños, Guías, Nosotros, Contacto) y buscador abren y llevan a la página correcta.
- [ ] Botón flotante de WhatsApp / chat abre.
- [ ] Carrito del encabezado abre; "Seguir comprando" e "Ir al pago" funcionan.
- [ ] Footer: enlaces a política de privacidad y términos.

## B. Planchas (acrílico, PET, PETG, policarbonato)
- [ ] Filtros de material, medida, espesor y color filtran y "Limpiar filtros" vuelve a todo.
- [ ] Filtros desde la URL (enlaces de anuncios) se aplican al entrar.
- [ ] "Compra rápida" abre el configurador en cada tarjeta con stock; sin stock muestra "Sin stock".
- [ ] Configurador: medida → espesor → "Continuar a cortes" → Sin cortes / Iguales / Distintos → piezas → plano de corte → "Continuar" y "Agregar al carro y seguir comprando".
- [ ] Botón "Atrás" y la X cierran o vuelven sin perder la selección.

## C. Cotiza por medidas (/acrilico-a-medida/)
- [ ] Piezas: agregar y quitar medidas, error si no cabe.
- [ ] Material, color y espesor; "Ver mis opciones".
- [ ] Opciones: elegir, "Continuar con esta opción", resumen y "Agregar al carro".
- [ ] WhatsApp de ayuda.

## D. Checkout
- [ ] Región → comuna → opciones de entrega correctas según el CRM (pestaña Despachos).
- [ ] Datos persona y empresa, validación de RUT, correo y teléfono.
- [ ] "Continuar al pago" → resumen → Webpay / Transferencia (hasta antes de confirmar).
- [ ] "¿Dudas? WhatsApp" abre con el pedido.

## E. Tinas, cascos, cúpulas, receptáculos, duchas y mamparas
- [ ] Filtros y orden de tinas; botones de cada ficha (comprar, elegir lado, cantidad).
- [ ] Botones de compra de cada ficha de producto.

## F. Landings B2B (POP, letreros, por mayor)
- [ ] Botones "Agendar reunión" llevan al formulario.
- [ ] El formulario valida y arma el mensaje (sin enviarlo).
- [ ] Preguntas frecuentes abren.

## Historial de revisiones
| Fecha | Alcance | Resultado |
|---|---|---|
| 2026-11-13 | A (automático): 48 páginas del sitemap y 49 enlaces internos | ✅ Todo responde. Sin enlaces rotos (la protección de correos de Cloudflare marca 404 sin navegador, pero funciona en el navegador) |
| 2026-11-13 | B, C y D en planchas acrílico y /acrilico-a-medida/ (revisión de medición, en vivo) | ✅ Configurador, cotiza por medidas, carrito y checkout hasta antes de pagar funcionaron. 🟡 La tarjeta "A regiones · flete por pagar en destino" aparece con planchas, que no se envían a regiones |
