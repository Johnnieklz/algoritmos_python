def triangulo(n):
    for i in range(1, n + 1):
        print(str(i) * i)

valor = int(input("Digite um valor para o triângulo: "))

triangulo(valor)