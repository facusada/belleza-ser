<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    /** Si se pasa, renderiza un <a> (ej: link de WhatsApp). */
    href?: string
    /** Si se pasa, renderiza un <NuxtLink> interno (ej: futuro checkout). */
    to?: string
    variant?: 'primary' | 'secondary' | 'ghost'
    external?: boolean
    block?: boolean
  }>(),
  { variant: 'primary', external: false, block: false }
)

const base =
  'inline-flex items-center justify-center gap-2 rounded-full px-7 py-3 text-sm font-semibold tracking-wide transition-all duration-300 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-bs-plum'

const variants: Record<string, string> = {
  primary: 'bg-bs-plum text-bs-cream shadow-card hover:bg-bs-ink hover:-translate-y-0.5',
  secondary: 'bg-bs-gold/90 text-bs-ink hover:bg-bs-gold hover:-translate-y-0.5',
  ghost: 'border border-bs-clay/60 text-bs-ink hover:border-bs-plum hover:text-bs-plum'
}

const classes = computed(() => [base, variants[props.variant], props.block ? 'w-full' : ''])

const tag = computed(() => (props.to ? 'NuxtLink' : props.href ? 'a' : 'button'))
const externalAttrs = computed(() =>
  props.href && props.external ? { target: '_blank', rel: 'noopener noreferrer' } : {}
)
</script>

<template>
  <component
    :is="tag"
    :to="to"
    :href="href"
    v-bind="externalAttrs"
    :class="classes"
  >
    <slot />
  </component>
</template>
