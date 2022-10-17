class Menu:
    menu_itens = []

    def __init__(self, code: int, name: str, price: float) -> None:
        self.code = code
        self.name = name
        self.price = price
