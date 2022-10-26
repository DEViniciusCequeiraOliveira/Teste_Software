from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository


def test_new_order_with_product_total_price():
    # Arrange
    customer1 = Customer(1, "Jefté")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Milk", 50, 10)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 5)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert order.total_price == 250

def test_new_order_without_product():
    # Arrange
    customer1 = Customer(1, "Jefté")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Milk", 50, 10)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 15)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert order.total_price == 0

def test_process_product():
    order_product = OrderProduct()
    product1 = Product(1, "Milk", 12.80, 100)
    product2 = Product(2, "Apple", 3.75, 750)

    order_product.add_product(product1, 15)

    assert order_product.product == product1
    assert order_product.product != product2
    assert order_product.value_item == 192
    assert order_product.quantity == 15

def test_integrated_down_stock():
    order_product = OrderProduct()
    product1 = Product(1, "Milk", 7.50, 10)

    order_product.add_product(product1, 5)

    assert order_product.quantity == 5

def test_down_stock():
    product1 = Product(1, "Sugar", 3.77, 10)

    product1.down_stock(7)

    assert product1.stock == 3


