from pratica_08 import ModelLivro

livro04 = ModelLivro('O Hobbit', 'J. R. R. Tolkien', 1937);
print(f'Estado do livro: {livro04._disponivel}');
livro04.emprestar();
print(f'Estado do livro: {livro04._disponivel}');

livros_disponiveis = ModelLivro.verificar_disponibilidade(1954);
print(f'Livros disponíveis: {livros_disponiveis}');


livro05 = ModelLivro('O Senhor dos Aneis', 'J. R. R. Tolkien', 1954);
livro06 = ModelLivro('Dom Quixote', 'Miguel de Cervantes', 1605);
livro07 = ModelLivro('O Hobbit', 'J. R. R. Tolkien', 1937);

ModelLivro.livros = [livro04, livro05, livro06, livro07];

for livro in ModelLivro.livros:
    print(livro);