<script setup lang="ts">
import { site } from '~/data/site'
</script>

<template>
  <section id="sobre-mi" class="scroll-mt-20 bg-bs-sand/40 py-24">
    <div class="bs-container grid items-center gap-12 lg:grid-cols-2">
      <RevealOnScroll>
        <div
          class="aspect-[4/5] w-full rounded-[2rem] bg-bs-aura shadow-soft ring-1 ring-bs-clay/20"
        >
          <div class="flex h-full items-center justify-center text-7xl text-bs-plum/40">
            ✺
          </div>
        </div>
      </RevealOnScroll>

      <RevealOnScroll>
        <p class="bs-eyebrow">{{ site.about.title }}</p>
        <h2 class="mt-3 text-4xl text-bs-ink sm:text-5xl">Un espacio para reencontrarte</h2>
        <div class="mt-6 space-y-5 text-lg leading-relaxed text-bs-muted">
          <p v-for="(p, i) in site.about.paragraphs" :key="i">{{ p }}</p>
        </div>
      </RevealOnScroll>
    </div>
  </section>
</template>
