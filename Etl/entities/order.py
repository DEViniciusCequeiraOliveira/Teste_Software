
from entities.book import Book
from entities.customer import Customer
from datetime import date

class Order:
    def __init__(self, id: int, customer: Customer, date_order: date) -> None:
        self.id = id
        self.customer = customer
        self.date_order = date_order
        self.purchased_book: Book
        self.total_price: float = 0
