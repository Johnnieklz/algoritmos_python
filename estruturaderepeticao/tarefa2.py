def senha():
    input_nome_usuario = input("Digite o nome do usuario: ")
    input_senha = input("Digite a senha: ")

    while True:
        if input_senha == input_nome_usuario:
            print("A senha não pode ser igual ao nome de usuario.")
            input_senha = input("Digite a senha: ")
        else:
            break
    print("Login aceito!")


senha()