# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
lista_de_nomes = ['Felipe', 'Jose', 'Julia', 'Maria'];
lista_de_anos = [2005, 2025];



# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for numero in lista_de_numeros:
    print(numero);



# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_de_numeros_impares = 0;

for numero in lista_de_numeros:
    if numero % 2 != 0:
        soma_de_numeros_impares += numero;
        print(f'Valor atual da lista: {soma_de_numeros_impares}');




# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
# range em python retorna uma sequencia de numeros, neste caso, de 10 a 1, a sintexe é a seguinte :range(inicio, fim, passo)
for numero in range(10, 0, -1):
    print(numero);


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero_escolhido = int(input('Insira um numero: '));
for numero in range(0, 11):
    print(f'{numero_escolhido} x {numero} = {numero_escolhido * numero}');

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
soma_da_lista = 0;
try:
    for numeros in lista_de_numeros:
        
        print(f'Valor atual da lista: {soma_da_lista}');
        soma_da_lista += numeros;
        print(f'Soma da lista: {soma_da_lista}');
except Exception as e:
    print(f'Erro: {e}');

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
soma_de_valores = 0;

try:
    for numeros in lista_de_numeros:
        soma_de_valores += numeros;
    # len retorna o tamanho da lista
    media = soma_de_valores/len(lista_de_numeros);
    print(f'Media: {media}');
except Exception as e:
    print(f'Erro: {e}');