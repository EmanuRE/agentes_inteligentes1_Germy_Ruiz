# Problema 1 - Agente de Patrullaje

## Descripción
Crea un agente reflejo que patrulle una ruta predefinida. El agente debe seguir un camino fijo
y reaccionar si detecta un obstáculo, cambiando su dirección de manera aleatoria.

## Funcionamiento
El agente de patrullaje sigue una ruta definida por una lista de puntos. En cada punto, el agente tiene una probabilidad del 20% de detectar un obstáculo. Si se detecta un obstáculo, el agente cambia de dirección de manera aleatoria entre las opciones disponibles: este, oeste, norte y sur. Si no se detecta ningún obstáculo, el agente avanza al siguiente punto de la ruta. (Se hace una ruta predefinida, se detectan los obstaculos, se cambia la dirección y se hace el patrullaje)

# Problema 2 - Agente explorador de mapas (Estado Interno)

## Descripción
Desarrolla un agente que explore un entorno representado como una cuadrícula. El agente
debe recordar las áreas visitadas y evitar repetir caminos ya explorados.

## Funcionamiento
El agente explora un mapa representado como una matriz de `filas x columnas`. En cada paso, el agente verifica las celdas adyacentes (arriba, abajo, izquierda, derecha) y se mueve aleatoriamente a una celda no visitada. Si no hay celdas adyacentes sin visitar, el agente finaliza la exploración.

El problema se compone de un mapa, Posicion actual, Movimiento y Exploración.