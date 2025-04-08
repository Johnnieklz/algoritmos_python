def numero_maior():
    numeros = []
    for i in range(3):
        valor = float(input(f"Digite a nota do aluno {i + 1}: "))
        numeros.append(valor)

    maior = max(numeros)

    print("o número maior é: ", maior)


numero_maior()