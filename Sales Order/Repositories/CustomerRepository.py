from Entities.Customer import Customer


class CustomerRepository:

    def __init__(self) -> None:
        self.list_customers: list[Customer] = []

    def append_customer(self, customer: Customer) -> None:
        self.list_customers.append(customer)

    def get_customers(self) -> list[Customer]:
        return self.list_customers
