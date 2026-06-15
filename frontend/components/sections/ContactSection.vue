<script setup lang="ts">
import { reactive, ref } from 'vue'
import { site } from '~/data/site'
import { services } from '~/data/services'
import { useWhatsApp } from '~/composables/useWhatsApp'

const config = useRuntimeConfig().public
const { url: waUrl } = useWhatsApp()

const whatsappHref = waUrl('¡Hola! Quiero hacer una consulta. 🌿')
const instagramHref = `https://instagram.com/${config.instagramUser}`

const form = reactive({
  name: '',
  email: '',
  phone: '',
  service_slug: '',
  message: ''
})

type Status = 'idle' | 'sending' | 'success' | 'error'
const status = ref<Status>('idle')
const errorMsg = ref('')

async function onSubmit() {
  status.value = 'sending'
  errorMsg.value = ''
  try {
    await $fetch(`${config.apiBase}/api/leads`, {
      method: 'POST',
      body: {
        name: form.name,
        email: form.email || null,
        phone: form.phone || null,
        service_slug: form.service_slug || null,
        message: form.message || null
      }
    })
    status.value = 'success'
  } catch (err: unknown) {
    status.value = 'error'
    errorMsg.value =
      'No pudimos enviar tu mensaje. Probá de nuevo o escribinos por WhatsApp.'
    console.error(err)
  }
}
</script>

<template>
  <section id="contacto" class="scroll-mt-20 bg-bs-sand/40 py-24">
    <div class="bs-container grid gap-12 lg:grid-cols-2">
      <RevealOnScroll>
        <p class="bs-eyebrow">Contacto</p>
        <h2 class="mt-3 text-4xl text-bs-ink sm:text-5xl">{{ site.contact.title }}</h2>
        <p class="mt-4 text-lg leading-relaxed text-bs-muted">{{ site.contact.subtitle }}</p>

        <div class="mt-8 flex flex-col gap-3 sm:flex-row">
          <CtaButton :href="whatsappHref" external variant="primary">WhatsApp</CtaButton>
          <CtaButton :href="instagramHref" external variant="ghost">
            @{{ config.instagramUser }}
          </CtaButton>
        </div>
      </RevealOnScroll>

      <RevealOnScroll>
        <form
          class="rounded-3xl border border-bs-sand bg-white/80 p-7 shadow-soft"
          @submit.prevent="onSubmit"
        >
          <template v-if="status !== 'success'">
            <div class="grid gap-4">
              <label class="block">
                <span class="text-sm font-semibold text-bs-ink">Nombre *</span>
                <input
                  v-model="form.name"
                  type="text"
                  required
                  minlength="2"
                  class="mt-1 w-full rounded-xl border border-bs-clay/40 bg-bs-cream/60 px-4 py-2.5 text-bs-ink outline-none focus:border-bs-plum"
                />
              </label>

              <div class="grid gap-4 sm:grid-cols-2">
                <label class="block">
                  <span class="text-sm font-semibold text-bs-ink">Email</span>
                  <input
                    v-model="form.email"
                    type="email"
                    class="mt-1 w-full rounded-xl border border-bs-clay/40 bg-bs-cream/60 px-4 py-2.5 text-bs-ink outline-none focus:border-bs-plum"
                  />
                </label>
                <label class="block">
                  <span class="text-sm font-semibold text-bs-ink">WhatsApp / Teléfono</span>
                  <input
                    v-model="form.phone"
                    type="tel"
                    class="mt-1 w-full rounded-xl border border-bs-clay/40 bg-bs-cream/60 px-4 py-2.5 text-bs-ink outline-none focus:border-bs-plum"
                  />
                </label>
              </div>

              <label class="block">
                <span class="text-sm font-semibold text-bs-ink">Servicio de interés</span>
                <select
                  v-model="form.service_slug"
                  class="mt-1 w-full rounded-xl border border-bs-clay/40 bg-bs-cream/60 px-4 py-2.5 text-bs-ink outline-none focus:border-bs-plum"
                >
                  <option value="">Sin preferencia</option>
                  <option v-for="s in services" :key="s.slug" :value="s.slug">
                    {{ s.name }}
                  </option>
                </select>
              </label>

              <label class="block">
                <span class="text-sm font-semibold text-bs-ink">Mensaje</span>
                <textarea
                  v-model="form.message"
                  rows="4"
                  class="mt-1 w-full rounded-xl border border-bs-clay/40 bg-bs-cream/60 px-4 py-2.5 text-bs-ink outline-none focus:border-bs-plum"
                />
              </label>

              <p v-if="status === 'error'" class="text-sm text-red-700">{{ errorMsg }}</p>

              <CtaButton variant="primary" block>
                <span v-if="status === 'sending'">Enviando…</span>
                <span v-else>Enviar mensaje</span>
              </CtaButton>

              <p class="text-center text-xs text-bs-muted">{{ site.contact.formNote }}</p>
            </div>
          </template>

          <div v-else class="py-10 text-center">
            <span class="text-4xl text-bs-gold">✺</span>
            <h3 class="mt-4 text-2xl text-bs-ink">¡Gracias por escribir!</h3>
            <p class="mt-2 text-bs-muted">Te voy a responder a la brevedad. 🌿</p>
          </div>
        </form>
      </RevealOnScroll>
    </div>
  </section>
</template>
