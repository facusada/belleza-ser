<script setup lang="ts">
import { site } from '~/data/site'
import { findService } from '~/data/services'
import { useWhatsApp } from '~/composables/useWhatsApp'

const { url } = useWhatsApp()
const ebook = findService('ebook')
const ebookHref = url(ebook?.whatsappMessage ?? '¡Hola! Quiero adquirir el e-book.')
</script>

<template>
  <section id="ebook" class="bs-container scroll-mt-20 py-24">
    <RevealOnScroll>
      <div
        class="relative overflow-hidden rounded-[2.5rem] bg-bs-plum px-8 py-16 text-center text-bs-cream shadow-card sm:px-16"
      >
        <div class="pointer-events-none absolute inset-0 bg-bs-aura opacity-30" />
        <div class="relative mx-auto max-w-2xl">
          <span class="text-4xl text-bs-gold" aria-hidden="true">❧</span>
          <p class="mt-4 text-xs font-semibold uppercase tracking-[0.22em] text-bs-gold">
            Material descargable
          </p>
          <h2 class="mt-3 text-4xl sm:text-5xl">{{ site.ebook.title }}</h2>
          <p class="mt-5 text-lg leading-relaxed text-bs-cream/85">
            {{ site.ebook.description }}
          </p>
          <div class="mt-8 flex justify-center">
            <CtaButton :href="ebookHref" external variant="secondary">
              {{ site.ebook.ctaLabel }}
            </CtaButton>
          </div>
        </div>
      </div>
    </RevealOnScroll>
  </section>
</template>
