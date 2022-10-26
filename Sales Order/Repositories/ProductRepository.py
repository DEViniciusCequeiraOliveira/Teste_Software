from Entities.Product import Product


class ProductRepository:

    def __init__(self) -> None:
        self.list_products: list[Product] = []

    def append_product(self, product: Product) -> None:
        self.list_products.append(product)

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20}\n"
        str_products = formatText.format("Id", "Description", "Price", "Stock")

        for item in self.list_products:
            str_products += formatText.format(item.id, item.description, item.price, item.stock)

        return str_products
