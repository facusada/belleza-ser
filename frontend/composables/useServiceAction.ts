import type { Service } from '~/data/services'

/**
 * SEAM PARA EL FUTURO (v2 con pagos online).
 *
 * Hoy la acción de "Reservar / Comprar" siempre es abrir WhatsApp. Cuando se
 * sume el checkout, esta función podrá devolver `{ kind: 'checkout', to }` para
 * algunos servicios, y los componentes (ServiceCard / CtaButton) NO cambian:
 * sólo consumen el descriptor que devuelve este composable.
 */

export interface WhatsAppAction {
  kind: 'whatsapp'
  label: string
  href: string
  external: true
}

export interface CheckoutAction {
  kind: 'checkout'
  label: string
  to: string
  external: false
}

export type ServiceAction = WhatsAppAction | CheckoutAction

export function useServiceAction() {
  const { url } = useWhatsApp()

  const actionFor = (service: Service): ServiceAction => {
    // v1: todo va a WhatsApp con el mensaje pre-cargado del servicio.
    return {
      kind: 'whatsapp',
      label: service.slug === 'ebook' ? 'Adquirir por WhatsApp' : 'Reservar por WhatsApp',
      href: url(service.whatsappMessage),
      external: true
    }
    // v2 (ejemplo):
    // if (service.checkoutEnabled) {
    //   return { kind: 'checkout', label: 'Comprar', to: `/checkout/${service.slug}`, external: false }
    // }
  }

  return { actionFor }
}
