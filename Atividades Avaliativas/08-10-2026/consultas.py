from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    # TODO: use select(Livro) e acesse livro.autor.nome.
    pass


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    # TODO: filtre Livro.disponivel igual a True.
    pass


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    # TODO: use contains ou like no título.
    pass


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    # TODO: busque o autor e navegue por autor.livros.
    pass
