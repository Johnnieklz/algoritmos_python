def calcular_salario():
    try:
        valor_por_hora = float(input("Digite quanto você ganha por hora: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

        salario_mensal = valor_por_hora * horas_trabalhadas

        print(f"Seu salário no mês será: R$ {salario_mensal:.2f}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


if __name__ == "__main__":
    calcular_salario()