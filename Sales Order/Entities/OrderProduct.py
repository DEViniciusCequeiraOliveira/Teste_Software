from Entities.Product import Product


class OrderProduct:
    def __init__(self) -> None:
        self.value_item: float
        self.quantity: int
        self.product: Product

    def add_product(self, product: Product, quantity: int) -> str:
        if (not product.check_stock(quantity)):
            return f"Product '{product.description}' without stock."

        self.process_product(product, quantity)
        return "Product add successfully!"

    def process_product(self, product: Product, quantity: int) -> None:
        self.product = product
        product.down_stock(quantity)
        self.value_item = product.price * quantity
        self.quantity = quantity
