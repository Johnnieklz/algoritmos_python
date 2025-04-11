def nome():
    while True:
        nome = input("Digite o seu nome: ")

        if len(nome) >= 3:
            print("Nome válido!")
            return nome
        else:
            print("O nome deve ter mais de 3 caracteres. Tente novamente.")


def idade():
    while True:
        try:
            idade = int(input("Digite a sua idade: "))

            if 0 < idade < 150:
                print("Idade válida!")
                return idade
            else:
                print("Idade inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número inteiro.")


def salario():
    while True:
        try:
            salario = float(input("Digite o seu salário: "))

            if salario > 0:
                print("Salário válido!")
                return salario
            else:
                print("Salário inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")


def sexo():
    while True:
        sexo = input("Digite o seu sexo (M/F): ").strip().upper()

        if sexo in ['M', 'F']:
            print("Sexo válido!")
            return sexo
        else:
            print("Sexo inválido. Tente novamente.")


def estado_civil():
    while True:
        estado_civil = input("Digite o seu estado civil (S/C/V/D): ").strip().upper()

        if estado_civil in ['S', 'C', 'V', 'D']:
            print("Estado civil válido!")
            return estado_civil
        else:
            print("Estado civil inválido. Tente novamente.")


def exibir_dados(nome, idade, salario, sexo, estado_civil):
    print("\nDados informados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")


nome_usuario = nome()
idade_usuario = idade()
salario_usuario = salario()
sexo_usuario = sexo()
estado_civil_usuario = estado_civil()

exibir_dados(nome_usuario, idade_usuario, salario_usuario, sexo_usuario, estado_civil_usuario)

