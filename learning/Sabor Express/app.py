import os

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
    print('4. sair');
def opcoes():
    opcao = int(input('Escolha uma opção:'))
    # opcao = int(opcao)
    if opcao == 1:
        print('opção: cadastrar restaurante');
    elif opcao == 2:
        print('opção: listar restaurantes');
    elif opcao == 3:
        print('opção: ativar restaurante');
    elif opcao == 4:
        print('opção: sair');
        finalizar_app();
    else:
        print('Opção inválida');

def main():
    exibir_nome_do_programa();
    exibir_opcoes();
    opcoes();

if __name__ == '__main__':
    main()