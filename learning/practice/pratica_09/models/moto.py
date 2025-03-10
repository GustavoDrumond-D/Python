from models.veiculo import ModelVeiculo

class ModelMoto(ModelVeiculo):
    def __init__ (this, marca, modelo, tipo):
        super().__init__(marca, modelo)
        this._tipo = tipo
    
    def __str__(this):
        return f'Marca: {this._marca} \nModelo: {this.modelo} \nLigado: {'Sim' if this._ligado else 'Não'} \nTipo: {this._tipo}'