"""Capa de pagos abstracta.

`PaymentProvider` define el contrato que cualquier proveedor (Mercado Pago, Stripe,
etc.) debe cumplir. La v1 usa `StubPaymentProvider`. Sumar Mercado Pago en la v2 =
implementar esta interfaz y registrarla en la factory (`app/services/payments/__init__.py`),
sin tocar el resto del backend ni la UI.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CheckoutSession:
    """Resultado de iniciar un checkout: a dónde mandar al usuario a pagar."""

    provider: str
    checkout_url: str
    external_id: str | None = None


@dataclass
class PaymentResult:
    """Resultado normalizado de un webhook/confirmación de pago."""

    provider: str
    external_id: str
    status: str  # "approved", "pending", "rejected"
    amount: float
    currency: str = "ARS"


class PaymentProvider(ABC):
    """Contrato de un proveedor de pagos."""

    name: str = "base"

    @abstractmethod
    async def create_checkout(
        self, *, order_id: int, amount: float, currency: str, description: str
    ) -> CheckoutSession:
        """Inicia un cobro y devuelve la URL de checkout."""
        raise NotImplementedError

    @abstractmethod
    async def handle_webhook(self, payload: dict) -> PaymentResult:
        """Procesa la notificación del proveedor y normaliza el resultado."""
        raise NotImplementedError
