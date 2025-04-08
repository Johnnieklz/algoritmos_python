def notas_parciais():
    numeros = []
    for i in range(2):
        valor = float(input(f"Digite a nota do aluno {i + 1}: "))
        numeros.append(valor)

    soma = sum(numeros)
    media = soma / len(numeros)

    print(f"Média: {media:.2f}")

    if media == 10:
        print("Aprovado com distinção!!!")
    elif media >= 7:
        print("Aprovado!")
    else:
        print("Média não alcançada")


notas_parciais()
