from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver indisponível, exiba uma mensagem.
    # TODO: se estiver disponível, altere disponivel para False e faça commit.
    pass


def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver disponível, exiba uma mensagem.
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.
    pass
