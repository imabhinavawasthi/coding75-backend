from dataclasses import dataclass


@dataclass
class CreateOrderRequest:
    def __init__(self, amount: int, currency: str, receipt: str, notes: dict = None):
        self.amount = amount
        self.currency = currency
        self.receipt = receipt
        self.notes = notes or {}

    def to_dict(self):
        return {
            "amount": self.amount,
            "currency": self.currency,
            "receipt": self.receipt,
            "notes": self.notes
        }