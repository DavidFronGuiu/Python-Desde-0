def comprobarNumero():
    while(True):
        print("Danos un número")
        try:
            num = int(input())
            return num
        except:
            print("Debe ser un número")

def calcularFactorial(num):
    if(num > 1):
        resultado = num * calcularFactorial(num - 1)    #Se llama de forma recursiva
        return resultado
    else: 
        return num


if __name__ == "__main__":
    print("El resultado es ", calcularFactorial(comprobarNumero()))