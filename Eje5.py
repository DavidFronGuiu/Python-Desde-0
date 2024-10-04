while (True):   #Repite infinitamente la condición hasta que alcanza el break
    print("Dame un número positivo")
    num = input()
    if(int(num) > 0):
        print("El número es positivo")
        break
    else:
        print("El número es negativo")