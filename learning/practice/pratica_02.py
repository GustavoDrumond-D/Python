import os

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('Insira um numero: '));

# o operdador % retorna o resto da divisão, neste caso, se o resto for 0, retorna par, caso contrario, retorna impar
if numero % 2 == 0:
    print(f'O numero {numero} é par.');
else:
    print(f'O numero {numero} é impar.');




# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Insira sua idade: '));

if idade <= 12:
    print('criança');
elif idade >= 13 and idade <= 18:
    print('adolescente');
elif idade > 18:
    print('adulto');
else:
    print('dados invalidos')



# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

nome = input('Insira seu nome:');
senha = input('Insira sua senha:');

nome_esperado = 'Gustavo';
senha_esperada = '1234';

if nome == nome_esperado and senha == senha_esperada:
    print('Acesso permitido');
else:
    print('Acesso negado');



# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

x = int(input('Insira o valor de x:'));
y = int(input('Insira o valor de y:'));

if x > 0 and y > 0:
    print('Primeiro Quadrante');
elif x < 0 and y > 0:
    print('Segundo Quadrante');
elif x < 0 and y < 0:
    print('Terceiro Quadrante');
elif x > 0 and y < 0:
    print('Quarto Quadrante');
elif x == 0 and y == 0:
    print('Origem');
else:
    print('Eixo ou origem');