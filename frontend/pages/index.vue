<script setup lang="ts">
import { site } from '~/data/site'

const siteUrl = useRuntimeConfig().public.siteUrl as string
const ogImageUrl = `${siteUrl}${site.seo.ogImage}`

// SEO + Open Graph. No seteamos `title` acá para que titleTemplate use el título
// completo del sitio en la home (sin duplicar "| EnbellezaSer").
useSeoMeta({
  description: () => site.seo.description,
  ogUrl: () => siteUrl,
  ogTitle: () => site.seo.title,
  ogDescription: () => site.seo.description,
  ogImage: () => ogImageUrl,
  twitterTitle: () => site.seo.title,
  twitterDescription: () => site.seo.description,
  twitterImage: () => ogImageUrl
})
useHead({
  link: [{ rel: 'canonical', href: siteUrl }]
})
</script>

<template>
  <div>
    <HeroSection />
    <ServicesSection />
    <AboutSection />
    <EbookSection />
    <!-- Formulario de contacto/leads: oculto por ahora. Feature lista para activar:
         descomentar esta línea y el link "Contacto" en AppHeader.vue. -->
    <!-- <ContactSection /> -->
  </div>
</template>
