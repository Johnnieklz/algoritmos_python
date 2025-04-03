def celsius(celsius, F):
    return (F - 32) * 5 / 9

F = float(input("Digite a temperatura em Fahrenheit: "))

celsius = celsius(0, F)

print(f"A temperatura em Celsius é: {celsius:.2f}°C")