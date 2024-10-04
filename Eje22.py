

class Deportista:
    def __init__(self, nombre, deporte, fec_nac):
        self.nombre = nombre
        self.deporte = deporte
        self.fec_nac = fec_nac
    
    def __str__(self):
        cadena = self.nombre + " nacio el " + str(self.fec_nac) + ' y practita ' + self.deporte
        return cadena

class Futbolista(Deportista):   #Futbolista hereda la clase Deportista()
    def __init__(self, nombre, fec_nac, equipo):
        super().__init__(nombre, "Futbol", fec_nac)
        self.equipo = equipo
    
    def Equipo(self):
        cadena = "El equipo donde más tiempo ha jugado es " + self.equipo
        return cadena

class Atleta(Deportista):
    def __init__(self, nombre, fec_nac, modalidad):
        super().__init__(nombre, "Atletismo", fec_nac)
        self.modalidad = modalidad

if __name__ == "__main__":
    deportista1 = Deportista("Mireia Belmonte", "Natacion", "10/11/1990")
    futbolista1 = Futbolista("Andres Iniesta",  "11/05/1984", "FCBarcelona")
    futbolista2 = Futbolista("Salma Celeste", "13/11/2003", "FCBarcelona")
    atleta1 = Atleta("Ana Peleteiro", "2/12/1995", "Triple salto")

    print(futbolista1)
    print(atleta1)
    print(futbolista2.Equipo())
    #print(atleta1.Equipo())