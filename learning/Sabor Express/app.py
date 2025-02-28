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
    print('3. Ativar restaurante');
    print('4. Deletar restaurante');
    print('5. sair');
def opcao_invalida():
    print('Opção inválida!');
    input('Pressione qualquer tecla para continuar...');
    main();

def cadastrar_restaurante():
    os.system('cls');
    try:
        nome_restaurante = input('Forneça o nome do restaurante:\n');
        if nome_restaurante == '':
            print('Nome invalido');
            main();
        else:
            # .append() adiciona um item ao final da lista
            restaurantes.append(nome_restaurante);
            print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
            input('Pressione qualquer tecla para continuar...');
            main();
    except:
        print('Erro ao cadastrar restaurante');
        input('Pressione qualquer tecla para continuar...');
        main();

def listar_restuarntes():
    os.system('cls');
    print('Listando restaurantes...');
    
    for restaurante in restaurantes:
        # .index retorna o index do item
        print(f'{restaurantes.index(restaurante) + 1}. {restaurante}');
    
    input('Pressione qualquer tecla para continuar...');
    main();


# def ativar_restaurante():

# def deletar_restaurante():

def opcoes():
    try:
        opcao = int(input('Escolha uma opção:'))
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
                print('opção: cadastrar restaurante');
                cadastrar_restaurante();
            case 2:
                print('opção: listar restaurantes');
                listar_restuarntes();
            case 3:
                print('opção: ativar restaurante');
                # ativar_restaurante();
            case 4:
                print('opção: deletar restaurante');
                # deletar_restaurante();
            case 5:
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