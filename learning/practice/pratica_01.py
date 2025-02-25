#1. Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura.');

#2. Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = 'Gustavo';
idade = 20;
print(f'Meu nome é {nome} e tenho {idade} anos.');

#3.Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha.
print("""
      A
      L
      U
      R
      A
    """)

# 4.Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais.

pi = 3.14159;

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))
