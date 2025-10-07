def menu():
    print("1- Cadastrar Paciente")
    print("2- Acesso aos Cadastros")
    print("3- Atender Paciente")
    print("0- Sair")
    return input("Escolha uma opção :")
    
paciente = None
cadastro = 0

while True:
    opcao = menu
    
    if opcao == "1":
        paciente = input("Digite o nome do Paciente: ")
        cadastro = 0

        print(f"Paciente {paciente} cadastrado com sucesso!")
