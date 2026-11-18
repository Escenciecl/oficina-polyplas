# Embudo de compra de planchas: celular vs computador — 18 nov 2026

Agente: Medición (para el plan SEO de compras web, acción A) · Cierra la propuesta P3 `medicion::1794318971909` sin export de la jefa (lectura directa de GA4).
Fuente: GA4 > Eventos, 21 oct – 17 nov 2026 (28 días), todo el tráfico, comparación "Tráfico en dispositivos móviles" vs "Tráfico web" (computador). Cifras = usuarios que hicieron el evento.

| Paso (evento) | Celular | Computador |
|---|---:|---:|
| Usuarios (session_start) | 1.322 | 387 |
| Ve la plancha (view_item) | 618 | 118 |
| Elige espesor (conf_espesor) | 416 | 28* |
| Elige medida (conf_medida) | 308 | 21* |
| Arma el pedido (conf_pedido) | 255 | 95 |
| Agrega al carro (add_to_cart) | 116 | 49 |
| Abre el pago (begin_checkout) | 104 | 48 |
| Datos y envío OK (pago_datos_ok) | 30 | 26 |
| Elige pago (add_payment_info) | 17 | 23 |
| **Compra (purchase)** | **8** | **14** |

*En computador el configurador usa otro flujo (conf_tarjeta_medida), por eso espesor/medida salen bajos.

## Paso a paso (% que pasa al siguiente)

| Tramo | Celular | Computador |
|---|---:|---:|
| Ve la plancha → arma el pedido | 41 % | 80 % |
| Pedido → carro | 45 % | 52 % |
| Carro → abre el pago | 90 % | 98 % |
| **Abre el pago → datos y envío OK** | **29 %** | **54 %** |
| **Datos OK → compra** | **27 %** | **54 %** |
| Total usuarios → compra | 0,6 % | 3,6 % |

## Lectura
1. El celular trae el 77 % de los usuarios pero solo 8 de 22 compras. Convierte ~6 veces menos que el computador.
2. Las dos fugas propias del celular están en el **pago**: llenar datos y envío (29 % vs 54 %) y del dato OK a pagar (27 % vs 54 %). La tercera está en el **configurador** (41 % vs 80 %).
3. Del carro al pago no hay problema (90 %).

## Cuidados
- El computador puede incluir pruebas internas (mucho evento por usuario: 480 conf_pedido de 95 usuarios). Las tasas del computador son un techo optimista.
- GA4 no cuenta compras de quienes rechazan cookies (afecta a ambos).
- El 13-nov cambió la entrega (bajo $200.000 solo retiro): parte de la fuga en "datos y envío" puede ser gente que quería despacho (pago_entrega_vista: 13 usuarios en celular).
- Muestra chica para orgánico solo; esto es todo el tráfico.

## Impacto si el celular cierra la mitad de la brecha en los dos tramos del pago
29 % → 41 % y 27 % → 40 %: compras en celular 8 → ~17 cada 28 días (+~2 por semana, ~+$200.000/semana con ticket $98.000, todos los canales).
