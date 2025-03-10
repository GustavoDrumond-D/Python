from models.veiculo import ModelVeiculo

class ModelCarro(ModelVeiculo):
    def __init__ (this, marca, modelo, portas):
        super().__init__(marca, modelo)
        this._portas = portas

    def __str__(this):
        return f'Marca: {this._marca} \nModelo: {this.modelo}\nLigado: {'Sim' if this._ligado else 'Não'} \nPortas: {this._portas}'