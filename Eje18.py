def comprobarNumero():
    while(True):
        print("Danos un número")
        try:
            num = int(input())
            return num
        except:
            print("Debe ser un número")

def esPositivo(num):
    if(num >= 0):
        return True
    else:
        return False


if __name__ == "__main__":
    num1 = comprobarNumero()
    num2 = comprobarNumero()
    resultado = num1 - num2
    if(esPositivo(resultado)):  #La función devuelve verdadero o falos
        print("El resultado es positivo")
    else:
        print("El resultado es negativo")