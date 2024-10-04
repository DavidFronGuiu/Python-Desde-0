print("Dame un número positivo")
num = input()

while (int(num) <= 0):   #Repite infinitamente la condición hasta que se deja de cumplir la condición
    print("Ese número no era positivo")
    num = input()

print("Este número sí era positivo")    #Como su identación está al mismo nivel que el while, no entra dentro del bucle sino que se realizará una vez que se acabe