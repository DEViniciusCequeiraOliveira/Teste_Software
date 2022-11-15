from entities.book import Book

def test_book():
    # Arrange
    livro1 = Book(1,"50 Tons da Vida","97-885-7480-817-8","Cleber Mario", "Literatura brasileira",39.90)
    livro2 = Book(2,"Capitães da Areia", "97-885-3591-169-5","Jorge Amado", "Romance",21.90)
    # Act
    livro1.author = "Levi Dantas"
    livro1.stock = 777
    livro2.author = "Jorge Amado"
    livro2.category = "Romance"
    livro2.stock = 5826
        
    # Assert
    assert livro1.id == 1
    assert livro1.name == "50 Tons da Vida"
    assert livro1.author == "Levi Dantas"
    assert livro1.author != "Cleber Mario"
    assert livro1.category == "Literatura brasileira"
    assert livro1.isbn == "97-885-7480-817-8"
    assert livro1.price == 39.90
    assert livro1.stock == 777

    assert livro2.id == 2
    assert livro2.name == "Capitães da Areia"
    assert livro2.author != "Ronaldinho"
    assert livro2.author == "Jorge Amado"
    assert livro2.category != "Ação"
    assert livro2.isbn == "97-885-3591-169-5"
    assert livro2.price == 21.90
    assert livro2.stock == 5826
    

