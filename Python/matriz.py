""" Ejercicio 30.- Programa que carga una matriz de 5 filas y 10 columnas con números enteros
imprimiendo los valores máximo y mínimo y sus posiciones dentro de la tabla. """

import random

matriz = []

for i in range(5):
    fila = []
    for j in range(10):
        fila.append(random.randrange(-50, 50))
    matriz.append(fila)


mayor = -51
mayor_fila = 0
mayor_columna = 0
for i in range(5):
    for j in range(10):
        if mayor < matriz[i][j]:
            mayor_fila = i+1
            mayor_columna = j+1
            mayor = matriz[i][j]

menor = 51
menor_fila = 0
menor_columna = 0
for i in range(5):
    for j in range(10):
        if menor > matriz[i][j]:
            menor_fila = i+1
            menor_columna = j+1
            menor = matriz[i][j]
        
print("El numero mayor es: {} y se encuentra en la posicion [{}][{}] ".format(mayor, mayor_fila, mayor_columna))
print("El numero menor es: {} y se encuentra en la posicion [{}][{}] ".format(menor, menor_fila, menor_columna))

for i in range(5):
    print(matriz[i])