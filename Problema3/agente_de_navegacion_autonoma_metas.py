from collections import deque

class AgenteNavegacion:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.meta = self.encontrar_meta()

    def encontrar_meta(self):
        """Encuentra la meta para salir del laberinto M"""
        # Logica para encontrar la meta
        pass

    def es_valido(self, x, y):
        """Una posicion valida para el laberinto."""
        # Logica para verificar la posicion valida
        pass

    def encontrar_ruta(self, inicio):
        """Se usa BFS para encontrar una buena ruta"""
        # Logica para encontra la ruta mas corta
        pass

    def mostrar_ruta(self, ruta):
        """Muestra la ruta seguida por el agente."""
        # Logica para buscar la ruta del laberinto
        pass

# Se crea el laberinto
laberinto = [
    ['#', ' ', ' ', '#', '#'],
    ['#', '#', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#'],
    ['#', '#', ' ', ' ', 'M'],
    ['#', '#', '#', '#', '#']
]

# Creación y ejecución del agente
agente = AgenteNavegacion(laberinto)
inicio = (1, 1)  # Primera posición del agente
ruta = agente.encontrar_ruta(inicio)

if ruta:
    print("Una ruta encontrada:")
    agente.mostrar_ruta(ruta)
else:
    print("No hay una ruta valida")