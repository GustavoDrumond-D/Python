# 1.Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# 2.Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# 3.Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

# 4.Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# 5.Crie uma instância da classe e imprima o valor da propriedade titular.

# 6.Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# 7.Crie um método de classe para a conta ClienteBanco.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular da conta: {self.titular} | Saldo: {self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        cls._ativo = True

    
conta_01 = ContaBancaria('João', 1020)
conta_02 = ContaBancaria('Maria', 500)

print(conta_01)
print(conta_02)

conta_03 = ContaBancaria('Pedro', 1000)
print(f'status da conta: {conta_01._ativo}')
ContaBancaria.ativar_conta(conta_03)
print(f'status da conta: {conta_01._ativo}')

class ContaBancariaPythonica:
    def __init__ (self, titular, saldo):
        self._titular = titular;
        self._saldo = saldo;
        self._ativo = False;

    @property
    def titular(self):
        return self._titular
    
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
conta_04 = ContaBancariaPythonica('João', 1020)
print(f'Titular: {conta_04.titular} | Saldo: {conta_04.saldo()}');

class ClienteBanco:
    def __init__ (self, id, titular, saldo, telefone, email):
        self._id = id;
        self._titular = titular;
        self._saldo = saldo;
        self._telefone = telefone;
        self._email = email;

    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancariaPythonica(titular, saldo)
        return conta
    
conta_cliente = ClienteBanco.criar_conta('João', 1020)
print(f'Titular: {conta_cliente.titular} | Saldo: {conta_cliente.saldo()}');
