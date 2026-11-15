# Protocolo ante brechas de datos personales — Polyplas (Ley 21.719)

> Documento operativo. No es asesoría legal: el plazo exacto de aviso y el formato del reporte a la
> Agencia deben confirmarse con un abogado y con las instrucciones que publique la Agencia.

## 1. Qué es una brecha
Cualquier incidente que provoque **destrucción, pérdida, alteración, acceso o divulgación no autorizada**
de datos personales. Ejemplos: alguien ve conversaciones o pedidos de otros clientes; se pierde un
computador o celular con planillas de clientes; se envía un correo masivo con los destinatarios a la vista;
una contraseña del CRM, Supabase, Brevo o Google se filtra; un proveedor nos avisa de un incidente.

## 2. Quién hace qué
| Rol | Persona | Qué hace |
|---|---|---|
| Responsable de la respuesta | Natalia (jefa) | Decide, autoriza avisos y comunica |
| Apoyo técnico | Claude / agentes (Vigilante) | Contiene, investiga y documenta |
| Contacto de privacidad | polyplaschile@gmail.com | Recibe reportes internos y externos |

Cualquier persona del equipo que sospeche una brecha **avisa de inmediato** a la jefa (WhatsApp y correo).
No se espera a "estar seguros".

## 3. Pasos (los primeros 72 horas)
1. **Detectar y registrar (hora 0):** anotar en el registro (sección 6) qué se vio, cuándo y quién lo detectó.
2. **Contener (primeras horas):**
   - Cambiar contraseñas y cerrar sesiones de las cuentas afectadas (CRM/Supabase, Brevo, Google, Cloudflare, cPanel, GitHub).
   - Revocar o rotar llaves (Supabase *secret key*, Brevo API key, Transbank) si pudieron quedar expuestas.
   - Quitar permisos abiertos o publicaciones que expongan datos; si hace falta, pausar el chat o el formulario afectado.
3. **Evaluar el riesgo (24 h):** qué datos (contacto, RUT, direcciones, compras), cuántas personas, si hay
   riesgo para ellas (fraude, suplantación, spam dirigido) y si los datos ya fueron usados.
4. **Avisar a la Agencia de Protección de Datos Personales** cuando la brecha pueda afectar a las personas,
   **sin demora indebida** (referencia interna: dentro de 72 horas desde que se supo; confirmar plazo legal).
   Usar la plantilla A.
5. **Avisar a las personas afectadas** cuando el riesgo sea relevante (por ejemplo, datos de pago, RUT con
   dirección, o datos que permitan fraudes), en lenguaje claro. Usar la plantilla B.
6. **Corregir la causa y verificar** que no vuelva a pasar; dejar todo en el registro.
7. **Revisión posterior (dentro de 14 días):** qué falló, qué se cambió, quién lo revisa.

## 4. Plantilla A — Aviso a la Agencia (borrador)
- Responsable: Polyplas Ltda, RUT [RUT], Santiago Concha 1525, Santiago. Contacto: polyplaschile@gmail.com.
- Fecha y hora del incidente y de su detección:
- Descripción de lo ocurrido:
- Datos y número aproximado de personas afectadas:
- Posibles consecuencias para las personas:
- Medidas adoptadas para contener y mitigar:
- Medidas para evitar que se repita:
- ¿Se avisó a las personas afectadas? ¿Cuándo y cómo?:

## 5. Plantilla B — Aviso a las personas afectadas (borrador)
> Asunto: Aviso importante sobre tus datos en Polyplas
>
> Hola [nombre]: el [fecha] detectamos [qué pasó, en simple]. Esto pudo afectar tus datos de [tipo de datos].
> Ya [medidas tomadas]. Te recomendamos [acciones concretas: desconfiar de correos que pidan pagos, cambiar
> tu contraseña de Mi cuenta, etc.]. Lamentamos lo ocurrido. Si tienes dudas, escríbenos a
> polyplaschile@gmail.com o ejerce tus derechos en https://polyplas.cl/ejercer-mis-derechos/.

## 6. Registro de incidentes
| Fecha detección | Qué pasó | Datos / personas | Riesgo | Contención | ¿Aviso Agencia? | ¿Aviso personas? | Cierre |
|---|---|---|---|---|---|---|---|
| — | Sin incidentes registrados | | | | | | |

> El hallazgo de permisos abiertos en la base de datos detectado el 12-nov-2026 se corrigió el 13-nov-2026
> antes de que rigiera la ley; el detalle está documentado en privado.
