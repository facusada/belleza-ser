/**
 * FUENTE ÚNICA de los servicios que muestra el sitio.
 * Para editar precios, descripciones o textos: cambiá SOLO este archivo.
 * El número de WhatsApp y el usuario de Instagram NO van acá: son variables
 * de entorno (ver .env / NUXT_PUBLIC_WHATSAPP_NUMBER, NUXT_PUBLIC_INSTAGRAM_USER).
 */

export interface Service {
  /** Identificador estable; se manda al backend como `service_slug`. */
  slug: string
  name: string
  /** Frase corta para la card. */
  tagline: string
  /** Descripción completa del servicio. */
  description: string
  /** Emoji o símbolo decorativo de la card. */
  icon: string
  /** Precio para mostrar (opcional). v1 puede dejarse vacío. */
  price?: string
  /** Mensaje que se pre-carga en WhatsApp al reservar este servicio. */
  whatsappMessage: string
}

export const services: Service[] = [
  {
    slug: 'reenergizacion',
    name: 'Sesiones de reenergización',
    tagline: 'Recuperá tu equilibrio y vitalidad',
    description:
      'Una sesión a distancia para liberar bloqueos energéticos, armonizar tus centros y reconectar con tu vitalidad. Trabajamos sobre el cansancio, el estrés y las emociones estancadas para devolverte claridad y calma.',
    icon: '✺',
    whatsappMessage: '¡Hola! Me interesa una sesión de reenergización. ¿Cómo la coordinamos?'
  },
  {
    slug: 'biodecodificacion',
    name: 'Sesiones de biodecodificación',
    tagline: 'Descubrí el origen emocional de lo que sentís',
    description:
      'Un acompañamiento para entender qué emoción o conflicto está detrás de un síntoma o situación que se repite. A través del diálogo y la decodificación, encontramos el sentido y abrimos el camino para sanarlo.',
    icon: '❀',
    whatsappMessage: '¡Hola! Me interesa una sesión de biodecodificación. ¿Cómo la coordinamos?'
  },
  {
    slug: 'cartas-numerologicas',
    name: 'Cartas numerológicas',
    tagline: 'Tu mapa personal a través de los números',
    description:
      'Un estudio numerológico personalizado que revela tus talentos, tus desafíos y los ciclos que estás transitando. Una guía para tomar decisiones con más conciencia y alinearte con tu propósito.',
    icon: '✷',
    whatsappMessage: '¡Hola! Me interesa una carta numerológica. ¿Cómo la coordinamos?'
  },
  {
    slug: 'ebook',
    name: 'E-book',
    tagline: 'Material para acompañar tu proceso',
    description:
      'Un material descargable con prácticas y reflexiones para sostener tu bienestar en lo cotidiano. Pensado para que puedas volver a él cada vez que lo necesites.',
    icon: '❧',
    whatsappMessage: '¡Hola! Quiero adquirir el e-book. ¿Cómo lo obtengo?'
  }
]

export const findService = (slug: string): Service | undefined =>
  services.find((s) => s.slug === slug)
