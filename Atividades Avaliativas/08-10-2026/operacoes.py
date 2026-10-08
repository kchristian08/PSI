from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    # TODO: busque o livro pelo título.
    livro = session.execute(select(Livro).where(Livro.titulo == titulo)).scalar_one_or_none()

    # TODO: se o livro não existir, exiba uma mensagem.
    if not livro:
        print(f"Erro: Livro '{titulo}' não encontrado.")
        return

    # TODO: se já estiver indisponível, exiba uma mensagem.
    if not livro.disponivel:
        print(f"Erro: O livro '{titulo}' já está emprestado.")
        return

    # TODO: se estiver disponível, altere disponivel para False e faça commit.
    livro.disponivel = False
    session.commit()
    print(f"Sucesso: O livro '{titulo}' foi emprestado.")
    pass


def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    # TODO: busque o livro pelo título.
    livro = session.execute(select(Livro).where(Livro.titulo == titulo)).scalar_one_or_none()

    # TODO: se o livro não existir, exiba uma mensagem.
    if not livro:
        print(f"Erro: Livro '{titulo}' não encontrado.")
        return
    
    # TODO: se já estiver disponível, exiba uma mensagem.
    if livro.disponivel:
        print(f"Erro: O livro '{titulo}' já está disponível.")
        return
    
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.
    livro.disponivel = True
    session.commit()
    print(f"Sucesso: O livro '{titulo}' foi devolvido.")
    pass