print("¿Qué nota has sacado en el examen?")
nota = int(input())
if(nota<5):     #Compureba si es menor que 5
    print("Has sacado un suspendo")
elif(nota<6):   #Si los condicionales anteriores son falos, comprueba si es menor que 6
    print("Has sacado un aprobado")
elif(nota<7):   #Si los condicionales anteriores son falos, comprueba si es menor que 7
    print("Has sacado un bien")
elif(nota<9):   #Si los condicionales anteriores son falos, comprueba si es menor que 9
    print("Has sacado un notable")
else:           #Si ninguno de los anteriores es verdero, significa que la nota es superior al 9
    print("Has sacado un sobresaliente")