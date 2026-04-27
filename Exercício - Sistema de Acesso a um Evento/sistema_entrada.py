while True:
    nome = (input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    convite = (input("Possui convite (S/N)? "))

    if convite not in ["S", "N"]:
        print("Entrada inválida. Use S ou N.")
        continue
        
    # Verificação das regras
    if idade < 16:
            print("Entrada negada.")
    elif idade >= 16 and convite == "S":
            print("Entrada permitida.")
    else:
            print("Entrada negada.")

    # Pergunta para continuar ou sair
    opcao = input("Você deseja sair (digite 'sair' ou 'continuar')? ") 

    if opcao == "sair":
        print("Sistema encerrado.")
        break
    elif opcao == "continuar":
        continue
    else:
        print("Opção inválida. Continuando o sistema...")