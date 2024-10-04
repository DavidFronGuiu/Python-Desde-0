
num1 = int(input("Danos un número: "))
num2 = int(input("Danos otro número: "))
operador = input("¿Qué operación te gustaría realizar? (+ - * /): ")

match operador:     #Compara el valor de la variable operador con los siguientes casos
    case "+":
         print("Suma")
         resultado = num1 + num2
    case"-":
         print("Resta")
         resultado = num1 - num2
    case "*":
         print("Multiplicación")
         resultado = num1 * num2
    case "/":
        print("División")
        resultado = num1 / num2
    case _:
        print("Error")
        resultado = "No se ha podido realizar la operación"
print(resultado)