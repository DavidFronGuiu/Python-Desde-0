
def comprobarNumero():
    while(True):
        print("Danos un número")
        try:
            num = int(input())
            return num  #Devuelve el valor de num
        except:
            print("Debe ser un número")

if __name__ == "__main__":
    num1 = comprobarNumero()
    num2 = comprobarNumero()
    print("La suma es ", num1+num2)