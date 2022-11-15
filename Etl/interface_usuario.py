from datetime import date
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository


class InterfaceUsuario:
    def __init__(self, customer_repository : CustomerRepository, book_repository : BookRepository, order_repository : OrderRepository) -> None:
        self.customer_repository = customer_repository
        self.book_repository = book_repository
        self.order_repository = order_repository
        

    def register_customer(self):
        id = int(input("Informe o código do cliente: "))
        nome = input("Informe o nome do cliente: ")
        customer = Customer(id, nome)
        self.customer_repository.list_customers.append(customer)
        print("Cliente cadastrado com sucesso!")

    def sell(self):
        id = int(input("Informe o código do pedido: "))
        customer_id = int(input("Informe o código do cliente: "))
        today = date.today()
        if (not self.customer_repository.verif_if_customer_exists(customer_id)):
            print("Cliente não existe!")
            

        customer = self.customer_repository.get_customer(customer_id)
        book_id = int(input("Informe o código do livro: "))

        if (not self.book_repository.verif_if_book_exists(book_id)):
            print("Livro não existe!")
            

        book = self.book_repository.get_book(book_id)
        order = Order(id, customer, today)
        order.purchased_book = book

        self.order_repository.list_orders.append(order)
        print("Pedido cadastrado com sucesso!")

    def output_usuario_order(self):
        print("\n***** Relatório de pedidos *****\n")
        for order in self.order_repository.list_orders:
            print(f"Código do Pedido: {order.id}")
            print(f"Cliente: {order.customer.name}")
            print(f"Data do pedido: {order.date_order}")
            print(f"Livro escolhido: {order.purchased_book.name} \n")
    
    def output_relatorio_customer(self):
        formatText = "{0:<10} {1:<20}\n"
        menu = ("\n***** Relatório de clientes *****\n")
        menu += formatText.format("Id", "Cliente")

        for customer in self.customer_repository.list_customers:
            menu += formatText.format(customer.id, customer.name)
        print(menu)

    def output_relatorio_book(self):
        formatText = "{0:<10} {1:<20} {1:<20} {1:<20} {1:<20} {1:<20}\n"
        menu = ("\n***** Relatório de livros cadastrados *****\n")
        menu += formatText.format("Id", "Ttítulo", "ISBN",
                                  "Autor", "Assunto", "Valor", "Estoque")
        for book in self.book_repository.list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                      book.author, book.category, book.price, book.stock)
        print(menu)

    def principal_menu(self) -> int:
        try:
            print("1 - Cadastrar cliente")
            print("2 - Fazer pedido")
            print("3 - Relatório de Pedidos")
            print("4 - Relatório de Clientes")
            print("5 - Relatório de Livros")
            print("0 - Sair")
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0