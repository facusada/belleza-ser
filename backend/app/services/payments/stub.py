"""Proveedor de pagos stub para la v1 (la web todavía no cobra online)."""

from app.services.payments.base import (
    CheckoutSession,
    PaymentProvider,
    PaymentResult,
)


class StubPaymentProvider(PaymentProvider):
    """No cobra nada. Existe para que la app arranque sin un proveedor real."""

    name = "stub"

    async def create_checkout(
        self, *, order_id: int, amount: float, currency: str, description: str
    ) -> CheckoutSession:
        raise NotImplementedError(
            "Los pagos online no están habilitados en la v1. "
            "Configurá PAYMENT_PROVIDER=mercadopago e implementá el proveedor."
        )

    async def handle_webhook(self, payload: dict) -> PaymentResult:
        raise NotImplementedError(
            "Los pagos online no están habilitados en la v1."
        )
