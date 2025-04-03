def raio_do_circulo(raio):
    return 3.14 * (raio * raio)

area = float(input("Digite o raio do círculo: "))

raio = raio_do_circulo(area)

print(f"A área do círculo é {raio:.2f} ")