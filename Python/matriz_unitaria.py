"""Ejercicio 32.- Programa que genera e imprime una matriz unitaria de orden N. Una matriz unitaria
de orden N es la que tiene N filas y N columnas con todas sus componentes a 0, excepto
las de su diagonal principal que están a 1."""

n = int(input(' Ingresa el orden de la matriz: '))

matriz = []

for fila in range(n):
    filas = []
    for columna in range(n):
        if fila == columna:
            filas.append(1)
        else:
            filas.append(0)
    matriz.append(filas)


for fila in range(n):
    for columna in range(n):
        matriz_unitaria=str(matriz[fila][columna])
        print(matriz_unitaria.rjust(3, ' '), end=' ')
    print()
print()