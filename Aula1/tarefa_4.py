# Converter metros para centimetros.

'''
def metros_para_centimetros(metros):
    return metros * 100

metros = float(input("Digite a quantidade em metros: "))

centimetros = metros_para_centimetros(metros)

print(f"{metros} metros equivalem a {centimetros} centimetros.")'''


metros = float(input("Digite a quantidade em metros: "))

centimetros = metros * 100

print(f"{metros:.2f} metros equivalem a {centimetros:.2f} centimetros.")