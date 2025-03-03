import os

restaurantes = [{'nome': 'Teste', 'categoria': 'carnes', 'ativo': False },
                {'nome': 'Teste 2', 'categoria': 'carnes', 'ativo': True },
                {'nome': 'Teste 3', 'categoria': 'carnes', 'ativo': False }];

'''Função responsavel por finalizar o app'''
def finalizar_app():
    os.system('cls');
    print('Finalizando...\n');
'''Função responsavel por exibir o nome do programa'''
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
'''Função responsavel por exibir as opcoes'''
def exibir_opcoes():
    print('1. Cadastrar restaurante');
    print('2. Listar restaurantes');
    print('3. Buscar restaurante');
    print('4. Alterar status do restaurante');
    print('5. Deletar restaurante');
    print('6. sair');
'''Função responsavel por voltar ao menu'''
def voltar_ao_menu():
    input('Pressione qualquer tecla para continuar... ');
    main();
'''Função responsavel por exibir a opcao invalida'''
def opcao_invalida():
    print('Opção inválida!');
    voltar_ao_menu();
'''Função responsavel por exibir o subtitulo'''
def exibir_subtitulo(texto):
    os.system('cls');
    linha = '═' * len(texto);
    print(linha);
    print(texto);
    print(linha);
    print()



'''Esssa função por cadastrar um restaurante'''
def cadastrar_restaurante():     

    exibir_subtitulo('Cadastrar restaurante');
    try:
        nome_restaurante = input('Forneça o nome do restaurante: ');
        categoria_restaurante = input('Forneça a categoria do restaurante: ');
        if nome_restaurante == '' or categoria_restaurante == '':
            print('Erro: Valor necessário');
            voltar_ao_menu();
        else:
            # .append() adiciona um item ao final da lista
            restaurantes.append({
                'nome': nome_restaurante,
                'categoria': categoria_restaurante,
                'ativo': False
            });
            print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
            voltar_ao_menu();
    except:
        print('Erro ao cadastrar restaurante');
        voltar_ao_menu();
'''Essa função por listar os restaurantes'''
def listar_restuarntes():
    exibir_subtitulo('Listando restaurantes...');
    
    print(f'{'nome'.ljust(29)} | {'categoria'.ljust(31)} | {'status'.ljust(29)}');
    for restaurante in restaurantes:
        # .index retorna o index do item
        status_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo';
        # .ljust() alinha o texto a esquerda
        print(f"{restaurantes.index(restaurante) + 1}. Nome: {restaurante['nome'].ljust(20)} | Categoria: {restaurante['categoria'].ljust(20)} | Status: {status_restaurante}")
    voltar_ao_menu();
'''Essa função por buscar um restaurante'''
def buscar_restaurante():
    exibir_subtitulo('buscar restaurante');
    try:
        nome_busca = input('Insira o nome do restaurante: ');
    except:
        print('Erro ao buscar restaurante');
        voltar_ao_menu();
'''Essa função por alterar o status do restaurante'''
def estado_restaurante():
    exibir_subtitulo('Alterar status do restaurante');
    try:
        nome_restaurante = input('Insira o nome do restaurante que deseja modificar o status: ');
        restaurante_encontrado = False;
        for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                restaurante_encontrado = True;
                restaurante['ativo'] = not restaurante['ativo'];
                mensagem = f'O Restaurante {nome_restaurante} foi ativado' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi desativado';
                print(mensagem);
            elif nome_restaurante == '':
                print('Erro: Valor indispensável');
            else:
                print('Restaurante nao encontrado');
                voltar_ao_menu();
        voltar_ao_menu();
    except:
        print('Erro ao ativar restaurante');
        voltar_ao_menu();
'''Essa função por deletar um restaurante'''
def deletar_restaurante():
    try:
        print('deletar restaurante');
    except:
        print('Erro ao deletar restaurante');

'''Função responasavel por ativar as opcoes do menu'''
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
                estado_restaurante();
            case 5:
                deletar_restaurante();
            case 6:
                finalizar_app();
            case _:
                opcao_invalida();
    except:
        opcao_invalida();

'''Função principal'''        
def main():
    os.system('cls');
    exibir_nome_do_programa();
    exibir_opcoes();
    opcoes();

if __name__ == '__main__':
    main()