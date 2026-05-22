# Desenvolva um sistema de pizzaria onde será recebido o preço total, um desconto de 10%, e ao final exiba o valor total do pedido com esse desconto;

# Declarar uma def (funcão)
def calcular_total(nome, preco, desconto=0.10):
    valor_desconto = preco * desconto
    total = preco - valor_desconto
    return print(f""" RECIBO
                 Pedido do cliente: {nome}
                 Valor do pedido: R$ {preco}
                 Desconto aplicado: {desconto}
                 Total R$ {total:.2f}
                 """)

# Invocação do def
calcular_total("João",45.90)
calcular_total("Ana",38.50)
calcular_total("Maria",20)
calcular_total("Rian",19)
calcular_total("Kitty", 8.99)