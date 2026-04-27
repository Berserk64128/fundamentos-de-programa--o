# Lista principal da turma
turma = []

# Quantidade de alunos
qtd = int(input("Quantos alunos serão cadastrados? "))

# Coleta de dados
for i in range(qtd):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    # Cálculo da média
    media = (nota1 + nota2 + nota3) / 3

    # Situação
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Armazenando dados do aluno
    aluno = [nome, nota1, nota2, nota3, media, situacao]
    turma.append(aluno)

# Relatório final
print("\n===== BOLETIM DA TURMA =====")
for aluno in turma:
    print(f"\nNome: {aluno[0]}")
    print(f"Notas: {aluno[1]}, {aluno[2]}, {aluno[3]}")
    print(f"Média: {aluno[4]:.2f}")
    print(f"Situação: {aluno[5]}")