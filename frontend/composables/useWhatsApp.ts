import { buildWhatsAppUrl } from '~/utils/whatsapp'

/**
 * Acceso al WhatsApp del negocio. Lee el número de la config pública (env).
 */
export function useWhatsApp() {
  const number = useRuntimeConfig().public.whatsappNumber as string

  const url = (message = '') => buildWhatsAppUrl(number, message)

  return { number, url }
}
