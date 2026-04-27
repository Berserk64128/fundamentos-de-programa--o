total = 0
quantidade = 0

while True:
    valor = float(input("Digite o valor do produto: "))

    if valor == 0:
        break

    total += valor
    quantidade += 1

# Evitar divisão por zero
if quantidade > 0:
    media = total / quantidade
else:
    media = 0

# Aplicar desconto se necessário
if total > 100:
    desconto = total * 0.10
    total_final = total - desconto
    print("\nDesconto de 10% aplicado!")
else:
    total_final = total

print("\n--- Resultado ---")
print(f"Total da compra: R$ {total_final:.2f}")
print(f"Quantidade de produtos: {quantidade}")
print(f"Média dos valores: R$ {media:.2f}")