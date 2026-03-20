# Estrutura de repetição
# if (se) -> verifica se uma condição é true(verdadeira). Se for, ele executa o código.
# elif (senão se) -> é usado para testar várias condições. Ele só executa se todas as condições anteriores forem falses.
# else (senão) -> Executa o código se a condição if for false(falsa).

# idade_usuario = 15
# # se o usuario for maior de 18 anoes, eu vou passar a informação: Você é maior de idade;
# if idade_usuario >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade")

idade = 18
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 0 and idade < 18:
    print("Você é jovem de idade.")
elif idade >= 70:
    print("Você é experiente de idade.")
else:
    print("Você é menor de idade.")