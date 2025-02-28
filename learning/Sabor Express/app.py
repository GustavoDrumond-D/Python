import os

restaurantes = [];

def finalizar_app():
    os.system('cls');
    print('Finalizando...\n');
def exibir_nome_do_programa():
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
      """);
def exibir_opcoes():
    print('1. Cadastrar restaurante');
    print('2. Listar restaurantes');
    print('3. Buscar restaurante');
    print('4. Ativar restaurante');
    print('5. Deletar restaurante');
    print('6. sair');
def voltar_ao_menu():
    input('Pressione qualquer tecla para continuar... ');
    main();
def opcao_invalida():
    print('Opção inválida!');
    voltar_ao_menu();
def exibir_subtitulo(texto):
    os.system('cls');
    print(texto);
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar restaurante');
    try:
        nome_restaurante = input('Forneça o nome do restaurante: ');
        if nome_restaurante == '':
            print('Erro: Valor necessário');
            voltar_ao_menu();
        else:
            # .append() adiciona um item ao final da lista
            restaurantes.append(nome_restaurante);
            print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
            voltar_ao_menu();
    except:
        print('Erro ao cadastrar restaurante');
        voltar_ao_menu();
def listar_restuarntes():
    exibir_subtitulo('Listando restaurantes...');
    for restaurante in restaurantes:
        # .index retorna o index do item
        print(f'{restaurantes.index(restaurante) + 1}. {restaurante}');
    
    voltar_ao_menu();
def buscar_restaurante():
    exibir_subtitulo('buscar restaurante');
    try:
        nome_busca = input('Insira o nome do restaurante: ');
    except:
        print('Erro ao buscar restaurante');
        voltar_ao_menu();

# def ativar_restaurante():
# def deletar_restaurante():

def opcoes():
    try:
        opcao = int(input('Escolha uma opção: '))
        # # opcao = int(opcao)
        # if opcao == 1:
        #     print('opção: cadastrar restaurante');
        # elif opcao == 2:
        #     print('opção: listar restaurantes');
        # elif opcao == 3:
        #     print('opção: ativar restaurante');
        # elif opcao == 4:
        #     print('opção: sair');
        #     finalizar_app();
        # else:
        #     print('Opção inválida');

        # match parece com o switch case, mas em python não precisa de chaves
        match opcao:
            case 1:
                cadastrar_restaurante();
            case 2:
                listar_restuarntes();
            case 3:
                buscar_restaurante();
            case 4:
                print('opção: ativar restaurante');
                # ativar_restaurante();
            case 5:
                print('opção: deletar restaurante');
                # deletar_restaurante();
            case 6:
                print('opção: sair');
                finalizar_app();
            case _:
                opcao_invalida();
    except:
        opcao_invalida();
        
def main():
    os.system('cls');
    exibir_nome_do_programa();
    exibir_opcoes();
    opcoes();

if __name__ == '__main__':
    main()