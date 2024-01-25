from repositorio.livro_repositorio import livro_repositorio

def buscarPorCodigo(codigo: int) -> dict or None:
    for livro in livro_repositorio:
        if livro["codigo"] == codigo:
            return livro
    return None

if __name__ == "__main__":
    print(buscarPorCodigo(1))
    print(buscarPorCodigo(10))