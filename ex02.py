from math import log as ln


def _fatorial(x: int) -> int:
    """Retorna o fatorial de x."""
    if x in (0, 1):
        return 1

    return x * _fatorial(x-1)


def gera_vetor() -> list:
    """Retorna uma lista de 10 elementos.
    O elemento da posição i é tal que
        i par: X[i] = 3**i + 7*i!
        i ímpar: X[i] = 2**i + 4*ln(i)
    """
    vec = []

    for i in range(10):
        if i % 2 == 0:
            vec.append(3**i+7*(_fatorial(i)))
        else:
            vec.append(2**i + 4*ln(i))
    
    return vec


if __name__ == "__main__":
    dados = gera_vetor()

    maior = max(dados)
    posicao_do_maior = dados.index(maior)
    media = sum(dados) / len(dados)

    print(f"O maior valor está na posição {posicao_do_maior}")
    print(f"A média dos elementos é {media:.2f}")
