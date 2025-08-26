def menu():
    print("\n--- Sistema de Estoque ---")
    print("1 - Cadastrar o Evento")
    print("2 - Compra de ingressos")
    print("3 - Repor os ingressos")
    print("4 - Ver quantidade de ingressos")
    print("0 - Sair")
    return input("Escolha uma opção: ")

evento = None
quantidade = 0

while True:
    opcao = menu()

    if opcao == "1":
        evento = input("Digite o nome do evento: ")
        quantidade = 0
        print(f"Evento '{evento}' cadastrado com sucesso!")

    elif opcao == "2":
        if evento is None:
            print("Nenhum ingresso vendido ainda!")
        else:
            retirar = int(input("Digite a quantidade de ingressos : "))
            if retirar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade -= retirar
                print(f"Comprou {retirar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "3":
        if evento is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a repor: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "4":
        if evento is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            print(f"Ingressos Vendidos: {retirar} | Quantidade em estoque: {quantidade}")

    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")