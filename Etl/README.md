- [1. Introduction](#1-introduction)
- [2. Create a class to represent the Books entity:](#2-create-a-class-to-represent-the-books-entity)
- [3. Create a class to represent the Customer entity](#3-create-a-class-to-represent-the-customer-entity)
- [4. Create a class to represent the Order entity](#4-create-a-class-to-represent-the-order-entity)
- [5. Import the .CSV file and for EACH LINE (DATA) of the .CSV instantiate an object inside a list:](#5-import-the-csv-file-and-for-each-line-data-of-the-csv-instantiate-an-object-inside-a-list)
- [6. The system when starting must ALWAYS import the CSV file.](#6-the-system-when-starting-must-always-import-the-csv-file)
- [7. Create a class to represent User Interactions.](#7-create-a-class-to-represent-user-interactions)
- [8. The system must contain the following validations, remembering that each validation must have its respective function and its respective unit/integration test.](#8-the-system-must-contain-the-following-validations-remembering-that-each-validation-must-have-its-respective-function-and-its-respective-unitintegration-test)
- [9. Format of reports](#9-format-of-reports)

# 1. Introduction

- The company Livraria Digital needs a system in Python to read a .CSV file to start its Book Sales system.

- The file has the following structure:

```
Titulo;Isbn;Autor;Assunto;Valor;
50 Tons da Vida;97-885-7480-817-8;Roberto Livianu;Literatura brasileira, Crônicas;R$ 39,90;
A Lua do Oriente e Outras Luas;978-65-5580-076-0;Christina Stephano de Queiroz;Ilustrado, Literatura brasileira, Crítica literária, Poesia, História, Biografia;R$ 78,00;
A Um - Poemas;85-85851-40-6;Robert Creeley;Poesia, Literatura estrangeira, Bilíngue, Ilustrado, Tradução;R$ 49,00;
(...)
```

# 2. Create a class to represent the Books entity:

- Create the class to represent the manipulation/validation/operations of the Book list.

# 3. Create a class to represent the Customer entity

- Create the class to represent the manipulation/validation/operations of the list of Customers.

# 4. Create a class to represent the Order entity

- Create the class to represent manipulation/validation/operations of the list of Orders.

# 5. Import the .CSV file and for EACH LINE (DATA) of the .CSV instantiate an object inside a list:

- Create a class for the responsibility of importing the file:

```
file_book = list(open("books.csv", "r", encoding="utf-8"))

list_books: list[Book] = []

def format_str_price_to_float(price: str) -> float:
    try:
        return float(price.replace("R$ ", "").replace(",", "."))
    except:
        return 0

for book in file_book[1:]:
    list_book = book.split(";")
    book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                list_book[4], format_str_price_to_float(list_book[5]))
    list_books.append(book)
```

# 6. The system when starting must ALWAYS import the CSV file.

# 7. Create a class to represent User Interactions.

# 8. The system must contain the following validations, remembering that each validation must have its respective function and its respective unit/integration test.

- Test option of menu.
- Check if menu options exists.
- Check if the book's stock has been downed.
- Do not allow entering a customer code that already exists.
- Do not allow entering an order code that already exists.
- Do not allow selling a book with zero price.
- Do not allow placing an order without a customer.
- Do not allow an order without a book.
- It is only allowed to inform ONE order in the order.
- If the format of the value of is wrong, return 0.
- Do not allow selling the same book again, as the bookstore only has 1 stock.
- Check if the code of the book being sold exists, if it does not exist, abort the order and return to the menu.

# 9. Format of reports

```
***** Relatório de clientes *****
Id         Customer
1          Maria
2          José


***** Relatório de livros cadastrados *****
Id         Ttítulo              Ttítulo              Ttítulo              Ttítulo              Ttítulo
1          50 Tons da Vida      50 Tons da Vida      50 Tons da Vida      50 Tons da Vida      50 Tons da Vida
2          A Lua do Oriente e Outras Luas A Lua do Oriente e Outras Luas A Lua do Oriente e Outras Luas A Lua do Oriente e Outras Luas A Lua do Oriente e Outras Luas
3          A Um - Poemas        A Um - Poemas        A Um - Poemas        A Um - Poemas        A Um - Poemas
4          A Voz e o Tempo - 3a ed. A Voz e o Tempo - 3a ed. A Voz e o Tempo - 3a ed. A Voz e o Tempo - 3a ed. A Voz e o Tempo - 3a ed.
5          A.S.A. - Associação dos Solitários Anônimos A.S.A. - Associação dos Solitários Anônimos A.S.A. - Associação dos Solitários Anônimos A.S.A. - Associação dos Solitários Anônimos A.S.A. - Associação dos Solitários Anônimos
6          Acústica Musical em Palavras e Sons, A Acústica Musical em Palavras e Sons, A Acústica Musical em Palavras e Sons, A Acústica Musical em Palavras e Sons, A Acústica Musical em Palavras e Sons, A
7          Adeus Penderama e Outros Escritos Adeus Penderama e Outros Escritos Adeus Penderama e Outros Escritos Adeus Penderama e Outros Escritos Adeus Penderama e Outros Escritos


***** Relatório de pedidos *****
Código do Pedido: 1
Cliente: teste
Data do pedido: 2022-10-30
Livro escolhido: Afeto Autoritário, O - Televisão, Ética e Democracia

Código do Pedido: 1
Cliente: teste
Data do pedido: 2022-10-30
Livro escolhido: Afeto Autoritário, O - Televisão, Ética e Democracia

Código do Pedido: 1
Cliente: teste
Data do pedido: 2022-10-30
Livro escolhido: Afeto Autoritário, O - Televisão, Ética e Democracia
```
