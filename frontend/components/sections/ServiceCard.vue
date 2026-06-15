<script setup lang="ts">
import type { Service } from '~/data/services'
import { useServiceAction } from '~/composables/useServiceAction'

const props = defineProps<{ service: Service }>()
const { actionFor } = useServiceAction()
const action = actionFor(props.service)
</script>

<template>
  <article
    class="flex h-full flex-col rounded-3xl border border-bs-sand bg-white/70 p-7 shadow-soft transition-all duration-300 hover:-translate-y-1 hover:shadow-card"
  >
    <span class="text-3xl text-bs-gold" aria-hidden="true">{{ service.icon }}</span>

    <h3 class="mt-4 text-2xl text-bs-ink">{{ service.name }}</h3>
    <p class="mt-1 text-sm font-semibold uppercase tracking-wider text-bs-plum">
      {{ service.tagline }}
    </p>

    <p class="mt-4 flex-1 text-[15px] leading-relaxed text-bs-muted">
      {{ service.description }}
    </p>

    <p v-if="service.price" class="mt-4 text-lg font-semibold text-bs-ink">
      {{ service.price }}
    </p>

    <!-- La acción la decide useServiceAction: hoy WhatsApp, mañana checkout. -->
    <div class="mt-6">
      <CtaButton
        :href="action.kind === 'whatsapp' ? action.href : undefined"
        :to="action.kind === 'checkout' ? action.to : undefined"
        :external="action.external"
        variant="primary"
        block
      >
        {{ action.label }}
      </CtaButton>
    </div>
  </article>
</template>
