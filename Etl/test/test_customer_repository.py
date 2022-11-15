from repositories.customer_repository import CustomerRepository
from entities.customer import Customer


def test_verif_if_customer_exists():
  custom_repository = CustomerRepository()
  custom_repository.list_customers.append(Customer(1, "Ana"))
  result = custom_repository.verif_if_customer_exists(1)
  
  assert result == True


def test_get_customer():
  custom_repository = CustomerRepository()
  cliente_ana = Customer(1, "Ana")

  custom_repository.list_customers.append(cliente_ana)
  result = custom_repository.get_customer(1)

  assert result == cliente_ana
