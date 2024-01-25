from livro.livro_buscar import buscarPorCodigo
from repositorio.livro_repositorio import livro_repositorio

def deletarLivro(codigo: int) -> None:
    livro = buscarPorCodigo(codigo)
    if livro:
        livro_repositorio.remove(livro)
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado!")

if __name__ == "__main__":
    print(buscarPorCodigo(1))
    deletarLivro(1)
    print(buscarPorCodigo(1))
