from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, descricao, tamanho):
        super().__init__(nome, preco)
        self._descricao = descricao
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._descricao} | {self._tamanho}'