def triangulo(n):
    for i in range(1, n + 1):
        print(''.join(map(str, range(1, i + 1))))

valor = int(input("Digite um valor para o triângulo: "))
triangulo(valor)