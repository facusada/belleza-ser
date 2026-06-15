"""Factory de proveedores de pago.

Lee `PAYMENT_PROVIDER` del entorno y devuelve la implementación correspondiente.
Para activar Mercado Pago en la v2: crear `MercadoPagoProvider(PaymentProvider)`
y registrarlo en `_PROVIDERS`.
"""

from app.core.config import settings
from app.services.payments.base import PaymentProvider
from app.services.payments.stub import StubPaymentProvider

_PROVIDERS: dict[str, type[PaymentProvider]] = {
    "stub": StubPaymentProvider,
    # "mercadopago": MercadoPagoProvider,  # <- v2
}


def get_payment_provider() -> PaymentProvider:
    provider_cls = _PROVIDERS.get(settings.payment_provider, StubPaymentProvider)
    return provider_cls()
