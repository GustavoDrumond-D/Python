class ModelVeiculo:
    def __init__ (this, marca, modelo):
        this._marca = marca
        this.modelo = modelo
        this._ligado = False
    
    def __str__(this):
        return f'Marca: {this._marca} \nModelo: {this.modelo} \nLigado: {'Sim' if this._ligado else 'Não'}'
    
    