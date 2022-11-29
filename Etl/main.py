from interface_usuario import InterfaceUsuario
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from service.open_book_csv import OpenBookCsv

customer_repository = CustomerRepository()
order_repository = OrderRepository()
book_repository = BookRepository()
interface_usuario = InterfaceUsuario(customer_repository, book_repository, order_repository)

open_book_csv = OpenBookCsv(book_repository)
open_book_csv.loading_book()

while True:
    menu_option = interface_usuario.principal_menu()
    if (menu_option == 0):
        break

    print("\n")

    if menu_option == 1:
        print(interface_usuario.register_customer())
    if menu_option == 2:
        print(interface_usuario.sell())
    if menu_option == 3:
        interface_usuario.output_usuario_order()
    if menu_option == 4:
        interface_usuario.output_relatorio_customer()
    if menu_option == 5:
        interface_usuario.output_relatorio_book()


