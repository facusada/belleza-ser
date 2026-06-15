<script setup lang="ts">
import { computed } from 'vue'
import { site } from '~/data/site'
import { useWhatsApp } from '~/composables/useWhatsApp'

const config = useRuntimeConfig().public
const { url } = useWhatsApp()

const whatsappHref = url('¡Hola! 🌿')
const instagramHref = `https://instagram.com/${config.instagramUser}`
const year = computed(() => new Date().getFullYear())
</script>

<template>
  <footer class="border-t border-bs-sand bg-bs-cream">
    <div class="bs-container flex flex-col items-center gap-6 py-12 text-center">
      <p class="font-display text-3xl text-bs-ink">{{ site.name }}</p>
      <p class="max-w-md text-sm text-bs-muted">{{ site.tagline }}</p>

      <div class="flex items-center gap-6 text-sm">
        <a
          :href="instagramHref"
          target="_blank"
          rel="noopener noreferrer"
          class="text-bs-plum transition-colors hover:text-bs-ink"
        >
          Instagram @{{ config.instagramUser }}
        </a>
        <a
          :href="whatsappHref"
          target="_blank"
          rel="noopener noreferrer"
          class="text-bs-plum transition-colors hover:text-bs-ink"
        >
          WhatsApp
        </a>
      </div>

      <p class="text-xs text-bs-muted">© {{ year }} {{ site.name }}. Todos los derechos reservados.</p>
    </div>
  </footer>
</template>
