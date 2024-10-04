import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Baraja:
    def __init__(self):
        valores = ["2", "3", "4", "5", "6", "7", "10", "11", "12", "100"]
        palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
        self.cartas = [Carta(valor, palo) for valor in valores for palo in palos]
        self.mezclar()

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()


if __name__ == "__main__":
    jugador1 = 0
    jugador2 = 0
    while(jugador1 < 3 and jugador2 < 3):
        # Uso de la clase Baraja
        print("Empezamos la ronda")
        baraja = Baraja()
        carta_repartida = baraja.repartir_carta()
        print("Carta robada: ")
        print(carta_repartida)
        print("")
        print("¿Deseas coger otra carta?")
        respuesta = input()
        if(respuesta.upper() == "SI"):
            carta_repartida = baraja.repartir_carta()
            print("Carta robada: ")
            print(carta_repartida)
        carta_rival = baraja.repartir_carta()
        print("")
        print("Carta del rival: ")
        print(carta_rival)
        print("")
        if(int(carta_repartida.valor) < int(carta_rival.valor)):
            print("Gana el rival")
            jugador2 = jugador2 + 1
        elif(int(carta_repartida.valor) > int(carta_rival.valor)):
            print("Ganaste")
            jugador1 = jugador1 + 1
        else:
            print("Empate")

        print("Jugador 1: " +str(jugador1))
        print("Jugador 2: " +str(jugador2))
        print("")

