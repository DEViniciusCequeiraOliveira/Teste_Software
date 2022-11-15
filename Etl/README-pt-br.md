- [1. Introdução](#1-introdução)
- [2. Criar uma classe para representar a entidade Livros:](#2-criar-uma-classe-para-representar-a-entidade-livros)
- [3. Criar uma classe para representar a entidade Cliente](#3-criar-uma-classe-para-representar-a-entidade-cliente)
- [4. Criar uma classe para representar a entidade Pedido](#4-criar-uma-classe-para-representar-a-entidade-pedido)
- [5. Importar o arquivo .CSV e para CADA LINHA (DADO) do .CSV instanciar um objeto dentro de uma lista:](#5-importar-o-arquivo-csv-e-para-cada-linha-dado-do-csv-instanciar-um-objeto-dentro-de-uma-lista)
- [6. O sistema ao iniciar SEMPRE deve importar o arquivo CSV.](#6-o-sistema-ao-iniciar-sempre-deve-importar-o-arquivo-csv)
- [7. Criar uma classe para representar as interações com o usuário.](#7-criar-uma-classe-para-representar-as-interações-com-o-usuário)
- [8. O sistema deve conter as seguintes validações, lembrando que cada validação dessa deve ter sua respectiva função e seu respectivo teste unitário/integração.](#8-o-sistema-deve-conter-as-seguintes-validações-lembrando-que-cada-validação-dessa-deve-ter-sua-respectiva-função-e-seu-respectivo-teste-unitáriointegração)
- [9. Formato dos relatórios](#9-formato-dos-relatórios)

# 1. Introdução

- A empresa Livraria Digital precisa de um sistema em Python para ler um arquivo .CSV para inicializar seu sistema de Venda de Livros.

- O arquivo tem a seguinte estrutura:

```
Titulo;Isbn;Autor;Assunto;Valor;
50 Tons da Vida;97-885-7480-817-8;Roberto Livianu;Literatura brasileira, Crônicas;R$ 39,90;
A Lua do Oriente e Outras Luas;978-65-5580-076-0;Christina Stephano de Queiroz;Ilustrado, Literatura brasileira, Crítica literária, Poesia, História, Biografia;R$ 78,00;
A Um - Poemas;85-85851-40-6;Robert Creeley;Poesia, Literatura estrangeira, Bilíngue, Ilustrado, Tradução;R$ 49,00;
(...)
```

# 2. Criar uma classe para representar a entidade Livros:

- Criar a classe para representar a manipulação/validação/operações da lista de Livros

# 3. Criar uma classe para representar a entidade Cliente

- Criar a classe para representar a manipulação/validação/operações da lista de Clientes

# 4. Criar uma classe para representar a entidade Pedido

- Criar a classe para representar a manipulação/validação/operações da lista de Pedidos

# 5. Importar o arquivo .CSV e para CADA LINHA (DADO) do .CSV instanciar um objeto dentro de uma lista:

- Criar uma classe para com a resposabilidade de importar o arquivo:

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

# 6. O sistema ao iniciar SEMPRE deve importar o arquivo CSV.

# 7. Criar uma classe para representar as interações com o usuário.

# 8. O sistema deve conter as seguintes validações, lembrando que cada validação dessa deve ter sua respectiva função e seu respectivo teste unitário/integração.

- Verificar se o estoque do livro foi baixado
- Não permitir inserir um código de cliente que já existe
- Não permitir inserir um código de pedido que já existe
- Não permitir vender um livro com valor zerado
- Não permitir fazer um pedido sem cliente
- Não permitir um pedido sem livro
- Só é permitido informar UM pedido no pedido
- Caso o formato do valor do esteja errado retornar 0
- Não permitir vender o mesmo livro novamente, pois a livraria só possui 1 estoque
- Verificar se o código do livro que está sendo vendido, existe, caso não exista aborta o pedido e volta para o menu

# 9. Formato dos relatórios

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