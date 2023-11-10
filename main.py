from juego_archivo import JuegoArchivo

if __name__ == "__main__":
    mapa = "Pryecto-Labe/mapas/"


    nombre= input("Introduzca su nombre: ")
    print("!Bienvenido a esta nueva aventura, {}!".format(nombre))

    juego = JuegoArchivo(mapa)
    juego.terminal()
    juego.jugar()