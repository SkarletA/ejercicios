"""Ejercicios 40.- Mediante el generador de números aleatorios llenar una tabla de dos dimensiones
(10,10) con números enteros comprendidos entre el 1 y el 99. La tabla deberá visualizarse
en pantalla.
Ordenar la matriz anterior por filas y columnas, de menor a mayor, y visualizar la tabla."""
import random
from tabulate import tabulate

matriz = []

for fila in range(10):
    numero = []
    for columna in range(10):
        numero.append(random.randrange(1, 99))
    matriz.append(numero)

print(" Tabla Inicial")

for fila in range(10):
    for columna in range(10):
        mt=str(matriz[fila][columna])
        print(mt.rjust(3, ' '), end=' ')
    print()
print()

m = [0 for x in range(100)]
x = 0
for fila in range(10):
    for columna in range(10):
        m[x] = matriz[fila][columna]
        x += 1

for num in range(len(m)-1, 0, -1):
    for n in range(num):
        if m[n] > m[n+1]:
            r = m[n]
            m[n] = m[n+1]
            m[n+1] = r

x = 0
for fila in range(10):
    for columna in range(10):
        matriz[fila][columna] = m[x]
        x += 1

print(" Tabla Ordenada ")

for fila in range(10):
    for columna in range(10):
        mo=str(matriz[fila][columna])
        print(mo.rjust(3, ' '), end=' ')
    print()
print()