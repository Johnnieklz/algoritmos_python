def nota():
    while True:
        try:
            nota = float(input("Digite o valor da nota: "))

            if 0 <= nota <= 10:
                print("Nota OK.")
                break
            else:
                print("Nota inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


nota()