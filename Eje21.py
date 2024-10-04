
class Pelicula:
    def __init__(self, nombre, director, fec_estreno):
        self.nombre = nombre
        self.director = director    #Pelicula tiene como atributo un objeto de la clase Director
        self.fec_nac = fec_estreno

class Director:
    def __init__(self, nombre, nacionalidad, fec_nac):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fec_nac = fec_nac

    def __str__(self):
        cadena = self.nombre + " nacio el " + str(self.fec_nac) + ' y tiene la nacionalidad ' + self.nacionalidad
        return cadena


if __name__ == "__main__":
    directores = []
    spielberg = Director("Steven Spielberg", "USA", 1946)
    directores.append(spielberg)
    gerwig = Director("Greta Gerwig", "USA", 1983)
    directores.append(gerwig)
    sorogoyen = Director("Rodrigo Sorogoyen", "ES", 1981)
    directores.append(sorogoyen)

    for director in directores:#Mostramos todos los directores
        print(director)

    peliculas = []
    peliculas.append(Pelicula("Munich", spielberg, 2006))#Añades una película
    print(peliculas[0].director)#Mostramos el director de la primera película