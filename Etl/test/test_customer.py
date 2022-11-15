from entities.customer import Customer

def test_customer():
    customer_fernando = Customer(1, "Fernando")
    customer_claudio = Customer(2, "Caludio")

    customer_claudio.name = "Claudio"

    assert customer_fernando.id == 1
    assert customer_fernando.name == "Fernando"
    assert customer_claudio.id == 2
    assert customer_claudio.name == "Claudio"