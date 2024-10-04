CAMBIO = 87.34

print("¿Qué moneda tienes? ¿Euros o rupias?")
moneda = input().upper()    #Transforma el String en otro String con todos los caracteres en mayúsculas
if(moneda == "EUROS" or moneda == "EURO"):
    print("¿Qué cantidad deseas cambiar?")
    cantidad = int(input())
    if(cantidad >= 0):
        resultado = cantidad * CAMBIO
        print("El resultado es ", resultado)
    else:
        print("El valor debe ser mayor a 0")
elif (moneda == "RUPIAS" or moneda == "RUPIA"):
    print("¿Qué cantidad deseas cambiar?")
    cantidad = int(input())
    if(cantidad >= 0):
        resultado = cantidad / CAMBIO
        print("El resultado es ", resultado)
    else:
        print("El valor debe ser mayor a 0")
else:
    print("Error. Finalizando programa")