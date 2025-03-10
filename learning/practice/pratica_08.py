# 1.Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

# 2.Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

# 3.Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

# 4.Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

# 5.Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# 6.No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

# 7.No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

# 8.Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

class ModelLivro:
    def __init__ (this, titulo, autor, ano_publicacao):
        this._titulo = titulo;
        this._autor = autor;
        this._ano_publicacao = ano_publicacao;
        this._disponivel = True;

    def __str__ (this):
        return f'Titulo: {this._titulo.ljust(20)} | Autor: {this._autor.ljust(20)} | Ano de publicação: {this._ano_publicacao}';

    def emprestar (this):
        this._disponivel = False;

    @staticmethod
    def verificar_disponibilidade (ano):
        livros_disponiveis = [livro for livro in ModelLivro.livros if livro._ano_publicacao == ano and livro._disponivel];
        return livros_disponiveis

livro01 = ModelLivro('Dom Quixote', 'Miguel de Cervantes', 1605);
livro02 = ModelLivro('O Senhor dos Aneis', 'J. R. R. Tolkien', 1954);

print(livro01);
print(livro02);

livro03 = ModelLivro('O Hobbit', 'J. R. R. Tolkien', 1937);
print(f'Estado do livro: {livro03._disponivel}');
livro03.emprestar();
print(f'Estado do livro: {livro03._disponivel}');

ModelLivro.livros = [livro01, livro02, livro03];

