# Mapa de dolores B2B — 11 nov 2026

Autor: Agente B2B · Fuente: pedidos web de empresas en Supabase (27-may al 11-nov-2026)
Estado: **hipótesis**. Ningún dolor está validado todavía con una conversación real con la empresa.
La lista con nombres de empresas está en Confluence (privada), no en este repositorio público.

---

## 1. Lo que dicen los datos

| Dato | Valor |
|------|-------|
| Empresas que compraron en la web | **66** (71 pedidos) |
| Venta a empresas | **$8.053.487** (ticket promedio por empresa: $122.022) |
| Empresas que volvieron a comprar otro día | **4 de 66 (6%)** |
| Empresas que pidieron corte a medida | 43 de 66 (65%) |
| Empresas fuera de la RM | 6 |

**El dolor nuestro, primero:** 94% de las empresas compra una vez y no vuelve. No tenemos
cuentas, tenemos compras sueltas. Nadie las llama después de la compra.

**Señal más fuerte:** 2 de cada 3 empresas compran con corte. El corte a medida es lo que las
trae: no quieren cortar ellas.

**Brecha de medición:** las conversaciones de WhatsApp no registran si el contacto es empresa
(`client_company` está vacío en todas). No sabemos cuántas empresas preguntan y no compran.
→ Pedir a Medición y al CRM un campo "empresa" en cada lead.

---

## 2. Dolores por segmento

| Segmento | Empresas | Venta | Con corte | Dolor probable | Cómo lo resuelve Polyplas | Oferta para empezar |
|----------|---------:|------:|----------:|----------------|---------------------------|---------------------|
| Construcción e instalaciones (constructoras, terminaciones, aislación, hojalatería, maestranza) | 13 | $2.040.437 | 9 | Material que llega tarde a obra; cortar en terreno; factura y despacho | Stock en Santiago, piezas cortadas listas para instalar, despacho gratis en Santiago desde $200.000 (desde 13-nov; bajo ese monto, retiro), factura a empresa | Primer pedido de obra con piezas cortadas + contacto directo para la próxima obra |
| Comercio, retail y online (tiendas, botillerías, farmacias, ventas por internet) | 20 | $1.930.045 | 10 | Exhibidores, separadores y vitrinas que se repiten en cada local | Mismas medidas cortadas cada vez; precios publicados; un solo proveedor para acrílico y PETG | "Tu medida guardada": repetir el pedido con las mismas piezas cuando abran otro local |
| Diseño, interiorismo y mueblería | 7 | $1.322.079 | 4 | Proyectos con plazos cortos; necesitan calidad pareja y asesoría de material | Línea PA 100% virgen para terminaciones; asesoría técnica de PM Planchas; cotización inmediata en la web | Ficha técnica AA vs PA para su estudio + pedido piloto del próximo proyecto |
| Gastronomía y servicios (restaurantes, bares, salud, transporte, educación) | 11 | $1.307.640 | 10 | Separadores, protecciones y señalética a medida, una vez y rápido | Corte a medida gratis si las piezas son iguales; retiro inmediato | Menor potencial de recompra: atender bien, no priorizar en prospección |
| Publicidad, letreros, eventos e insumos gráficos | 7 | $863.726 | 4 | **Compran seguido** (2 de las 4 empresas que repitieron están aquí); necesitan stock de colores y espesores | Importador directo, colores AA (flúor, espejo, negro) y PA; stock inmediato | **Prioridad 1**: llamarlas para ser su proveedor habitual de planchas |
| Industria y empresas productivas (envases, aeronáutica, ingeniería, refrigeración, I+D) | 8 | $589.560 | 6 | Repuestos y protecciones técnicas; continuidad de abastecimiento; PETG y policarbonato | Policarbonato compacto y PETG en stock; asesoría técnica | Visita o llamada técnica con PM Planchas: qué compran hoy y a quién |

Segmentos asignados por el giro que la empresa declaró al comprar. Es una aproximación.

---

## 3. Prioridad de trabajo (primeras 2 semanas)

1. **Reactivar a las empresas que ya compraron** (más fácil y barato que captar nuevas):
   - Prioridad 1: publicidad, letreros e insumos gráficos (ya repiten).
   - Prioridad 2: construcción e instalaciones (mayor venta total).
   - Prioridad 3: diseño e interiorismo (mayor ticket por empresa: $188.868).
2. **Validar dolores**: 10 llamadas cortas a empresas que compraron (guion abajo). Cada respuesta
   se registra en `REGISTRO_CAMBIOS.md` y se comparte con PM Planchas.
3. **Propuesta al sitio** (con CRO, UX/UI y SEO): página "Proveedor de planchas para empresas"
   con cotización por volumen. Solo después de validar los dolores.

---

## 4. Guion de llamada (borrador, requiere aprobación de la jefa)

> Hola, le hablo de Polyplas. Ustedes nos compraron [producto] en [mes]. Quería saber cómo les
> fue con el material y hacerle 3 preguntas cortas:
> 1. ¿Para qué lo usaron y cada cuánto necesitan planchas?
> 2. ¿A quién le compran normalmente y qué es lo que más les complica con ese proveedor?
> 3. ¿Les serviría recibir las piezas ya cortadas a su medida para la próxima compra?
>
> Si hay interés: ofrecer una cotización del próximo pedido con las mismas medidas.

No se promete precio especial, descuento ni plazo sin aprobación de la jefa y sin confirmar
stock con PM Planchas.

---

## 5. Validación con PM Planchas (pendiente)

- [ ] Stock para abastecer pedidos repetidos de colores AA (letreros y publicidad).
- [ ] Ficha técnica AA vs PA para estudios de diseño.
- [ ] Policarbonato compacto y PETG: espesores con stock para industria.
- [ ] Capacidad de corte para pedidos grandes (piezas por día).
