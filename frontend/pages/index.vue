<script setup lang="ts">
import { site } from '~/data/site'

const siteUrl = useRuntimeConfig().public.siteUrl as string
const ogImageUrl = `${siteUrl}${site.seo.ogImage}`

// SEO + Open Graph. No seteamos `title` acá para que titleTemplate use el título
// completo del sitio en la home (sin duplicar "| Belleza Ser").
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
    <ContactSection />
  </div>
</template>
