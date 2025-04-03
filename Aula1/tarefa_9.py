def farenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))

farenheit = farenheit(celsius)

print(f"A temperatura em Fahrenheit é: {farenheit:.2f}°F")