from models.restaurante import ModelRestaurante


restaurante_carpa = ModelRestaurante('Carpa', 'peixes');
# restaurante_mexicano = ModelRestaurante('Mexicano express', 'Comida Mexicana');
# restaurante_japonese = ModelRestaurante('Tekomo Nakama', 'Comida Japonesa');

# restaurante_mexicano.alternar_status();

restaurante_carpa.receber_avaliacao('Fernando', 5);
restaurante_carpa.receber_avaliacao('Lais', 7);
restaurante_carpa.receber_avaliacao('Rebeca', 8);


def main():
    ModelRestaurante.listar_restaurantes();

if __name__ == '__main__':
    main()