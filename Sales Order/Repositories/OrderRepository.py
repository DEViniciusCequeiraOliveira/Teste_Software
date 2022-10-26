from Entities.Order import Order


class OrderRepository:
    def __init__(self) -> None:
        self.list_orders: list[Order] = []

    def add_order(self, order: Order) -> None:
        self.list_orders.append(order)
