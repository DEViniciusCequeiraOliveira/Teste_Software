from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.OrderRepository import OrderRepository
from Repositories.ProductRepository import ProductRepository

customer1 = Customer(1, "Jefté")
customer2 = Customer(2, "João")
customer3 = Customer(3, "Maria")
customer4 = Customer(4, "José")

customer_repository = CustomerRepository()
customer_repository.append_customer(customer1)
customer_repository.append_customer(customer2)
customer_repository.append_customer(customer3)
customer_repository.append_customer(customer4)

product1 = Product(1, "Milk", 8.78, 2)
product2 = Product(2, "Bean", 11.00, 11)
product3 = Product(3, "Rice", 10.23, 9)
product4 = Product(4, "Noodle", 5.98, 6)

product_repository = ProductRepository()
product_repository.append_product(product1)
product_repository.append_product(product2)
product_repository.append_product(product3)
product_repository.append_product(product4)


# order_repository = OrderRepository()

order = Order(1, customer3, datetime.today)
order_product1 = OrderProduct()
order_product2 = OrderProduct()
print(order_product1.add_product(product2, 5))
print(order_product2.add_product(product3, 5))
order.add_order_product(order_product1)
order.add_order_product(order_product2)
order.update_total_price()

print("\n** Report order **")
print(order)


print("\n** Report products **")
print(product_repository)
