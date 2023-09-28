#  Andres Mayorga
# Proyecto integrador parte 4

import readchar
import os
from typing import List, Tuple

def limpiar_pantalla_mostrar_mapa(matriz: List[List[str]]):  # Agrega matriz como argumento
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
    for fila in matriz:
        print(''.join(fila))  # Imprimir la matriz

def cadena_a_matriz(cadena_mapa):
    lineas = cadena_mapa.strip().split('\n')  # Dividir la cadena en líneas
    matriz = [list(linea) for linea in lineas]  # Dividir cada línea en caracteres
    return matriz

def main_loop(matriz: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
  
    px, py = posicion_inicial #Posiciones iniciales
 
    matriz[px][py] = 'P'
    
    while (px, py) != posicion_final:
        limpiar_pantalla_mostrar_mapa(matriz)
        # Asignar el caracter 'P' en el mapa a las coordenadas (px, py)
        matriz[px][py] = 'P'
        # Leer la tecla presionada
        key = readchar.readkey()
        nueva_px, nueva_py = px, py
        #validacion teclas
        if key == readchar.key.UP:
            nueva_px -= 1
        if key == readchar.key.DOWN:
            nueva_px += 1
        if key == readchar.key.LEFT:
            nueva_py -= 1
        if key == readchar.key.RIGHT:
            nueva_py += 1 
        #verificar si la posicion nueva es valida, su lo es, actualiza los datos, si no lo es, no actualiza nada.
        if (0 <= nueva_px < len(matriz) and 0 <= nueva_py < len(matriz[0]) and matriz[nueva_px][nueva_py] != '#'):
            matriz[px][py] = '.'   #Actualiza valor pasado de la matriz cuando si se cumplen los terminos 
            px, py = nueva_px, nueva_py #Da nuevo valor de posicion a P 
            matriz[px][py] = 'P'

    print("FELICIDADES!!!" + nombre + " HAZ TERMINADO EL JUEGO!!!")

#Mapa mas estetico
#cadena_mapa = """            
#█.███████████████████
#█...........█...█...█
#█████.███.█.█.███.█.█
#█...█.█...█.█.....█.█
#█.███.█.███████.█.█.█
#█...█.█...█.█...█.█.█
#███.███.█.█.███.███.█
#█.......█...█.....█.█
#█.█.█.█████████.█.█.█
#█.█.█...........█.█.█
#█.█.███████.█████.█.█
#█.█...█.█.█...█.█.█.█
#█.█████.█.█.███.█████
#█.█...█...█.........█
#█.█.███.█.█.███.█.█.█
#█.█...█.█...█...█.█.█
#█████.█.███████████.█
#█.█.█.....█.....█...█
#█.█.█.█████.█████.█.█
#█...............█.█.█
#███████████████████.█
#"""

#Mapa como lo piden en el proyecto
cadena_mapa = """  
#.###################
#.#.......#.#...#.#.#
#.#####.###.#.#.#.#.#
#.....#.......#.....#
#####.#.###.#.#######
#.........#.#.#.....#
###.###.#.#.#.#####.#
#.....#.#.#.#.#.....#
#.#####.###.###.###.#
#.#.#...#.#.....#...#
#.#.###.#.#######.#.#
#.#.....#.......#.#.#
#.#######.#####.#.###
#.#.#...#.#.....#...#
#.#.#.###.#####.###.#
#.#.#.........#.....#
#.#.###.#.#####.###.#
#.#.#...#...#...#.#.#
#.#.###.###.###.#.#.#
#...#...#.....#.#.#.#
###################.#

"""
#Guarda la cadena en la variable matriz
matriz = cadena_a_matriz(cadena_mapa)
posicion_inicial = (0, 1)
posicion_final = (20, 19) 

print("             El JUEGO DEL LABERINTO MISTERIOSO          ")
print("Recuerde que para mover el personaje es con las flechas del teclado"+ " ↑ "+ " ↓ "+ " ← "+ " → ")
print("Inserte su nombre por favor")
nombre=input()

main_loop(matriz, posicion_inicial, posicion_final)
