from textual.screen import Screen
from textual.widgets import (Header, Footer, Static)
from model import (biblioteca, Livro, Leitor, Emprestimo)

class TelaInicial(Screen):
    def compose(self):
        yield Header(show_clock=True)  # Exibe o cabeçalho com relógio
        yield Static("Bem-vindo à Biblioteca")
        yield Footer()  # Exibe o rodapé padrão

class TelaCadastrarLivros(Screen):
    def compose(self):
        yield Header(show_clock=True)  # Exibe o cabeçalho com relógio        
        yield Footer()  # Exibe o rodapé padrão
        yield Static("Esta é a tela de cadastro de livros.")

class TelaCadastrarLeitores(Screen):
    def compose(self):
        yield Header(show_clock=True)  # Exibe o cabeçalho com relógio        
        yield Footer()  # Exibe o rodapé padrão
        yield Static("Esta é a tela de cadastro de leitores.")
