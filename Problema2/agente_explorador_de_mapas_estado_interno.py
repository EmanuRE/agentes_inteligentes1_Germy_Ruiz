import random

class AgenteExplorador:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.mapa = [[False for _ in range(columnas)] for _ in range(filas)]  # Mapa de visitas
        self.posicion_actual = (0, 0)  # Primera posición del agente
        self.mapa[0][0] = True  # Primera posición visitada

    def mover(self):
        """Mueve al agente a una celda no visitada."""
        # Logica para mover el agente
        pass

    def explorar(self):
        """Explora el mapa para no dejar celdas sin visitar."""
        # Logica para explorar el mapa
        pass

# Creación del agente
agente = AgenteExplorador(5, 5)
agente.explorar()