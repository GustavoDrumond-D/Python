from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco melancia', 5.00, 'melancia', 'grande')
prato_carne = Prato('carne de porco', 20.00, 'carne de porco')



def main():
    print(bebida_suco)
    print(prato_carne)

if __name__ == '__main__':
    main()