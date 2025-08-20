from model import (Biblioteca, Livro)

#
# Cadastrar livro
#
# pré-condições: 
# - exite uma Biblioteca

biblioteca = Biblioteca()

# Início do cadastro

biblioteca.cadastrar_livro("a01", "Volta ao mundo em 80 dias")
biblioteca.cadastrar_livro("a02", "Viagem ao Centro da Terra")
biblioteca.cadastrar_livro("a03", "Vinte Mil Léguas Submarinas")


# pós-condições
# - existe um livro_novo:Livro
# - livro_novo está em Biblioteca.livros

# Testando pós-condições

# Consulta de livros
#
# Pré-condições:
# existe uma biblioteca

# pós-condições
# nenhuma em especial

um_livro = biblioteca.consultar_livro("a03")
print(um_livro.titulo)


# Excluir livro
# pré-condições:
# exite uma bilioteca

# 