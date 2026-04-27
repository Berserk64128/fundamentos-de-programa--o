<<<<<<< HEAD
# Crie um sistema aonde o valor inicial é de R$1000 e o usuário consiga realizar um saque e ao final se exibido o valor restante do saldo.
saldo = 1000
while saldo > 0:
    saque = float(input("Digite o valor do saque: "))
    saldo -= saque # saldo = saldo - saque
=======
# Crie um sistema aonde o valor inicial é de R$1000 e o usuário consiga realizar um saque e ao final se exibido o valor restante do saldo.
saldo = 1000
while saldo > 0:
    saque = float(input("Digite o valor do saque: "))
    saldo -= saque # saldo = saldo - saque
>>>>>>> f46ef55b99b85ef64f45f066cc4272d46c3d33e2
    print(f'Saldo restante: {saldo}')