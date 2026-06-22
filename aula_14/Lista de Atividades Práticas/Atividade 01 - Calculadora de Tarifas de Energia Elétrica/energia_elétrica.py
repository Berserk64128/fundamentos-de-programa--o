#Declaração dos variáveis globais - snake_case 
valor_ate_100kwh = 0.40
valor_ate_200kwa = 0.60
valor_acima_200kwa = 0.90

print(f" ------ Seja bem vindo ao programa de calculo de energia eletrica ------")
while True:
    input_kwa = input(f"Digite a quantidade da kwa consumidos (ou 'sair' para encerrar):")
    if input_kwa.lower() == 'sair':
        print("Encerrando o programa. Obrigado por usar!\n")
        break
    elif not input_kwa.isdigit():
        print("Entrada inválida. Por favor, digite um número válido ou 'sair' para encerrar.\n")
        continue
    else:
        kwh = int(input_kwa)
        if kwh <= 100:
            valor_total = kwh * valor_ate_100kwh
            print(f"A faixa de consumo é: 0 a 100 kWh")
            print(f"O valor total da conta de energia é: R$ {valor_total:.2f}\n")
        elif kwh <= 200:
            valor_total = 100 * valor_ate_100kwh + (kwh - 100) * valor_ate_200kwa
            print(f"A faixa de consumo é: 100 a 200 kWh")
            print(f"O valor total da conta de energia é: R$ {valor_total:.2f}\n")
        else:
            valor_total = 100 * valor_ate_100kwh + 100 * valor_ate_200kwa + (kwh - 200) * valor_acima_200kwa
            print(f"A faixa de consumo é: 200 kWh ou mais")
            print(f"O valor total da conta de energia é: R$ {valor_total:.2f}\n")