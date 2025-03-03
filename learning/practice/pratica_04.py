import os;


# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
print('''
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
''')
dicionario = {
    'nome': 'João',
    'idade': 20,
    'cidade': 'Rio de Janeiro'
}
print(dicionario);
input('Pressione qualquer tecla para continuar... ');
os.system('cls');



# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
print('''
2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
''')
dicionario['idade'] = 21;
dicionario['profissão'] = 'Desenvolvedor';
# del remove o item do dicionario
del dicionario['cidade'];
print(dicionario);

input('Pressione qualquer tecla para continuar... ');
os.system('cls');



# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
print('''
3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
''')
numeros_a_serem_quadrados = [1, 2, 3, 4, 5];
for numero in numeros_a_serem_quadrados:
    print(f'numero quadrado de {numero}: {numero * numero}');
input('Pressione qualquer tecla para continuar... ');
os.system('cls');



# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
print('''
4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
''');
procura = input('Insira a chave que deseja procurar: ');
for chave in dicionario:
    if procura == chave:
        print(f'Chave {procura} encontrada');
    elif procura == '':
        print('Erro: Valor indispensável');
    else:
        print(f'Chave {procura} nao encontrada');

input('Pressione qualquer tecla para continuar... ');
os.system('cls');



# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

print('''
5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
''')
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {};
# o split separa a frase em uma lista, onde cada palavra fica em um item da lista
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1;
print(contagem_palavras);
input('Pressione qualquer tecla para continuar... ');
os.system('cls');