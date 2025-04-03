def salario_do_mes(valor_hora, num_hora):
    return valor_hora * num_hora

valor_hora = float(input("Digite o valor da hora: "))

num_hora = int(input("Digite o número de horas trabalhadas: "))

salario = salario_do_mes(valor_hora, num_hora)

print(f"O salário semanal é: R$ {salario}")
print(f"O salário do mensal é: R$ {salario * 4}")