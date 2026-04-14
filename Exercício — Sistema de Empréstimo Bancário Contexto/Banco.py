# Solicitação de dados
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
tempo_trabalho = int(input("Digite seu tempo de trabalho (em anos): "))

# Verificação das regras
if idade < 18:
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho — todas as condições básicas foram atendidas, portanto o empréstimo é negado automaticamente (cliente menor de idade).")


elif salario >= 5000:
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho — todas as condições básicas foram atendidas, portanto o empréstimo é aprovado automaticamente (salário alto).")


elif idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho — todas as condições básicas foram atendidas, portanto o empréstimo é aprovado.")


else:
    print(f"O cliente tem {idade} anos, salário de R$ {salario} e {tempo_trabalho} ano(s) de trabalho — todas as condições básicas foram atendidas, portanto o empréstimo é negado (cliente não atende aos requisitos).")


# Exibição dos dados
print(f"\nResumo:")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario}")
print(f"Tempo de trabalho: {tempo_trabalho} ano(s)")
