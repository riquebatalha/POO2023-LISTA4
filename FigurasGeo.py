'''
Hierarquia de Figuras Geométricas: considere as seguintes figuras geométricas: retângulo, triângulo
e círculo. Crie uma hierarquia de classes para representar essas figuras geométricas. Cada classe
deve ter os seguintes atributos:
• Retângulo:
• base: comprimento da base do retângulo.
• altura: altura do retângulo.

• Triângulo:
• base: comprimento da base do triângulo.
• altura: altura do triângulo.

• Círculo:
• raio: raio do círculo.
Cada classe deve implementar os seguintes métodos:

• calcularÁrea(): calcula a área da figura geométrica.
• calcularPerimetro(): calcula o perímetro (ou circunferência, no caso do círculo) da figura
geométrica.

Você deve criar as classes Retangulo, Triangulo e Circulo, que herdam de uma classe base
FiguraGeometrica. Cada classe deve implementar os métodos de cálculo de área e perímetro de
acordo com as fórmulas adequadas para cada figura geométrica.
Além disso, você deve criar objetos dessas classes e testar os métodos calcularÁrea e
calcularPerimetro, exibindo os resultados para cada figura geométrica criada.
Lembre-se de utilizar as fórmulas corretas para calcular a área e o perímetro de cada figura
geométrica
'''
class FiguraGeo():
    def __init__(self):
        def calcularArea(self):
            pass

        def calcularPerimetro(self):
            pass

class Retangulo(FiguraGeo):
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
    
    def calcularArea(self):
        area = self._base * self._altura
        print('+=' * 18)
        print('Área do retângulo: {}'.format(area))

    def calcularPerimetro(self):
        perimetro = self._base * 2 + self._altura * 2
        print('Perímetro do retângulo: {}'.format(perimetro))    
        print('+=' * 18)

class Triangulo(FiguraGeo):
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def calcularArea(self):
        area = self._base * self._altura / 2
        print('Área do triângulo: {}'.format(area))

    def calcularCircuferencia(self):
        perimetro = self._altura * 2 + self._base * 2 
        print('Circuferência do triângulo: {}'.format(perimetro))
        print('+=' * 18)

class Circulo(FiguraGeo):
    def __init__(self, raio):
        self._raio = raio

    def calcularArea(self):
        area = self._raio * self._raio * 3.14
        print('Área de um círculo: {}'.format(area))

    def calcularCircunferencia(self):
        circunferencia = 2 * 3.14 * self._raio
        print('Circunferência de um círculo: {}'.format(circunferencia))
        print('+=' * 18)

t1 = Retangulo(3,4)
t2 = Triangulo(3,4)
t3 = Circulo(3)

t1.calcularArea()
t1.calcularPerimetro()
t2.calcularArea()
t2.calcularCircuferencia()
t3.calcularArea()
t3.calcularCircunferencia()
