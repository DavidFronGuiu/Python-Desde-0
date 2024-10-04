CAMBIO = 87.34


def rupiasAEuros():
    print("¿Qué cantidad deseas cambiar?")
    cantidad = int(input())
    if(cantidad >= 0):
        resultado = cantidad / CAMBIO
        print("El resultado es ", resultado)
    else:
        print("El valor debe ser mayor a 0")

def eurosARupias():
    print("¿Qué cantidad deseas cambiar?")
    cantidad = int(input())
    if(cantidad >= 0):
        resultado = cantidad * CAMBIO
        print("El resultado es ", resultado)
    else:
        print("El valor debe ser mayor a 0")

if __name__ == "__main__":
    print("¿Qué moneda tienes? ¿Euros o rupias?")
    moneda = input().upper()
    if(moneda == "EUROS" or moneda == "EURO"):
        eurosARupias()  #Llama a la función eurosARupias()
    elif (moneda == "RUPIAS" or moneda == "RUPIA"):
        rupiasAEuros()  #Llama a la función rupiasAEuros()
    else:
        print("Error. Finalizando programa")

