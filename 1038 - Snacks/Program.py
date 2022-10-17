from Menu import Menu
from MenuRepository import MenuRepository
from UserInterface import UserInterface

menu_repository = MenuRepository()
menu_repository.set_menu_item(Menu(1, "Hot dog", 4.00))
menu_repository.set_menu_item(Menu(2, "X-Salada", 4.50))
menu_repository.set_menu_item(Menu(3, "X-Bacon", 5.00))
menu_repository.set_menu_item(Menu(4, "Toast", 2.00))
menu_repository.set_menu_item(Menu(5, "Refrigerant", 1.50))

print(menu_repository)

user_interface = UserInterface(menu_repository)

while user_interface.get_interaction():
    pass
