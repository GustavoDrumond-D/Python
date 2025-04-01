from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        
    # def __str__(self):
    #     return f''

app = Flask(__name__)

@app.route('/inicio')

def saudacao():
    
    lista_jogos = [
        Jogo('Super Mario Bros', 'Plataforma', 'SNES'),
        Jogo('Castlevania', 'RPG', 'SNES'),
        Jogo('Final Fantasy', 'RPG', 'SNES'),
        Jogo('Metroid', 'Plataforma', 'SNES'),
        Jogo('Super Mario World', 'Plataforma', 'SNES'),
        Jogo('Donkey Kong', 'Plataforma', 'SNES'),
        Jogo('Tekken', 'Luta', 'SNES'),
        Jogo('Street Fighter', 'Luta', 'SNES'),
        Jogo('Tekken 2', 'Luta', 'SNES'),
        Jogo('Mortal Kombat', 'Luta', 'SNES'),
        Jogo('Mortal Kombat 2', 'Luta', 'SNES'),]
    
    return render_template('lista.html', titulo = 'Jogos', jogos = lista_jogos)

app.run(debug=True)