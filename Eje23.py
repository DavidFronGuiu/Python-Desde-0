from Clases.Videojuego import Videojuego

def myfunc(n):
  return lambda a : a * n

if __name__ == "__main__":
    videojuego1 = Videojuego("Baldur's Gate 3", "Larian Studios", 2023)
    videojuego2 = Videojuego("The Legend of Zelda: Ocarina of Time", "Nintendo", 1998)
    videojuego3 = Videojuego("Uncharted 4: El Desenlace Del Ladrón", "Naughty Dog", 2016)   

    videojuegos = [videojuego1, videojuego2, videojuego3]

    for juego in videojuegos:
        print(juego.titulo)


    doblar = myfunc(2)
    triplicar = myfunc(3)
    print(doblar(2))
    print(triplicar(2))
        
    videojuegos.sort(key=lambda x: x.fec)
    print("")
    for juego in videojuegos:
        print(juego.titulo)
   
   