print("¿Qué edad tienes?")
edad = input()
if(int(edad) < 18): #if recibe una condición que devuelve un valor binario: verdadero o falso, sí o no
    print("No tienes edad para votar")
else:   #Si la condición no se cumple, se realizará lo que siga al else
    print("Puedes votar")