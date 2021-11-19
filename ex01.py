def conta_numeros() -> int:
    """Conta quantos números entre 1 e 5.000.000 são múltiplos
    simultâneos de 2, 37 e 49"""
    
    valor = 5000001  # O range() não inclui o maior valor

    # Note que 2, 37 e 49 são primos entre si, portanto o
    # MDC entre eles será simplesmente o produto entre eles.
    produto = 2 * 37 * 49  

    # A quantidade de elementos que satisfazem as condições
    # não é tão grande, portanto não há problema salvar todos em 
    # memória.
    satisfazem_a_condicao = list(range(produto, valor, produto))
    
    quantidade = len(satisfazem_a_condicao)
    
    return quantidade


if __name__ == "__main__":
    quantidade = conta_numeros
    print(f"Há {quantidade} números que satisfazem as 3 condições.")