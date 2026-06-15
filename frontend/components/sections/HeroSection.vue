<script setup lang="ts">
import { site } from '~/data/site'
import { useWhatsApp } from '~/composables/useWhatsApp'

const { url } = useWhatsApp()
const heroHref = url('¡Hola! Me gustaría saber más sobre tus servicios de bienestar. 🌿')
</script>

<template>
  <section class="relative overflow-hidden bg-bs-aura">
    <div class="bs-container flex min-h-[88vh] flex-col items-center justify-center py-24 text-center">
      <p class="bs-eyebrow animate-fade-up">{{ site.hero.eyebrow }}</p>

      <h1
        class="mt-5 max-w-3xl text-4xl font-medium leading-[1.05] text-bs-ink animate-fade-up sm:text-6xl"
        style="animation-delay: 0.08s"
      >
        {{ site.hero.title }}
      </h1>

      <p
        class="mt-6 max-w-xl text-lg leading-relaxed text-bs-muted animate-fade-up"
        style="animation-delay: 0.16s"
      >
        {{ site.hero.subtitle }}
      </p>

      <div
        class="mt-9 flex flex-col items-center gap-3 animate-fade-up sm:flex-row"
        style="animation-delay: 0.24s"
      >
        <CtaButton :href="heroHref" external variant="primary">
          {{ site.hero.ctaLabel }}
        </CtaButton>
        <CtaButton href="#servicios" variant="ghost">
          {{ site.hero.secondaryLabel }}
        </CtaButton>
      </div>
    </div>

    <!-- Separador suave hacia la siguiente sección -->
    <div class="h-px w-full bg-gradient-to-r from-transparent via-bs-clay/40 to-transparent" />
  </section>
</template>
