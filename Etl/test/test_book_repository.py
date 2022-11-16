from repositories.book_repository import BookRepository
from entities.book import Book


def test_verif_if_book_exists():
  book_repository = BookRepository()
  book_um = Book(1,"Flutter", "a", "eu", "ensino", 15)
  book_dois = Book(2, "Pytest com alegria", "123135456", "Carlos", "Ação", 142.85)

  book_repository.list_books.append(book_dois)

  result_false = book_repository.verif_if_book_exists(book_um.id)
  result_true = book_repository.verif_if_book_exists(book_dois.id)

  assert result_false == False
  assert result_true == True

def test_get_book():
    book_repository = BookRepository()
    book_um = Book(1,"Flutter", "4864648468468", "eu", "ensino", 15)
    book_dois = Book(2,"Java por amor <3", "46548678646", "eu", "ensino", 15)

    book_repository.list_books.append(book_um)

    result_true = book_repository.get_book(book_um.id)
    result_false = book_repository.get_book(book_dois.id)
    result_not_found = book_repository.get_book(777)

    assert result_true == book_um
    assert result_false != book_dois
    assert result_not_found.id == -1

def test_down_stock():
    book_repository = BookRepository()
    book_um = Book(1,"Flutter", "4864648468468", "eu", "ensino", 15)
    book_dois = Book(2,"Java por amor <3", "46548678646", "eu", "ensino", 15)

    book_repository.list_books.append(book_um)
    book_repository.down_stock(book_um.id)

    assert book_um.stock == 0
    assert book_dois.stock == 1

def test_get_stock():
    book_repository = BookRepository()
    book_um = Book(1,"Flutter", "4864648468468", "eu", "ensino", 15)
    book_dois = Book(2,"Java por amor <3", "46548678646", "eu", "ensino", 15)
    book_repository.list_books.append(book_um)

    book_repository.down_stock(book_um.id)
    stock_book_um = book_repository.get_stock(book_um.id)

    stock_book_dois = book_repository.get_stock(book_dois)
    assert stock_book_um == 0
    assert stock_book_dois == 1

def verif_if_book_cost_more_zero():
    book_repository = BookRepository()
    book_um = Book(1,"Flutter", "4864648468468", "eu", "ensino", 0)
    book_dois = Book(2,"Java por amor <3", "46548678646", "eu", "ensino", 15)

    result_false = book_repository.verif_if_book_cost_more_zero(book_um.id)
    result_true = book_repository.verif_if_book_cost_more_zero(book_dois)

    assert result_false == False
    assert result_true == True


