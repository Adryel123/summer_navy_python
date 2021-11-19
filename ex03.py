def input_nota(text: str) -> float:
    """Lê a nota de um aluno.
    Caso o valor passado não seja um float,
    pede o imput no tipo correto."""

    try:
        nota = float(input(text))
        return nota
    except ValueError:
        print("Erro: nota inválida. Digite um número e use [.] como separador decimal.")
        nota = input_nota(text)
        return nota


if __name__ == "__main__":
    alunos = {}
    for i in range(1, 6):
        aluno = input(f"Digite o nome do {i}º aluno: ").strip().title()
        nota = input_nota(f"Digite a nota de {aluno}: ")
        alunos[aluno] = nota
        print()
    
    aluno_maior_nota = max(alunos, key=alunos.get) 
    maior_nota = alunos[aluno_maior_nota]

    print(f"O aluno com maior nota é {aluno_maior_nota}")
    print(f"Sua nota foi {maior_nota}")
