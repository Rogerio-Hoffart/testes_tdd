# Definindo a classe pai Item
class Item:
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao


# Criando subclasses Livro, Revista e DVD que herdam da classe pai Item
class Livro(Item):
    def __init__(self, titulo, autor, data_publicacao, numero_de_paginas):
        super().__init__(titulo, autor, data_publicacao)
        self.numero_de_paginas = numero_de_paginas

    def __str__(self):
        return  f'Título: {self.titulo}, Autor: {self.autor}, Data de publicação: {self.data_publicacao}, Número de páginas: {self.numero_de_paginas}'

class Revista(Item):
    def __init__(self, titulo, autor, data_publicacao, numero_edicao):
        super().__init__(titulo, autor, data_publicacao)
        self.numero_edicao = numero_edicao

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Data de publicação: {self.data_publicacao}, Número da edição: {self.numero_edicao}'

class DVD(Item):
    def __init__(self, titulo, autor, data_publicacao, duracao):
        super().__init__(titulo, autor, data_publicacao)
        self.duracao = duracao

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Data de publicação: {self.data_publicacao}, Duração: {self.duracao} minutos'

# Criando uma classe Biblioteca que guarda uma lista de itens
class Biblioteca:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        for item in self.itens:
            print(item)

# Usando a biblioteca
biblioteca = Biblioteca()
livro = Livro('Aprendendo Python', 'Mark Lutz', '01/01/2010', 300)
revista = Revista('Revista de Programação', 'Editora Abril', '01/01/2021', 50)
dvd = DVD('Filme A', 'Diretor A', '01/01/2015', 120)
biblioteca.adicionar_item(livro)
biblioteca.adicionar_item(revista)
biblioteca.adicionar_item(dvd)
biblioteca.listar_itens()
