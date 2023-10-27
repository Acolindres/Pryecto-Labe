from laberinto import Juego
from functools import reduce


class JuegoArchivo(Juego):
    def _init_(self, mapas):
        super().__init__(mapas)