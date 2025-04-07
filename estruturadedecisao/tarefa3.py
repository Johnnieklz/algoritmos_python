def masc_fem():
    letra = input("Digite 'F' para feminino ou 'M' para masculino: ").strip().upper()

    if letra == "F":
        print("É feminino!")
    elif letra == "M":
        print("É masculino!")
    else:
        print("Opção inválida. Digite apenas 'F' ou 'M'.")


masc_fem()



