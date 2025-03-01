from collections import deque

class AgenteNavegacion:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.meta = self.encontrar_meta()

    def encontrar_meta(self):
        """Encuentra la meta para salir del laberinto M"""
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.laberinto[i][j] == 'M':
                    return (i, j)
        return None

    def es_valido(self, x, y):
        """Una posicion valida para el laberinto."""
        return 0 <= x < self.filas and 0 <= y < self.columnas and self.laberinto[x][y] != '#'

    def encontrar_ruta(self, inicio):
        """Se usa BFS para encontrar una buena ruta"""
        cola = deque()
        cola.append((inicio, [inicio]))  # (posición momentanea y ruta)
        visitado = set()

        while cola:
            (x, y), ruta = cola.popleft()

            if (x, y) == self.meta:
                return ruta  # Devuelve la ruta completa, incluyendo la meta

            if (x, y) in visitado:
                continue
            visitado.add((x, y))

            # Movimientos: arriba, abajo, izquierda, derecha
            movimientos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for nueva_x, nueva_y in movimientos:
                if self.es_valido(nueva_x, nueva_y):
                    cola.append(((nueva_x, nueva_y), ruta + [(nueva_x, nueva_y)]))

        return None  # No se encuentra una ruta

    def mostrar_ruta(self, ruta):
        """Muestra la ruta seguida por el agente."""
        for i in range(self.filas):
            for j in range(self.columnas):
                if (i, j) in ruta:
                    print('Z', end=' ')  # Punto del Agente Z
                elif self.laberinto[i][j] == 'M':
                    print('M', end=' ')  # Mostrar la meta
                else:
                    print(self.laberinto[i][j], end=' ')
            print()

# Creación de laberinto
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