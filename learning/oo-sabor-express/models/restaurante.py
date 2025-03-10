from models.avaliacao import ModelAvaliacao

class ModelRestaurante:
    restaurantes = []
    # self é o proprio objeto que foi criado a partir da classe
    # mas não precisa ser chamado self, pode ser qualquer coisa, como this
    def __init__(this, nome, categoria):
        this._nome = nome.title() # Atribuindo o nome
        this.categoria = categoria # Atribuindo a categoria
        this._ativo = False # Atribuindo o status do restaurante
        this._avaliacao = []

        # todas as instancias da classe ModelRestaurante serao adicionadas na lista
        ModelRestaurante.restaurantes.append(this)

    # __str__ serve para exibir o objeto como uma string
    def __str__(self):
        return f'Restaurante: {self._nome.l} | Categoria: {self.categoria}'
    
    # @classmethod serve para criar um metodo de classe, que pode ser chamado diretamente da classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"nome".ljust(33)} | {"categoria".ljust(31)} | {'avaliacao'.ljust(31)} |{"ativo"}');
        for restaurante in cls.restaurantes:
            print(f'restaurante: {restaurante._nome.ljust(20)} | categoria: {restaurante.categoria.ljust(20)} | avaliação: {str(restaurante.media_avaliacao).ljust(20)} |ativo: {restaurante.ativo}') 

    @property
    def ativo(this):
        return '✔' if this._ativo else '✘'
    
    def alternar_status(this):
        this._ativo = not this._ativo

    def receber_avaliacao(this, cliente, nota):
        if 0 <= nota <= 5:
            avalicao = ModelAvaliacao(cliente, nota)
            this._avaliacao.append(avalicao)

    @property
    def media_avaliacao(this):
        if not this._avaliacao:
            return "sem avaliacao"
    
        