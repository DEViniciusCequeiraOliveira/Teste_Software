from datetime import datetime

from Entities.Customer import Customer
from Entities.OrderProduct import OrderProduct


class Order:
    def __init__(self, id: int, customer: Customer, date: datetime) -> None:
        self.id = id
        self.customer = customer
        self.date = date
        self.order_products: list[OrderProduct] = []
        self.total_price: float = 0

    def add_order_product(self, order_item: OrderProduct) -> None:
        if (hasattr(order_item, "product")):
            self.order_products.append(order_item)

    def update_total_price(self) -> None:
        for order_product in self.order_products:
            self.total_price += order_product.value_item

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20} {4:<20}\n"
        str_products = f"Customer: {self.customer.name} Total Price: {self.total_price}\n"

        str_products += formatText.format(
            "Id", "Description", "Price", "Quantity", "Total Price")
        
        for order_product in self.order_products:
            str_products += formatText.format(order_product.product.id,
                                              order_product.product.description, order_product.product.price, order_product.quantity, order_product.value_item)

        return str_products
