from Menu import Menu
from Order import Order


class MenuRepository:
    menu_itens: Menu = []

    def __init__(self) -> None:
        pass

    def set_menu_item(self, menu: Menu) -> None:
        self.menu_itens.append(menu)

    def check_if_itens_exists(self, order: Order) -> bool:
        for item in self.menu_itens:
            if (order.code == item.code):
                return True

        return False

    def get_total_price(self, order: Order) -> float:
        for item in self.menu_itens:
            if (order.code == item.code):
                return item.price * order.quantity

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20}\n"
        menu = formatText.format("Code", "Name", "Price")

        for item in self.menu_itens:
            menu += formatText.format(item.code, item.name, f"$ {item.price}")

        return menu
