from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order
from UserInterface import UserInterface



def test_check_total_price():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    user_interface = UserInterface(menu_repository)

    # Act
    menu_repository.set_menu_item(menu1)

    # Assert
    total70 = user_interface.get_total_price(Order(1, 7))
    total_null = user_interface.get_total_price(Order(2, 5))

    assert total70 == 70
    assert total_null is None

def test_check_user_input(monkeypatch):
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    user_interface = UserInterface(menu_repository)
    menu1 = Menu(1, "Test 1", 5)

    # Act
    menu_repository.set_menu_item(menu1)
    monkeypatch.setattr('builtins.input', lambda _: "1 4")
    order = user_interface.get_user_input()

    # Assert
    assert Order(1, 4) == order


