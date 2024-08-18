from enum import Enum


class OrderStatus(Enum):
    """
    Restricts usage to allowed options.
    """
    pending = 'pending'
    executed = 'executed'
    canceled = 'canceled'


class Order:
    """
    Sample order model.
    """
    def __init__(self, item: str, quantity: int):
        self.item = item
        self.quantity = quantity
