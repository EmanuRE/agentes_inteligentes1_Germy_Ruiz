# Problema 1 - Agente de Patrullaje

## Descripción
Crea un agente reflejo que patrulle una ruta predefinida. El agente debe seguir un camino fijo
y reaccionar si detecta un obstáculo, cambiando su dirección de manera aleatoria.

## Funcionamiento
Este es un agente de patrullaje que sigue una ruta definida por un listado de puntos, en cada uno de los puntos, el agente tiene la 
probabilidad de un 20% de detectar un obstaculo. Si en caso se detecta un obstaculo, este agente cambia de dirección de una forma 
aleatoria entre las opciones que tenemos: este, oeste, norte y sur. Si no se detecta ninguno de los obstaculos, el agente se puede mover al siguente pnto de nuestra ruta.(Se hace una ruta predefinida, se detectan los obstaculos, se cambia la dirección y se hace el patrullaje)

# Problema 2 - Agente explorador de mapas (Estado Interno)

## Descripción
Desarrolla un agente que explore un entorno representado como una cuadrícula. El agente
debe recordar las áreas visitadas y evitar repetir caminos ya explorados.

## Funcionamiento
El agente puede explorar un mapa que se presenta en una matriz de "Filas y columnas", en cada uno de los pasos, este agente verifica las celdas que estan adyacentes (arriba, abajo, izquierda, derecha) y este se mueve de forma aleatoria a una celda no visitada. Si en caso no hay celdas adyacentes de visitar, el agente da por finalizada la exploración.

El problema se compone de un mapa, Posicion actual, Movimiento y Exploración.

# Problema 3 - Agente de navegacion automata (Metas)

## Descripción
Crea un agente que tenga como meta encontrar la salida en un laberinto de tamaño 5x5. Debe
buscar la ruta más corta para alcanzar la meta

## Funcionamiento
Este agente se encarga de recibir un laberinto y en forma de matriz y punto de inicio. Despues, usa el algoritmo de BFS para poder explorar las posibles rutas desde el punto de su inciio, hasta llegar a la meta, evitando las paredes. Cuando se encuentra la ruta, este agente muestra el laberinto con la ruta encontrada marcando cada espacio usado con Z.

Se crea un Laberinto por medio de una matriz, se hace un punto de inicio, se busca una ruta y se visualiza la ruta.

# Problema 4 - Agente de Seleccion de rutas (Basado en utilidad)

## Descripción 
Diseña un agente que seleccione la mejor ruta en un entorno con múltiples caminos y valores
de recompensa. El agente debe elegir el camino con mayor utilidad.

## Funcionamiento
Este agente recibe un entorno en forma de matriz y establece un punto de inicio. Usa el algoritmo BFS para poder explorar las posibles rutas desde el primer punto de inicio, hasta llegar a la meta, logrando evitar las paredes. Durante esta exploración, el agente hace el calculo de la utilidad acumulada para cada ruta y selecciona la que da una maxima utilidad. Por ultimo, muestra la ruta mas optima y marca el camino con una Z

Esta formado por Entorno, Punto de Inicio, una busqueda de ruta óptima, se calcula la utilidad y se visualiza la ruta.