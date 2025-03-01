import random

class AgentePatrullaje:
    def __init__(self, ruta):
        self.ruta = ruta  # Primera ruta 
        self.posicion_actual = 0  # Primera Posición
        self.direcciones = ["este", "oeste", "norte", "sur"]  # Direcciones para cambiar

    def detectar_obstaculo(self):
        """Simula la detección de un obstáculo."""
        # Logica para el obstaculo
        pass

    def cambiar_direccion(self):
        """Cambia la dirección del agente de manera aleatoria."""
        # Logica para el cambio de dirección
        pass

    def patrullar(self):
        """Patrulla la ruta predefinida."""
        # Logica para patrullaje
        pass

# Rutas
ruta = ["Punto 1", "Punto 2", "Punto 3", "Punto 4", "Punto 5"]

# Creación y ejecución del agente
agente = AgentePatrullaje(ruta)
agente.patrullar()