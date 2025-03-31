from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'restaurante')

bebida_suco = Bebida('suco melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_carne = Prato('carne de porco', 20.00, 'carne de porco')
prato_carne.aplicar_desconto()

restaurante_praca.adicionar_item_no_cardapio(bebida_suco)
restaurante_praca.adicionar_item_no_cardapio(prato_carne)

def main():
    restaurante_praca.exibir_cardapio
    
if __name__ == '__main__':
    main()