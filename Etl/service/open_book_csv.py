from entities.book import Book
from repositories.book_repository import BookRepository
from service.format_price import FormatPrice


class OpenBookCsv:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    file_book = list(open("books.csv", "r", encoding="utf-8"))

    def loading_book(self):
        for book in self.file_book[1:]:
            list_book = book.split(";")
            book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                        list_book[4], FormatPrice().format_str_price_to_float(list_book[5]))
            self.book_repository.list_books.append(book)
