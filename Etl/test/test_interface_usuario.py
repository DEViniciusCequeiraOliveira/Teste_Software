from datetime import datetime
from entities.book import Book
from entities.order import Order
from entities.customer import Customer
from interface_usuario import InterfaceUsuario
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository


def test_register_customer(monkeypatch):
    customer_repository = CustomerRepository()
    book_repository = BookRepository()
    order_repository = OrderRepository()
    interface_usuario = InterfaceUsuario(customer_repository, book_repository, order_repository)

    customer_repository.list_customers.append(Customer(1, "Robert"))

    monkeypatch.setattr('builtins.input', lambda _: 1)
    result_customer_already_registered = interface_usuario.register_customer()

    inputs = iter([2, "Carlinhos"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result_customer_registered = interface_usuario.register_customer()

    customer_carlinhos = customer_repository.get_customer(2)

    assert result_customer_already_registered == "Cliente já cadastrado!!!"
    assert result_customer_registered == "Cliente cadastrado com sucesso!"
    assert customer_carlinhos.id == 2
    assert customer_carlinhos.name == "Carlinhos"


def test_validate_sell():
    customer_repository = CustomerRepository()
    book_repository = BookRepository()
    order_repository = OrderRepository()
    interface_usuario = InterfaceUsuario(customer_repository, book_repository, order_repository)

    book_one = Book(1, "Um bom livro", "564786756434", "Carlos Augusto", "Uma Aventura", 42.8)
    book_two = Book(2, "A Lua do Oriente e Outras Luas", "978-65-5580-076-0", "Christina Stephano de Queiroz",
                    "Ilustrado, Literatura brasileira", 78.0)
    book_three = Book(3, "A Um - Poemas", "85-85851-40-6", "Robert Creeley", "Poesia, Literatura estrangeira", -7.5)
    book_four = Book(-1, "A Voz e o Tempo - 3a ed.", "978-65-5580-016-6", "Roberto Gambini",
                     "Ilustrado, Psicanálise e Psicologia", 72.0)
    book_two.stock = -777
    book_repository.list_books = [book_one, book_two, book_three, book_four]

    customer_cleber = Customer(1, "Cleber")
    customer_repository.list_customers.append(customer_cleber)

    order_exits = Order(1, customer_cleber, datetime.today())
    order_repository.list_orders.append(order_exits)

    result_order_exits = interface_usuario.validate_sell(order_exits.id, customer_cleber.id, book_one)
    result_verif_if_customer_exists = interface_usuario.validate_sell(2, 777, book_one)
    result_stock_valid = interface_usuario.validate_sell(2, customer_cleber.id, book_two)
    result_verif_if_book_cost_more_zero = interface_usuario.validate_sell(2, customer_cleber.id, book_three)
    result_verif_id_book = interface_usuario.validate_sell(2, customer_cleber.id, book_four)

    assert result_order_exits == "Pedido já existe"
    assert result_verif_if_customer_exists == "Cliente não cadastrado"
    assert result_stock_valid == "Livro sem estoque"
    assert result_verif_if_book_cost_more_zero == "Livro com preço invalido"
    assert result_verif_id_book == "Livro não cadastrado"


def test_sell(monkeypatch):
    customer_repository = CustomerRepository()
    book_repository = BookRepository()
    order_repository = OrderRepository()
    interface_usuario = InterfaceUsuario(customer_repository, book_repository, order_repository)

    book_one = Book(2, "Um livro bem ruim", "487898423", "Richarlison Pombo", "Broco mermo", 150)
    book_repository.list_books.append(book_one)

    customer_pompo = Customer(2, "pombo")
    customer_repository.list_customers.append(customer_pompo)

    inputs = iter([1, customer_pompo.id, book_one.id])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result_sell_ok = interface_usuario.sell()

    inputs = iter([1, 777, 777])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result_sell_fail = interface_usuario.sell()

    assert result_sell_ok == "Pedido cadastrado com sucesso!"
    assert result_sell_fail == "Erro durante a compra, tente novamente mais tarde"
