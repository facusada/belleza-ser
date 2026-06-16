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
    name: 'Sesiones de Reenergetización',
    tagline: 'Alineá todos tus cuerpos desde la consciencia',
    description:
      'Una técnica que alinea todos los cuerpos —mental, emocional, físico y espiritual— a través de la apertura de consciencia en cada persona. Solo la propia consciencia puede lograr cambios profundos y radicales en cada ser. La Reenergetización permite un cambio en las estructuras, patrones y mandatos que puedan estar alterando el equilibrio de los cuerpos. Esta herramienta profundiza en la sanación, limpiando todo bloqueo, registro familiar ancestral y mal karma.',
    icon: '✺',
    whatsappMessage: '¡Hola! Me interesa una sesión de Reenergetización. ¿Cómo la coordinamos?'
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
    tagline: 'Personales y de pareja',
    description:
      'En esta carta encontrarás herramientas para alinearte con tu misión de vida y entender qué te impide ser lo que realmente querés. A través de tu fecha de nacimiento y tu nombre completo, realizamos un análisis que te sirva de guía en tu vida, volviéndote un observador de vos mismo y logrando así liberar tus bloqueos. ¿Estás necesitando un cambio y no sabés por dónde empezar? La numerología te puede ayudar. Disponible en cartas personales y de pareja.',
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
