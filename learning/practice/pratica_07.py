# 1.Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# 2.Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# 3.Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

# 4.Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

# 5.Crie uma instância da classe e imprima o valor da propriedade titular.

# 6.Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

# 7.Crie um método de classe para a conta ClienteBanco.

# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#         self._ativo = False

#     def __str__(self):
#         return f'Titular da conta: {self.titular} | Saldo: {self.saldo}'
    
#     @classmethod
#     def ativar_conta(cls, conta):
#         cls._ativo = True

    
# conta_01 = ContaBancaria('João', 1020)
# conta_02 = ContaBancaria('Maria', 500)

# print(conta_01)
# print(conta_02)

# conta_03 = ContaBancaria('Pedro', 1000)
# print(f'status da conta: {conta_01._ativo}')
# ContaBancaria.ativar_conta(conta_03)
# print(f'status da conta: {conta_01._ativo}')

# 1) Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False  # Atributo protegido

# 2) Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"
    
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)

# 3) Adicione um método de classe chamado `ativar_conta` à classe `ContaBancaria` que define o atributo ativo como `True`. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")