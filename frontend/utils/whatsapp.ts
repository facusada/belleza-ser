/**
 * Constructor puro del link de WhatsApp (sin dependencias de Nuxt → testeable).
 * @param number Número en formato internacional sin '+' ni espacios (ej: 5491100000000).
 * @param message Mensaje a pre-cargar en el chat.
 */
export function buildWhatsAppUrl(number: string | number, message = ''): string {
  // Nuxt parsea env numéricas como number (destr); por eso coercionamos a string.
  const digits = String(number ?? '').replace(/\D/g, '')
  const base = `https://wa.me/${digits}`
  return message ? `${base}?text=${encodeURIComponent(message)}` : base
}
