import os

if(os.path.isfile("archivos/myfile.txt")):
    print("Existe")
else:
    f = open("archivos/myfile.txt", "x")
    #Crea el archivo myfile.txt
    f.close()

f = open("archivos/myfile.txt", "a") #Añade al archivo el siguiente texto
f.writelines("Now the file has more content1!\n")
f.writelines("Now the file has more content2!\n")
f.close()


f = open("archivos/myfile.txt", "r+")    #Lee y añade al archivo


#print(f.read(5))

for x in f:
    print(x) 
f.writelines("Tercera línea\n")
f.close()


#os.remove("myfile.txt")
#Elimina el archivo

