def maior():

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num1 > num2:
        print(f"{num1} é maior do que {num2}.")
    elif num2 > num1:
        print(f"{num2} é maior do que {num1}.")
    else:
        print("Os dois valores são iguais.")
maior()