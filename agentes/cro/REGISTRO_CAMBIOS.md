# Registro de Cambios — Agente CRO

Cada cambio implementado se registra aquí con fecha, funnel afectado y resultado medido.

| Fecha | Cambio | Funnel | Riesgo | Aprobado por | Resultado 14d | Resultado 28d |
|-------|--------|--------|--------|-------------|--------------|--------------|
| 2026-11-03 | Aviso de opciones de despacho en carrito (RM gratis, regiones, retiro SCL) | add_to_cart → begin_checkout (hoy 73%, 168 abandonos/mes) | Bajo | Natalia | Medir 2026-11-17 | Medir 2026-12-01 |
| 2026-11-05 | Columna "Disponibilidad · ⚡ Retiro hoy" agregada a la tabla comparativa de modelos en /tinas-de-hidromasaje/ | Categoría tinas → ficha individual (bounce 18,7%, 445 visitas/28d) | Bajo | Natalia | Medir 2026-11-19 | Medir 2026-12-03 |
| 2026-11-05 | Botón WhatsApp "Cotizar 2+ unidades con factura" en bloque B2B de /cascos-de-tinas/ | Lead B2B → cotización (ticket ~$175K × 3 unidades) | Bajo | Natalia | Medir 2026-11-19 | Medir 2026-12-03 |
| 2026-11-10 | Auditoría del cotizador de planchas + caída de ventas (sin cambios en el sitio). Ver AUDITORIA_COTIZADOR_2026-11-10.md. 6 propuestas nuevas | Planchas (A) + WhatsApp/mesón | Nulo | Natalia | — | — |
| 2026-11-10 | fix(cotizador): conf_pedido corregido — disparaba en paso 3 en lugar de paso 5 en los 4 módulos (acrílico, PET, PETG, PC). Elimina conversiones GA4 falsas. + ppGuard: alerta en dataLayer si algún elemento crítico del funnel desaparece en un futuro deploy | Funnel planchas completo | Bajo | Natalia | Medir en GA4: conf_pedido debería bajar de volumen (ya no cuenta paso 3) | — |

> Agente activado el 2026-11-03. Paso 0 pendiente: verificar cobertura de eventos en GA4 y comparar compras GA4 vs ventas reales del sistema.
> Medición asignada: Agente Medición mide impacto de los 5 cambios UX checkout (2026-11-06) a 14d (2026-11-20) y 28d (2026-12-04).
| 2026-11-12 | Co-autor del plan de medición B2B (agentes/medicion/PLAN_MEDICION_LANDINGS_B2B_2026-11-12.md): hipótesis E1–E6, métrica principal form_start/sesiones, ~1.470 visitas por variante | Pendiente jefa | — |
| 2026-11-13 | Despacho por zonas en checkout: Zona 1 $19.000 / Zona 2 $30.000, gratis desde $200.000 (antes $350.000), 15 comunas sin despacho, plazo visible AM→PM (exp-012, PR #11) | Paso 3 'Datos y envío' → compra (antes: bajo $350.000 solo retiro) | Medio (cambia el total a pagar; servidor verifica tarifa) | Fredy + Natalia | Medir 2026-11-27 | Medir 2026-12-11 |
| 2026-11-13 | AJUSTE exp-012: despacho pagado $19.000/$30.000 SUSPENDIDO por equipo reducido (renunció quien hacía los fletes). Bajo $200.000 solo retiro; gratis desde $200.000 en Zona 1 y 2 se mantiene. Interruptor para reactivar (PR #12) | Paso 3 'Datos y envío' | Bajo | Natalia | Medir 2026-11-27 | Medir 2026-12-11 |
