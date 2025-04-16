class quadrado:
    def __init__(self, valor_lado, num1):
        self.valor_lado = valor_lado
        self.num1 = num1

    def pedir_lado(self):
        self.valor_lado = float(input("Digite o valor do lado do quadrado: "))
        return self.valor_lado

    def calcular_area(self):
        area = self.valor_lado ** 2
        return area

    def mostrar_resultados(self):
        print(f"Área do quadrado: {self.calcular_area()}")

    def mostrar_lado(self):
        print(f"Lado do quadrado: {self.valor_lado}")


if __name__ == "__main__":
    lado_inicial = float(input("Digite o valor inicial do lado do quadrado: "))
    quadrado1 = quadrado(valor_lado=lado_inicial, num1=0)

    quadrado1.mostrar_lado()

    quadrado1.pedir_lado()

    quadrado1.mostrar_resultados()