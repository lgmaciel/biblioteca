from textual.app import App
from textual.binding import Binding
from view import (TelaInicial, TelaCadastrarLivros, TelaCadastrarLeitores)

class AppBiblioteca(App):

    SCREENS = {
        "inicial": TelaInicial,
        "cadastrar_livros": TelaCadastrarLivros,
        "cadastrar_leitores": TelaCadastrarLeitores,
    }

    BINDINGS = [
        Binding("escape", "ir_para_inicial", "Início"),
        Binding("ctrl+n", "cadastrar_livro", "Cadastrar Livro"),
        Binding("ctrl+l", "cadastrar_leitores", "Cadastrar Livro"),
    ]

    def on_mount(self):
        self.push_screen("inicial")

    def action_ir_para_inicial(self):
        self.switch_screen("inicial")

    def action_cadastrar_livro(self):
        self.switch_screen("cadastrar_livros")

    def action_cadastrar_leitores(self):
        self.switch_screen("cadastrar_leitores")

if __name__ == "__main__":
    AppBiblioteca().run()
