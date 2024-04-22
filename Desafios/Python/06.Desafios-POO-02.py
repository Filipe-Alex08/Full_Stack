class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def triangulo_valido(self):
        return (self.lado1 + self.lado2 > self.lado3) and \
               (self.lado1 + self.lado3 > self.lado2) and \
               (self.lado2 + self.lado3 > self.lado1)

    def calcular_area(self):
        if self.triangulo_valido():
            s = (self.lado1 + self.lado2 + self.lado3) / 2
            area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
            return area
        else:
            return

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

triangulo = Triangulo(lado1, lado2, lado3)

if triangulo.triangulo_valido():
    print("É um triângulo válido.")
    print("A área do triângulo é:", triangulo.calcular_area())
else:
    print("Não é um triângulo válido.")