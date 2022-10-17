from MenuRepository import MenuRepository
from Order import Order


class UserInterface:
    def __init__(self, menu_repository: MenuRepository) -> None:
        self.menu_repository = menu_repository

    def get_user_input(self) -> Order:
        result = input(
            "Inform code (valid) included in menu and quantity, separated by space to buy snacks: ").split()
        return Order(int(result[0]), int(result[1]))

    def get_total_price(self, order: Order) -> float:
        return self.menu_repository.get_total_price(order)

    def get_interaction(self) -> bool:
        order = self.get_user_input()

        if (self.menu_repository.check_if_itens_exists(order) == False):
            print("Invalid code!")
            return False

        print(f"Total: $ {self.get_total_price(order)}")
        return True
