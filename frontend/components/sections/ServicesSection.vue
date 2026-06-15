<script setup lang="ts">
import { services } from '~/data/services'
</script>

<template>
  <section id="servicios" class="bs-container scroll-mt-20 py-24">
    <RevealOnScroll>
      <div class="mx-auto max-w-2xl text-center">
        <p class="bs-eyebrow">Servicios</p>
        <h2 class="mt-3 text-4xl text-bs-ink sm:text-5xl">Formas de acompañarte</h2>
        <p class="mt-4 text-bs-muted">
          Todas las sesiones son a distancia. Elegí la que resuene con vos y coordinamos por WhatsApp.
        </p>
      </div>
    </RevealOnScroll>

    <div class="mt-14 grid gap-7 sm:grid-cols-2 lg:grid-cols-3">
      <RevealOnScroll v-for="service in services" :key="service.slug">
        <ServiceCard :service="service" class="h-full" />
      </RevealOnScroll>
    </div>
  </section>
</template>
