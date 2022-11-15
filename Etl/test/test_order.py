from datetime import datetime
from entities.order import Order
from entities.customer import Customer
from entities.book import Book


def test_order():
    #Arrange
    customer_um = Customer(1, "Ana Paula")
    order_um = Order(1, customer_um, datetime.today())

    book = Book(1, "50 Tons da Vida","97-885-7480-817-8","Levi Dantas","Literatura brasileira",39.90)
    #Act

    order_um.purchased_book = book
    
    #Assert
    assert order_um.id == 1
    assert order_um.customer == customer_um
    assert order_um.purchased_book == book
