from collections import deque

class AgenteSeleccionRutas:
    def __init__(self, entorno):
        self.entorno = entorno
        self.filas = len(entorno)
        self.columnas = len(entorno[0])
        self.meta = self.encontrar_meta()

    def encontrar_meta(self):
        """Se encuentra la posición meta (M)"""
        # Logica para la meta
        pass

    def es_valido(self, x, y):
        """Se verifica la posicion valida"""
        # Logica para la posicion

    def calcular_utilidad(self, ruta):
        """La mejor ruta acumulada"""
        # Logica para calcular la utilidad
        pass

    def encontrar_ruta_optima(self, inicio):
        """Se encuentra la mejor ruta BFS"""
        # Logica para la ruta optima
        pass

    def mostrar_ruta(self, ruta):
        """Se muestra la mejor ruta del agente"""
        # Logica para mostrar la ruta
        pass

# Define la ruta establecida
entorno = [
    ['#', '5', '2', '#', '#'],
    ['#', '1', '#', '3', '#'],
    ['#', '4', '2', '6', '#'],
    ['#', '#', '7', '1', 'M'],
    ['#', '#', '#', '#', '#']
]

# Creación y ejecución del agente
agente = AgenteSeleccionRutas(entorno)
inicio = (1, 1)  # Primera posición del agente
ruta_optima = agente.encontrar_ruta_optima(inicio)

if ruta_optima:
    print("Ruta óptima encontrada:")
    agente.mostrar_ruta(ruta_optima)
else:
    print("No se encontró una ruta válida.")