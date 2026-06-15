/**
 * Textos y datos generales del sitio (editables en un solo lugar).
 * El número de WhatsApp y el usuario de Instagram se configuran por entorno.
 */

export const site = {
  name: 'Belleza Ser',
  tagline: 'Bienestar holístico y sanación a distancia',

  hero: {
    eyebrow: 'Terapias holísticas a distancia',
    title: 'Volvé a habitarte con calma',
    subtitle:
      'Acompañamiento energético y emocional para reencontrar tu equilibrio, dondequiera que estés. Sesiones a distancia, presencia cercana.',
    ctaLabel: 'Reservar por WhatsApp',
    secondaryLabel: 'Conocé los servicios'
  },

  about: {
    title: 'Sobre el espacio',
    paragraphs: [
      'Belleza Ser nace del deseo de acompañar a otras personas en su proceso de sanación y autoconocimiento. Cada encuentro es un espacio seguro, amoroso y sin juicios.',
      'Trabajo de manera holística: integro lo energético, lo emocional y lo simbólico para que puedas reconectar con tu bienestar más profundo. Todas las sesiones son a distancia, así la geografía nunca es un límite.'
    ]
  },

  ebook: {
    title: 'E-book',
    description:
      'Un material descargable con prácticas y reflexiones para sostener tu bienestar día a día. Pronto disponible para adquirir online; por ahora lo coordinamos por WhatsApp.',
    ctaLabel: 'Quiero el e-book'
  },

  contact: {
    title: 'Empecemos a conversar',
    subtitle:
      'Escribime por WhatsApp o dejame tus datos y te contacto. Estoy para acompañarte.',
    formNote: 'Te respondo a la brevedad. Tus datos son privados y no se comparten.'
  },

  seo: {
    title: 'Belleza Ser — Bienestar holístico y sanación a distancia',
    description:
      'Sesiones de reenergización, biodecodificación y cartas numerológicas a distancia. Un espacio cálido para reconectar con tu equilibrio. Reservá por WhatsApp.',
    // Reemplazá por una imagen real en /public/og-image.* para compartir en IG/WhatsApp.
    ogImage: '/og-image.svg'
  }
} as const
