import { onBeforeUnmount, onMounted, ref } from 'vue'

/**
 * Anima la aparición de un elemento al entrar en viewport (IntersectionObserver).
 * Devuelve un `target` para enlazar al elemento y un `visible` reactivo.
 */
export function useReveal(options: { threshold?: number; once?: boolean } = {}) {
  const { threshold = 0.15, once = true } = options
  const target = ref<HTMLElement | null>(null)
  const visible = ref(false)
  let observer: IntersectionObserver | null = null

  onMounted(() => {
    // SSR-safe + respeta usuarios que prefieren menos movimiento.
    if (typeof IntersectionObserver === 'undefined') {
      visible.value = true
      return
    }

    observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            visible.value = true
            if (once && observer && target.value) observer.unobserve(target.value)
          } else if (!once) {
            visible.value = false
          }
        }
      },
      { threshold }
    )

    if (target.value) observer.observe(target.value)
  })

  onBeforeUnmount(() => observer?.disconnect())

  return { target, visible }
}
