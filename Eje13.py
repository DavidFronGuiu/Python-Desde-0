import random
solucion = random.randint(0, 9)
while(True):
    intento = int(input("En qué número estoy pensando: "))
    if(solucion < intento):
        print("Te has pasado")
    elif(solucion > intento):
        print("Te has quedado corto")
    else:
        print("¡Has acertado!")
        break