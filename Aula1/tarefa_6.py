def area_do_quadrado(lado):
    return lado * lado

lado = float(input("Digite o lado do quadrado: "))

area = area_do_quadrado(lado)

print(f"A área do quadrado é: ", area)
print(f"O dobro da área do quadrado: ", area * 2)