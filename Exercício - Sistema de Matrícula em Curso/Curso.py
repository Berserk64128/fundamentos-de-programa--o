# Solicitação de dados
idade = int(input("Digite sua idade: "))
nota = int(input("Digite sua nota: "))
frequencia = float(input("Digite sua frequência (em %): "))
18
# Verificação das regras
if idade < 18:
    print("matrícula negado automaticamente.")

elif nota >= 9:
    print("matrícula aprovado automaticamente.")

elif idade >= 18 and nota >= 6 and frequencia >= 75:
    print("matrícula aprovado.")

else:
    print("matrícula negada.")

# Exibição dos dados
print(f"\nResumo:")
print(f"Idade: {idade}")
print(f"Nota: {nota}")
print(f"Frequência: {frequencia}")
