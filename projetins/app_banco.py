import os;
import getpass;
import random;
import time;
import sys;

class Banco:
    contas = []
    def __init__ (self, id, titular, senha):
        self._id = id;
        self._titular = titular;
        self._senha = senha;
        self._saldo = 0;

    @classmethod
    def criar_conta(cls):
        try:
            print('Opção: Criar Conta');
            print();
        
            nome_titular = input('Insira o nome do titular: ');
            if not nome_titular:
                raise Exception('O nome do titular nao pode ser vazio');
    
            senha_titular = getpass.getpass('Insira a senha: ');
            if not senha_titular:
                raise Exception('A senha nao pode ser vazia');
    
            for conta in cls.contas:
                if conta._titular == nome_titular:
                    raise Exception('Ja existe uma conta com esse titular');

            gerar_id = random.randint(1000, 9999);
            nova_conta = Banco(gerar_id, nome_titular, senha_titular)
            cls.contas.append(nova_conta)

            print('Conta criada com sucesso!')
            print(f'ID da conta: {nova_conta._id}')
            print(f'Titular: {nova_conta._titular}')
            voltar_ao_menu()        


        except Exception as e:
            print('Erro ao criar conta');
            print(f'Erro: {e}');
            voltar_ao_menu();

    def tirar_extrato(self):
        print('Opção: Tirar Extrato');
        print();
        print(f'Titular: {self._titular}');
        print(f'Saldo: {self._saldo}');
    def depositar(self):
        pass;
    def sacar(self):
        pass;
    def transferir(self):
        pass;
    def alterar_senha(self):
        pass;
    def excluir_conta(self):
        pass;

    @staticmethod
    def entrar_conta():
        print('Opção: Entrar na Conta');
        print();
    
        try:
            id_conta = int(input('Insira o ID da conta: '));
            if not id_conta:
                raise Exception('O ID da conta nao pode ser vazio');

            senha_conta = getpass.getpass('Insira a senha: ');
            if not senha_conta:
                raise Exception('A senha nao pode ser vazia');
            
            if id_conta not in [conta._id for conta in Banco.contas]:
                raise Exception('Nao existe uma conta com esse ID');

            for conta in Banco.contas:
                if conta._id == id_conta and conta._senha == senha_conta:
                    print('Entrou na conta com sucesso!');
                    input('Pressione qualquer tecla para continuar... ');
                    os.system('cls');
                    
                    while True:
                        print('Escolha uma opção:');
                        print('1 - Tirar Extrato \n2 - Depositar \n3 - Sacar \n4 - Transferir \n5 - Alterar Senha \n6 - Excluir Conta \n7 - Sair');
                        opcao = int(input('Escolha uma opção: '));
                        match opcao:
                            case 1:
                                conta.tirar_extrato();
                                print('deseja realizar outra operacao?');
                                print('(1) sim | (2) nao');
                                input_opcao = int(input('Escolha uma opção: '));
                                if input_opcao == 1:
                                    continue;
                                else:
                                    finalizar_app();
                                    voltar_ao_menu();
                            case 2:
                                conta.depositar();
                                print('deseja realizar outra operacao?');
                                print('(1) sim | (2) nao');
                                input_opcao = int(input('Escolha uma opção: '));
                                if input_opcao == 1:
                                    continue;
                                else:
                                    finalizar_app();
                                    voltar_ao_menu();
                            case 3:
                                conta.sacar();
                                print('deseja realizar outra operacao?');
                                print('(1) sim | (2) nao');
                                input_opcao = int(input('Escolha uma opção: '));
                                if input_opcao == 1:
                                    continue;
                                else:
                                    finalizar_app();
                                    voltar_ao_menu();
                            case 4:
                                conta.transferir();
                                print('deseja realizar outra operacao?');
                                print('(1) sim | (2) nao');
                                input_opcao = int(input('Escolha uma opção: '));
                                if input_opcao == 1:
                                    continue;
                                else:
                                    finalizar_app();
                                    voltar_ao_menu();
                            case 5:
                                conta.alterar_senha();
                                print('deseja realizar outra operacao?');
                                print('(1) sim | (2) nao');
                                input_opcao = int(input('Escolha uma opção: '));
                                if input_opcao == 1:
                                    continue;
                                else:
                                    finalizar_app();
                                    voltar_ao_menu();
                            case 6:
                                conta.excluir_conta();
                                print('deseja realizar outra operacao?');
                                print('(1) sim | (2) nao');
                                input_opcao = int(input('Escolha uma opção: '));
                                if input_opcao == 1:
                                    continue;
                                else:
                                    finalizar_app();
                                    voltar_ao_menu();
                            case 7:
                                finalizar_app();
                                voltar_ao_menu();
                                break;
                            case _:
                                opcao_invalida();
                    
                    
                 
        except Exception as e:
            print('Erro ao entrar na conta');
            print(f'Erro: {e}');
            voltar_ao_menu();
            

    @staticmethod
    def listar_contas():
        print('Opção: Listar contas');
        print();
        
        for conta in Banco.contas:
            print(f'ID: {conta._id}');
            print(f'Titular: {conta._titular}');
            print();

        voltar_ao_menu();

def iniciar_sistema():
    os.system('cls');
    print('Bem vindo ao Banco XPTO!');
    print();
    print('''Esolha uma opção: \n1 - Criar Conta \n2 - Entrar na Conta \n3 - listar contas \n4 - Sair''');
def voltar_ao_menu():
    input('Pressione qualquer tecla para continuar... ');
    main();
def opcao_invalida():
    print('Opção inválida!');
def finalizar_app():
    sinal_de_saida = [' ', '.', '..', '...']
    for _ in range(3):
        for sinal in sinal_de_saida:
            sys.stdout.write(f'\rFinalizando{sinal}');
            sys.stdout.flush();
            time.sleep(0.5);
            

def opcoes():
    try:
        opcao = int(input('Escolha uma opção: '));
        match opcao:
            case 1:
                Banco.criar_conta();
            case 2:
                Banco.entrar_conta();
            case 3:
                Banco.listar_contas();
            case 4:
                finalizar_app();
                print('\nObrigado por utilizar o Banco XPTO!');
            case _:
                opcao_invalida();
                voltar_ao_menu();
    except Exception as e:
        print(f'Erro: {e}');
        voltar_ao_menu();

def main():
    os.system('cls');
    iniciar_sistema();
    opcoes();
    
if __name__ == '__main__':
    main();