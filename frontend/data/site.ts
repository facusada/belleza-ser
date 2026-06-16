/**
 * Textos y datos generales del sitio (editables en un solo lugar).
 * El número de WhatsApp y el usuario de Instagram se configuran por entorno.
 */

export const site = {
  name: 'EnbellezaSer',
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
    heading: 'Un espacio para reencontrarte',
    paragraphs: [
      'EnbellezaSer nace del deseo de acompañar a otras personas en su camino a reencontrarse consigo mismas, activando la autosanación de su ser y logrando así reconectarse en las distintas etapas de la vida en la que se encuentre.',
      'Cada sesión está pensada para asistir, liberar y trascender el síntoma o patrón que esté limitando a tu cuerpo físico, trabajándolo de manera integral. La respuesta siempre estuvo hacia adentro: te espero para que juntos logremos tu mejor versión.'
    ]
  },

  aboutMe: {
    title: 'Acerca de mí',
    heading: 'Soy María Milagros',
    paragraphs: [
      'Bienvenidos a EnbellezaSer. Acá me presento: soy María Milagros y trabajo en consultorio hace más de 7 años. Me he capacitado en Reiki, Reflexología, Biodecodificación, Reenergetización, Barras de Access, Yoga, Alimentación intuitiva y Registros akáshicos.',
      'Pero mi mejor estudio fue y sigue siendo la experiencia: el día a día, el descubrir mi mejor versión en las diferentes etapas de la vida, el hacer espacio en lo cotidiano para habitar el presente, superando los desafíos y convirtiéndolos en aprendizaje para integrarlos y crear la vida desde el Ser.',
      'Estas herramientas nacen de mi propio proceso, para que de “todo lo que elijas ser, elijas libre cada vez…” ✨'
    ]
  },

  ebook: {
    title: 'E-book',
    description:
      'Un material para acompañarte a usar tu energía, tus pensamientos y tus emociones desde la creación. El compromiso es con VOS.',
    quotes: [
      'Usá tu energía para crear, no para preocuparte.',
      'Usá tus pensamientos para crecer, no para dudar.',
      'Usá tus emociones para atraer, no para alejar.'
    ],
    ctaLabel: 'Quiero el e-book'
  },

  contact: {
    title: 'Empecemos a conversar',
    subtitle:
      'Escribime por WhatsApp o dejame tus datos y te contacto. Estoy para acompañarte.',
    formNote: 'Te respondo a la brevedad. Tus datos son privados y no se comparten.'
  },

  seo: {
    title: 'EnbellezaSer — Bienestar holístico y sanación a distancia',
    description:
      'Sesiones de reenergización, biodecodificación y cartas numerológicas a distancia. Un espacio cálido para reconectar con tu equilibrio. Reservá por WhatsApp.',
    // Reemplazá por una imagen real en /public/og-image.* para compartir en IG/WhatsApp.
    ogImage: '/og-image.svg'
  }
} as const
