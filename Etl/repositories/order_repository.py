from entities.order import Order

class OrderRepository:
    def __init__(self, ) -> None:
        self.list_orders: list[Order] = []

    def verif_if_order_exists(self, id):
        for order in self.list_orders:
            if order.id == id:
                return True
        return False