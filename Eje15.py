lista = []
print("Dame 5 números:")
for i in range (0, 5, 1):
    lista.append(int(input()))  #Añade elemento
print(lista)
lista.sort()
print(lista)

i = 0
while(i < len(lista)):
    if(lista[i] < 5):
        print("Eliminamos ", lista[i])
        lista.pop(i)
    else:
        i = i+1

lista.remove(int(input("¿Qué número deseas eliminar?: ")))  #Elimina elemento
print(lista)