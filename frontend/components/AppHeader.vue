<script setup lang="ts">
import { site } from '~/data/site'
import { useWhatsApp } from '~/composables/useWhatsApp'

const { url } = useWhatsApp()
const ctaHref = url('¡Hola! Me gustaría coordinar una sesión. 🌿')

const links = [
  { label: 'Servicios', href: '#servicios' },
  { label: 'Sobre mí', href: '#sobre-mi' },
  { label: 'E-book', href: '#ebook' }
  // Contacto/leads oculto por ahora (ver ContactSection en pages/index.vue):
  // { label: 'Contacto', href: '#contacto' }
]
</script>

<template>
  <header class="sticky top-0 z-40 border-b border-bs-sand/70 bg-bs-cream/80 backdrop-blur">
    <div class="bs-container flex h-16 items-center justify-between">
      <a href="#" class="font-display text-2xl font-medium tracking-wide text-bs-ink">
        {{ site.name }}
      </a>

      <nav class="hidden items-center gap-8 md:flex">
        <a
          v-for="link in links"
          :key="link.href"
          :href="link.href"
          class="text-sm text-bs-muted transition-colors hover:text-bs-plum"
        >
          {{ link.label }}
        </a>
      </nav>

      <CtaButton :href="ctaHref" external variant="primary" class="!px-5 !py-2 text-xs">
        WhatsApp
      </CtaButton>
    </div>
  </header>
</template>
