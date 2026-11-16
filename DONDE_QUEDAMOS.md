# Dónde quedamos

> **Para cualquier asistente (Claude Code o Cowork): lee este archivo ANTES de hacer nada, y actualízalo AL TERMINAR.**
> Es el puente entre sesiones y entre productos. Lo que no esté aquí o en GitHub, el otro no lo sabe.

## Reglas de trabajo (siempre)

1. **GitHub `main` es la verdad.** Antes de tocar nada, poner al día las copias locales (sitio `Escenciecl/Polyplas-web` y oficina `Escenciecl/oficina-polyplas`).
2. **Cada cambio al sitio:** rama nueva → PR → la jefa hace Merge → borrar la rama. Nunca publicar sin su Merge.
3. **Al terminar cada bloque de trabajo:** subir todo a GitHub (nada a medias solo en el computador) y **actualizar este archivo**.
4. Explicar en lenguaje simple: la jefa no es programadora.
5. No ingresar contraseñas ni claves; las pega la jefa.

## Estado actual — 16-nov-2026 (cerrado por Claude Code)

**Publicado hoy en polyplas.cl (PR #21 a #27):**
- Crear cuenta en la página de gracias + Mi cuenta suma compras anteriores del mismo correo (SQL `pp_vincular_mis_compras` ejecutado).
- Ingreso claro: botón "Ingresar" azul, pestañas Ingresar/Crear cuenta, accesible.
- Repetir pedido en un clic (Mi cuenta y correo de comprobante).
- Pago con datos de la cuenta ya llenados (solo clientes con sesión).
- Al ingresar va a Mi cuenta; cabecera "Hola, nombre"; aviso "Tu pedido sigue en el carro"; pantalla "Crea tu nueva contraseña".

**Configurado hoy (fuera del código):**
- Correos de las cuentas en español por **Brevo** (remitente ventas@polyplas.cl), límite 100/hora. Probado: entregado.
- ⚠️ **No desactivar "Enable custom SMTP" en Supabase**: borra las plantillas en español.

**Pendiente (en orden sugerido):**
1. Medición: activadores GTM de `login`, `sign_up`, `repetir_pedido`, `checkout_autocompletado`, `checkout_datos_borrados`, `aviso_carro`, `cuenta_ofrecida`, `cuenta_rechazada`.
2. Estado del pedido en Mi cuenta (Pagado → En preparación → Listo para retiro → Entregado).
3. Documentos para descargar (comprobante y diagrama de cortes).
4. Revisar comuna de facturación que a veces queda "Santiago" (empresa + RM + otra comuna).
5. **30-nov:** decisión de la jefa sobre abandono en "Datos y envío" (ver `agentes/cro/REGISTRO_CAMBIOS.md`).

**En espera (NO hacer):**
- "Mis datos personales" (Ley 21.719): espera revisión de un abogado.

**Copias en el computador de la jefa (no afectan producción):** rama `respaldo-local-2026-11-16` (basura) y `vigilante-pruebas` en `~/Polyplas-web-vig` (prueba del Vigilante a medias, 13-nov).

---
*Al actualizar: reemplazar la sección "Estado actual" con fecha, quién cerró (Claude Code / Cowork) y lo mismo: publicado, configurado, pendiente, en espera.*
