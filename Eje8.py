notas = [4, 7, 3, 8, 10]
alumnos = ["Alba", "Lucia", "Mateo", "Pablo", "Laura"]

for i in range(0, len(notas), 1): #Valor inicial, valor final, aumento
    if(notas[i]>=5):
        print(f"{alumnos[i]} ha aprobado")