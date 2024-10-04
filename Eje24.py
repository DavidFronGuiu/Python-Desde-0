
class Figura: 
    def calcular_perimetro():
        print("Figura indefinida")

    def calcular_area():
        print("Figura indefinida")

class Circulo(Figura):
    PI = 3.14
    def __init__(self, radio):
        self.radio = int(radio)

    def calcular_perimetro(self):
        return self.radio * 2 * self.PI
    
    def calcular_area(self):
        return self.radio**2 * self.PI
    
    
class Triangulo(Figura):
    def __init__(self, lado):
        self.lado = int(lado)

    def calcular_perimetro(self):
        return self.lado*3
    
    def calcular_area(self):
        return (self.lado**2 - (self.lado/2)**2)**(1/2) * self.lado
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = int(base)
        self.altura = int(altura)

    def calcular_perimetro(self):
        return self.altura*2+self.base*2
    
    def calcular_area(self):
        return self.altura*self.base
    
class Poligono(Figura):
    def __init__(self, base, numLados, apotema):
        self.base = int(base)
        self.numLados = int(numLados)
        self.apotema = int(apotema)

    def calcular_perimetro(self):
        return self.base * self.numLados
    
    def calcular_area(self):
        return self.apotema * self.calcular_perimetro() / 2

def seleccionar_figura():
    print("¿Qué figura deseas calcular? ¿Círculo, rectángulo, triángulo o un poligono de 5 o más lados")
    respueta = input()
    if(respueta.lower() == "circulo"):
        figura = Circulo(input("¿Cuál es el radio del círuclo? "))
    elif (respueta.lower() == "triangulo"):
        figura = Triangulo(input("¿Cuál es su lado? "))
    elif (respueta.lower() == "rectangulo"):
        figura = Rectangulo(input("¿Cuál es su base? "), input("¿Y su altura? "))
    else:
        figura = Poligono(input("¿Cuál es su base? "), input("¿Cuántos lados tiene? "), input("¿Cuál es su apotema? "))

    print("El perimetro es ", figura.calcular_perimetro())
    print("El area es ", figura.calcular_area())




if __name__ == "__main__":
    print("Bienvenido a nuestra aplicación. ¿Qué deseas hacer? Calcular una figura o salir")
    while(True):
        respuesta = input()
        if(respuesta.lower() == "calcular una figura"):
            seleccionar_figura()
            print("¿Qué deseas hacer ahora?")
        elif (respuesta.lower() == "salir"):
            break
        else:
            print("Respueta no reconocida. Vuelva a intentarlo.")