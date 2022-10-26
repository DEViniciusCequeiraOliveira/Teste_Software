class Product:
    def __init__(self, id: int, description: str, price: float, stock: int) -> None:
        self.id = id
        self.description = description
        self.price = price
        self.stock = stock

    def check_stock(self, quantity) -> bool:
        if (self.stock > quantity):
            return True
        else:
            return False

    def down_stock(self, quantity) -> None:
        self.stock -= quantity
