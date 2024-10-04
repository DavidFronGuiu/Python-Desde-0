
class Libro:
    
    def __init__(self, titulo, autor, anyo):
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo

    def __str__(self):
        cadena = "Este libro se trata de " + self.titulo + " escrito por " + self.autor + ' en ' + str(self.anyo)
        return cadena



if __name__ == "__main__":
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605) #Crea un objeto de la clase libro con los siguientes valores
    libro2 = Libro("Hamlet", "William Shakespeare", 1603)
    libro3 = Libro("Frankenstein o el moderno Prometeo", "Mary Shelley", 1818)
    libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", 1813)

    print(libro1.titulo)
    print(libro1.autor)
    print(libro3.titulo)
    print(libro3.anyo)
    print(libro4)