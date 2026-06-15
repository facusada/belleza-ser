<script setup lang="ts">
import { useReveal } from '~/composables/useReveal'

withDefaults(defineProps<{ as?: string }>(), { as: 'div' })
const { target, visible } = useReveal()
</script>

<template>
  <component :is="as" ref="target" class="reveal" :class="{ 'is-visible': visible }">
    <slot />
  </component>
</template>
