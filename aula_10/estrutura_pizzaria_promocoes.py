<<<<<<< HEAD
# Variáveis da pizzaria
FRETE = 2 #Constante Fake
pizza_sabor = input("Informe o sabor da pizza - [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]:")
pizza_tamanho = input("Informe o tamanho da pizza - [pequena], [média], [grande]: ")
dia_semana = input("Informe o dia da semana - [quarta], [quinta], [sexta], [sábado], [domingo]: ")

print(f" o sabor escolido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")
# Promoções -> Estruturas condicionais

# Comprando qualquer pizza e qualquer tamanho no sábado,
# o refri é gratuito.
if dia_semana == "sábado":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Refri hoje é por conta da casa!.")
elif dia_semana == "domingo":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete e o Refri hoje é por conta da casa!.")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete hoje é por conta da casa!.")


# Comprando uma pizza de calabresa tamanho médio, em qualquer dia, o frete é gratuito.

=======
# Variáveis da pizzaria
FRETE = 2 #Constante Fake
pizza_sabor = input("Informe o sabor da pizza - [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]:")
pizza_tamanho = input("Informe o tamanho da pizza - [pequena], [média], [grande]: ")
dia_semana = input("Informe o dia da semana - [quarta], [quinta], [sexta], [sábado], [domingo]: ")

print(f" o sabor escolido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")
# Promoções -> Estruturas condicionais

# Comprando qualquer pizza e qualquer tamanho no sábado,
# o refri é gratuito.
if dia_semana == "sábado":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Refri hoje é por conta da casa!.")
elif dia_semana == "domingo":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete e o Refri hoje é por conta da casa!.")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete hoje é por conta da casa!.")


# Comprando uma pizza de calabresa tamanho médio, em qualquer dia, o frete é gratuito.

>>>>>>> f46ef55b99b85ef64f45f066cc4272d46c3d33e2
# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.