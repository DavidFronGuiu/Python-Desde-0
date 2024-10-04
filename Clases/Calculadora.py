class Calculadora:
    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicacion(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: división por cero"