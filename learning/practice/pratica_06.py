import os;
# 1.Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
# 2.Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# 3.Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# 4.Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# 5.Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class ModelCarro: 
    def __init__(this, modelo, cor, ano):
        this.modelo = modelo
        this.cor = cor
        this.ano = ano

carro = ModelCarro('Ferrari', 'Vermelho', 2022)
print(f'Modelo: {carro.modelo} | Cor: {carro.cor} | Ano: {carro.ano}')
input('Pressione qualquer tecla para continuar... ');
os.system('cls');


class ModelRestaurante:
    def __init__(this, nome, categoria, ativo, endereco, telefone):
        this.nome = nome
        this.categoria = categoria
        this.ativo = ativo
        this.endereco = endereco
        this.telefone = telefone

    def __str__(this):
        return f'Restaurante: {this.nome} | Categoria: {this.categoria} | Ativo: {this.ativo} | Endereco: {this.endereco} | Telefone: {this.telefone}'


#neste caso, o construtor recebe 5 parametros e os atribui aos respectivos atributos
restaurante = ModelRestaurante('Test', 'carnes', False, 'Rua 1', '12345678')
print(f'Restaurante: {restaurante.nome} | Categoria: {restaurante.categoria} | Ativo: {restaurante.ativo} | Endereco: {restaurante.endereco} | Telefone: {restaurante.telefone}')
input('Pressione qualquer tecla para continuar... ');
os.system('cls');


# diferente do construtor acima, neste caso, o construtor recebe 3 parametros e os atribui aos respectivos atributos de outra forma, atraves de um dicionario
novo_restaurante = ModelRestaurante(nome='Teste', categoria='carnes', ativo=False, endereco='Rua 1', telefone='12345678')
print(novo_restaurante)
input('Pressione qualquer tecla para continuar... ');
os.system('cls');

class ModelCliente:
    def __init__(this, nome, telefone, email,):
        this.nome = nome
        this.telefone = telefone
        this.email = email

cliente = ModelCliente(nome='Teste', telefone='12345678', email='qYH4d@example.com')
input('Pressione qualquer tecla para continuar... ');
os.system('cls');