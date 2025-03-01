import random

class AgentePatrullaje:
    def __init__(self, ruta):
        self.ruta = ruta  # Primera ruta 
        self.posicion_actual = 0  # Primera Posición
        self.direcciones = ["este", "oeste", "norte", "sur"]  # Direcciones para cambiar

    def detectar_obstaculo(self):
        """Se simula la detección de obstaculo"""
        # Probabilidad de encontrar un obstaculo 20%
        return random.random() < 0.2

    def cambiar_direccion(self):
        """Cambio de dirección de forma aleatoria"""
        return random.choice(self.direcciones)

    def patrullar(self):
        """Patrulla para recorrer la ruta"""
        while self.posicion_actual < len(self.ruta):
            print(f"Posición actual: {self.ruta[self.posicion_actual]}")
            if self.detectar_obstaculo():
                nueva_direccion = self.cambiar_direccion()
                print(f"¡Un obstáculo detectado! Cambio de dirección a → {nueva_direccion}")
            else:
                print("Avanzando a la siguiente ruta")
                self.posicion_actual += 1

# Rutas donde pasara
ruta = ["Punto 1", "Punto 2", "Punto 3", "Punto 4", "Punto 5"]

# Creación y ejecucion del agente
agente = AgentePatrullaje(ruta)
agente.patrullar()