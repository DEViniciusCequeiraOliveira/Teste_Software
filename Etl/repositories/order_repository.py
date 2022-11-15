from entities.order import Order

class OrderRepository:
    def __init__(self, ) -> None:
        self.list_orders: list[Order] = []
