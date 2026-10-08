# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
   Serve para indicar o status do livro no acervo. Se for `True`, significa que o livro está na biblioteca e pode ser emprestado. Se for `False`, significa que o livro já foi emprestado e não está disponível no momento.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
   Porque o SQLAlchemy gerencia as alterações em uma transação. As modificações feitas nos objetos (como alterar o valor de `disponivel`) ficam apenas na memória (sessão) até que o `commit()` seja chamado. O `commit()` é o comando que efetiva e persiste essas alterações permanentemente no banco de dados.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
   Usa-se o relacionamento nas consultas:
   - `listar_livros`, `listar_livros_disponiveis` e `buscar_livros_por_titulo`, ao acessar `livro.autor.nome` para exibir o nome do autor de cada livro.
   - `listar_livros_por_autor`, ao acessar `autor.livros` para obter a lista de livros vinculados àquele autor.