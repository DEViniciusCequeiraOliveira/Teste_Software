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

    assert result_true == book_um
    assert result_false != book_dois



