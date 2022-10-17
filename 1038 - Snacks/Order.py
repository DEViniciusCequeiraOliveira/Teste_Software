class Order:
    def __init__(self, code: int, quantity: int) -> None:
        self.code = code
        self.quantity = quantity

    def __eq__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        return self.code == other.code and self.quantity == other.quantity