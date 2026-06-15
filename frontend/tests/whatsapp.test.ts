import { describe, expect, it } from 'vitest'
import { buildWhatsAppUrl } from '../utils/whatsapp'

describe('buildWhatsAppUrl', () => {
  it('arma el link base con el número limpio', () => {
    expect(buildWhatsAppUrl('5491100000000')).toBe('https://wa.me/5491100000000')
  })

  it('quita caracteres no numéricos del número', () => {
    expect(buildWhatsAppUrl('+54 9 11 0000-0000')).toBe('https://wa.me/5491100000000')
  })

  it('acepta un número (Nuxt parsea env numéricas como number)', () => {
    expect(buildWhatsAppUrl(5491112345678)).toBe('https://wa.me/5491112345678')
  })

  it('codifica el mensaje en el query param text', () => {
    const url = buildWhatsAppUrl('5491100000000', '¡Hola! Quiero una sesión 🌿')
    expect(url.startsWith('https://wa.me/5491100000000?text=')).toBe(true)
    expect(url).toContain(encodeURIComponent('¡Hola! Quiero una sesión 🌿'))
  })

  it('no agrega query si no hay mensaje', () => {
    expect(buildWhatsAppUrl('5491100000000', '')).not.toContain('?')
  })
})
