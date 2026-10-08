from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""

    if session.query(Autor).first():
            return
    
    # TODO: crie pelo menos 3 autores.
    autor1 = Autor(nome="Mioses", pais="Brasil")
    autor2 = Autor(nome="Davi D🦁 🚩 Silva", pais="Brasil")
    autor3 = Autor(nome="Davi ⚫", pais="Brasil")

    # TODO: crie pelo menos 6 livros.
    # TODO: inclua livros disponíveis e indisponíveis.
    livro1 = Livro(titulo="Detran Impossível", ano=2026, autor=autor1, disponivel=True)
    livro2 = Livro(titulo="Amigona De Mioses", ano=2026, autor=autor1, disponivel=False)
        
    livro3 = Livro(titulo="Buraco Negro", ano=2026, autor=autor2, disponivel=True)
    livro4 = Livro(titulo="A arte de receber cabimento", ano=2026, autor=autor2, disponivel=True)
        
    livro5 = Livro(titulo="Direção conturbada", ano=2026, autor=autor3, disponivel=False)
    livro6 = Livro(titulo="Não me toque", ano=2026, autor=autor3, disponivel=True)
    
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    session.add_all([autor1, autor2, autor3, livro1, livro2, livro3, livro4, livro5, livro6])
    session.commit()
    print("Banco de dados populado com sucesso!")
    pass