from sqlalchemy import select

from models import Autor, Livro

def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    livros = session.execute(select(Livro)).scalars().all()
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")

def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    livros = session.execute(select(Livro).where(Livro.disponivel == True)).scalars().all()
    for livro in livros:
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome}")

def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    livros = session.execute(select(Livro).where(Livro.titulo.contains(trecho))).scalars().all()
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")

def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    autor = session.execute(select(Autor).where(Autor.nome == nome_autor)).scalar_one_or_none()
    if autor:
        print(f"Livros de {autor.nome}:")
        for livro in autor.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f" - {livro.titulo} ({status})")
    else:
        print(f"Autor '{nome_autor}' não encontrado.")