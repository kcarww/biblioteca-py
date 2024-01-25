from repositorio.livro_repositorio import livro_repositorio

codigo_atual = 1

# Cadastro de livro - function
def registrarLivro(titulo: str, autor: str) -> None:
    livro = criarLivro(titulo, autor)
    livro_repositorio.append(livro)
    print("Livro adicionado com sucesso!")
def criarLivro(titulo: str, autor: str) -> dict:
    global codigo_atual
    codigo_atual += 1
    livro = {
        "codigo": codigo_atual,
        "titulo": titulo,
        "autor": autor,
        "emprestado": False
    }
    return livro

if __name__ == "__main__":
    registrarLivro("1984", "George Orwel")
    print(livro_repositorio)


