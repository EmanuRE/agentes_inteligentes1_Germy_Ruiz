import random

class AgenteExplorador:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.mapa = [[False for _ in range(columnas)] for _ in range(filas)]  # Mapa de visitas
        self.posicion_actual = (0, 0)  # Primera posicion del agente
        self.mapa[0][0] = True  # Primera posicion visitada

    def mover(self):
        """Mueve al agente a una celda no visitada."""
        x, y = self.posicion_actual
        movimientos_posibles = []

        # celdas adyacentes
        if x > 0 and not self.mapa[x - 1][y]:  # Arriba
            movimientos_posibles.append((x - 1, y))
        if x < self.filas - 1 and not self.mapa[x + 1][y]:  # Abajo
            movimientos_posibles.append((x + 1, y))
        if y > 0 and not self.mapa[x][y - 1]:  # Izquierda
            movimientos_posibles.append((x, y - 1))
        if y < self.columnas - 1 and not self.mapa[x][y + 1]:  # Derecha
            movimientos_posibles.append((x, y + 1))

        if movimientos_posibles:
            nueva_posicion = random.choice(movimientos_posibles)
            self.posicion_actual = nueva_posicion
            self.mapa[nueva_posicion[0]][nueva_posicion[1]] = True
            return f"Se mueve a {nueva_posicion}"
        else:
            return "No hay celdas no visitadas"

    def explorar(self):
        """Se explora el mapa para no dejar celdas"""
        while True:
            print(f"Posición actual: {self.posicion_actual}")
            resultado = self.mover()
            print(resultado)
            if resultado == "No hay celdas no visitadas":
                print("Exploración exitosa")
                break

# Creacion y ejecución del agente
agente = AgenteExplorador(5, 5)
agente.explorar()