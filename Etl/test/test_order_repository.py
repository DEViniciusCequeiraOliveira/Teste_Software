from repositories.order_repository import OrderRepository;

def test_order_repository():
    order_repository = OrderRepository()
    assert order_repository.list_orders == [] 