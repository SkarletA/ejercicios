"""Ejercicios 31.- Crear una matriz con numeros random. Programa que obtiene e imprime su
matriz traspuesta."""

import random

matriz = []

for i in range(5):
    fila = []
    for j in range(10):
        fila.append(random.randrange(-50, 50))
    matriz.append(fila)

print('Matriz: ', end='\n')
for i in range(5):
    for j in range(10):
        mt=str(matriz[i][j])
        print(mt.rjust(3, ' '), end=' ')
    print()
print()
print('Matriz Transpuesta: ', end='\n')

for j in range(10):
    for i in range(5):
        mt=str(matriz[i][j])
        print(mt.rjust(3, ' '), end=' ')
    print()
        

