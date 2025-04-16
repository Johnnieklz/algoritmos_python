# Exercicio 1 - Criar uma classe bola que tenha os atributos cor, circunferencia e material.
# A classe deve ter os métodos: trocarCor e mostrarCor.

class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, cor):
        self.cor = cor
        print('Cor trocada com sucesso!')

    def mostrarCor(self):
        return self.cor


bola_futebol = bola(cor="branca", circunferencia=0.22, material="couro")
bola_futebol.trocarCor("azul")

print("A cor atual da bola é:", bola_futebol.mostrarCor())