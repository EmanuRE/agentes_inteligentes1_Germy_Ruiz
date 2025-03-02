from collections import deque

class AgenteSeleccionRutas:
    def __init__(self, entorno):
        self.entorno = entorno
        self.filas = len(entorno)
        self.columnas = len(entorno[0])
        self.meta = self.encontrar_meta()

    def encontrar_meta(self):
        """Se encuentra la posición meta (M)"""
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.entorno[i][j] == 'M':
                    return (i, j)
        return None

    def es_valido(self, x, y):
        """Se verifica la posicion valida"""
        return 0 <= x < self.filas and 0 <= y < self.columnas and self.entorno[x][y] != '#'

    def calcular_utilidad(self, ruta):
        """La mejor ruta acumulada"""
        utilidad = 0
        for (x, y) in ruta:
            if self.entorno[x][y] not in ['#', 'M']:
                try:
                    utilidad += int(self.entorno[x][y])  # Suma las celdas
                except ValueError:
                    # Sino es un numero no se toma en cuenta
                    pass
        return utilidad

    def encontrar_ruta_optima(self, inicio):
        """Se encuentra la mejor ruta BFS"""
        cola = deque()
        cola.append((inicio, [inicio]))  # La posiciion actual
        mejor_ruta = None
        mejor_utilidad = -float('inf')
        visitado = set()

        while cola:
            (x, y), ruta = cola.popleft()

            if (x, y) == self.meta:
                utilidad = self.calcular_utilidad(ruta)
                if utilidad > mejor_utilidad:
                    mejor_utilidad = utilidad
                    mejor_ruta = ruta
                continue

            if (x, y) in visitado:
                continue
            visitado.add((x, y))

            # Movimientos: arriba, abajo, izquierda, derecha
            movimientos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for nueva_x, nueva_y in movimientos:
                if self.es_valido(nueva_x, nueva_y):
                    cola.append(((nueva_x, nueva_y), ruta + [(nueva_x, nueva_y)]))

        return mejor_ruta

    def mostrar_ruta(self, ruta):
        """Se muestra la mejor ruta del agente"""
        for i in range(self.filas):
            for j in range(self.columnas):
                if (i, j) in ruta:
                    print('Z', end=' ')  # El punto del agente Z
                elif self.entorno[i][j] == 'M':
                    print('M', end=' ')  # Se muestra la meta
                else:
                    print(self.entorno[i][j], end=' ')
            print()

# Se definen los lugares optimos 
entorno = [
    ['#', '5', '2', '#', '#'],
    ['#', '1', '#', '3', '#'],
    ['#', '4', '2', '6', '#'],
    ['#', '#', '7', '1', 'M'],
    ['#', '#', '#', '#', '#']
]

# Creación y ejecución del agente
agente = AgenteSeleccionRutas(entorno)
inicio = (1, 1)  # La primer posición del agente
ruta_optima = agente.encontrar_ruta_optima(inicio)

if ruta_optima:
    print("La mejor ruta encontrada:")
    agente.mostrar_ruta(ruta_optima)
    print(f"Utilidad del camino: {agente.calcular_utilidad(ruta_optima)}")
else:
    print("No hay una ruta valida.")