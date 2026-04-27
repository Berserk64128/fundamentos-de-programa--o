print("Sistema de Empréstimo Bancário")

# Solicitação de dados
idade = int(input("Digite a idade do idade: "))
salario = float(input("Digite o salário do cliente: "))
tempo_trabalho = int(input("Digite o tempo de trabalho (em anos): "))

# Estruturas condicionais
if idade < 18:
    print("Empréstimo negado. Cliente menor de idade.")
elif salario >= 5000:
    print("Empréstimo aprovado automaticamente.")
elif idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")
# Verificar a idade, o salario e o tempo de trabalho
