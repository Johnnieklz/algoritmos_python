'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento. Então busquei resolver da seguinte forma:

A = população 1 = 80000

B = população 2 = 200000
'''

# Primeira forma de resolver o problema:

a = 80000
b = 200000
tempo = 0

while a < b:
    a += a * 0.03
    b += b * 0.015
    tempo += 1

print(f"Serão necessários {tempo} anos para que a população do país A ultrapasse ou iguale a população do país B.")
print(f"População final de A: {int(a)} habitantes.")
print(f"População final de B: {int(b)} habitantes.")

# Segunda forma de resolver o problema:
'''
pop_a = 80000
pop_b = 200000
ano_passou = 0 

while pop_a < pop_b:

    ano_passou += 1
    mais_pop_a = pop_a * 3 // 100
    pop_a += mais_pop_a
    mais_pop_b = pop_b * 1.5 // 100
    pop_b += mais_pop_b

    if pop_a > pop_b and pop_a != pop_b: 
        print(f'A população da cidadade A: {pop_a:.0f} habitantes, Passa a população da cidade B: {pop_b} habitantes',end='')
        print(f', após {ano_passou} anos. Além disso, a população de B nunca será exatamente igual à população de A')
        print()

    elif pop_a == pop_b:
        print(f'A população da cidade A e da cidade B irão igualar-se após {ano_passou} anos')'''