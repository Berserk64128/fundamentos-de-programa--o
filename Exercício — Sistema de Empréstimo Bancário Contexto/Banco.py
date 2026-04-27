# Solicitação de dados
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
tempo_trabalho = int(input("Digite seu tempo de trabalho (em anos): "))
valor_emprestimo = float(input("Digite o valor do empréstimo desejado: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

# Cálculo da parcela
valor_parcela = valor_emprestimo / parcelas
limite = salario * 0.30

# Verificação das regras
if idade < 18:
    print(f"O cliente tem {idade} anos, salário de R$ {salario:.2f} e {tempo_trabalho} ano(s) de trabalho — portanto o empréstimo é negado automaticamente (cliente menor de idade).")

elif valor_parcela > limite:
    print(f"O cliente tem {idade} anos, salário de R$ {salario:.2f} e {tempo_trabalho} ano(s) de trabalho — a parcela de R$ {valor_parcela:.2f} ultrapassa 30% do salário, portanto o empréstimo é negado.")

elif salario >= 5000:
    print(f"O cliente tem {idade} anos, salário de R$ {salario:.2f} e {tempo_trabalho} ano(s) de trabalho — o empréstimo é aprovado automaticamente (salário alto).")

elif idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:
    print(f"O cliente tem {idade} anos, salário de R$ {salario:.2f} e {tempo_trabalho} ano(s) de trabalho — todas as condições básicas foram atendidas, portanto o empréstimo é aprovado.")

else:
    print(f"O cliente tem {idade} anos, salário de R$ {salario:.2f} e {tempo_trabalho} ano(s) de trabalho — o empréstimo é negado (cliente não atende aos requisitos).")

# Exibição dos dados
print(f"\nResumo:")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Tempo de trabalho: {tempo_trabalho} ano(s)")
print(f"Valor do empréstimo: R$ {valor_emprestimo:.2f}")
print(f"Parcelas: {parcelas}")
print(f"Valor da parcela: R$ {valor_parcela:.2f}")