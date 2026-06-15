import { defineNuxtConfig } from 'nuxt/config'
import { site } from './data/site'

export default defineNuxtConfig({
  compatibilityDate: '2026-06-14',
  // Mantiene la estructura clásica (pages/components/data en la raíz).
  srcDir: '.',
  modules: ['@nuxtjs/tailwindcss'],
  // Auto-import por nombre de archivo (sin prefijo de carpeta): <CtaButton>, <HeroSection>, etc.
  components: [{ path: '~/components', pathPrefix: false }],
  css: ['~/assets/css/main.css'],
  devtools: { enabled: true },

  runtimeConfig: {
    public: {
      // Estos valores se sobreescriben con las env NUXT_PUBLIC_* en runtime.
      siteUrl: 'http://localhost:3000',
      apiBase: 'http://localhost:8000',
      whatsappNumber: '',
      instagramUser: 'enbellezaser'
    }
  },

  typescript: {
    strict: true,
    typeCheck: false
  },

  app: {
    head: {
      htmlAttrs: { lang: 'es' },
      title: site.seo.title,
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'theme-color', content: '#FBF6EF' },
        // Open Graph base (los campos dinámicos con URL absoluta se setean en pages/index.vue).
        { property: 'og:type', content: 'website' },
        { property: 'og:site_name', content: site.name },
        { name: 'twitter:card', content: 'summary_large_image' }
      ],
      link: [
        { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' },
        { rel: 'apple-touch-icon', href: '/favicon.svg' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Nunito+Sans:wght@300;400;600;700&display=swap'
        }
      ]
    }
  },

  // SSR (sin prerender): el servidor Node renderiza en cada request leyendo las
  // env NUXT_PUBLIC_* en runtime. Así el número de WhatsApp, el usuario de IG y la
  // URL del sitio se configuran por entorno SIN rebuild. robots.txt y sitemap.xml
  // son server routes dinámicas que también leen la config en runtime.
})
