import os;
# 1.Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
# 2.Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
# 3.Verifique o valor inicial do atributostatus para a instância restaurante_praca e exiba uma mensagem informando se o restaurante estástatus ou instatusstatus.
# 4.Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# 5.Altere o valor do atributo nome para 'Bistrô'.
# 6.Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# 7.Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# 8.Mude o estado da instância restaurante_pizza parastatus.
# 9.Imprima no console o nome e a categoria da instância restaurante_praca.

class Restaurante:
    def __init__(self, nome, categoria, status):
        self.nome = nome
        self.categoria = categoria
        self.status = status

restaurante_praca = Restaurante('Restaurante Praca', 'Italiana', False)
print(f'Nome: {restaurante_praca.nome} \nCategoria: {restaurante_praca.categoria} \nstatus: {restaurante_praca.status} \n')
input('Pressione qualquer tecla para continuar... ');
os.system('cls');

''''''

nome_restaurante = restaurante_praca.nome;

''''''

if restaurante_praca.status == 'True':
    print('Restaurante ativo');
else:
    print('Restaurante inativo');
input('Pressione qualquer tecla para continuar... ');
os.system('cls');

''''''

categoria = restaurante_praca.categoria;

''''''

print(f'Nome Restaurante: {restaurante_praca.nome}')
restaurante_praca.nome = 'Bistrô';
print(f'Nome Restaurante: {restaurante_praca.nome}')
input('Pressione qualquer tecla para continuar... ');
os.system('cls');

''''''

restaurante_pizza = Restaurante('Pizza Place', 'Fast Food', False);

''''''

if restaurante_pizza.categoria == 'Fast Food':
    print('Restaurante Fast Food');
else:
    print('Restaurante nao Fast Food');
input('Pressione qualquer tecla para continuar... ');
os.system('cls');

''''''

print(f'Status: {restaurante_pizza.status}')
restaurante_pizza.status = True;
print(f'Status: {restaurante_pizza.status}')
input('Pressione qualquer tecla para continuar... ');
os.system('cls');

''''''

print(f'Nome: {restaurante_praca.nome} \nCategoria: {restaurante_praca.categoria} \nstatus: {restaurante_praca.status} \n')
