from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    pais: Mapped[str]

    # TODO: relacione Autor com Livro usando relationship e back_populates.


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    ano: Mapped[int]
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))

    # TODO: adicione o campo disponivel, com valor padrão True.
    # TODO: relacione Livro com Autor usando relationship e back_populates.
