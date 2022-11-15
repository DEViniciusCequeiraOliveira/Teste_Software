class Book:
    def __init__(self, id: int, name: str, isbn: str, author: str, category: str, price: float) -> None:
        self.id = id
        self.name = name
        self.isbn = isbn
        self.author = author
        self.category = category
        self.price = price
        self.stock: int = 1

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return self.id == other.id and self.name == other.name and self.isbn == other.isbn and self.author == other.author and self.category == other.category and self.price == other.price and self.stock == other.stock
        return False
