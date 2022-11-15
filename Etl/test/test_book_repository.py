from entities.book import Book
from repositories.book_repository import BookRepository


def test_verif_if_book_exists():
  book_repository = BookRepository()
  book = Book(1,"Flutter", "a", "eu", "ensino", 15)
  result = book_repository.verif_if_book_exists(book.id)

  assert result == True

def test_get_book():
    book_repository = BookRepository()
    book = Book(1,"Flutter", "a", "eu", "ensino", 15)
    result = book_repository.get_book(book.id)
    # SECOND(SEGUNDO) TEST(TESTE) 
    book2 = Book(1,"java", "a", "eu", "ensino", 15)
    result2 = book_repository.get_book(book.id)

    assert result == book
    assert result2 != book2



