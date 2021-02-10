"""Ejercicio 34.- Programa que imprime un cuadrado latino de orden N. Un cuadrado latino de orden
N es una matriz cuadrada en la que la primera fila contiene los N primeros números
naturales y cada una de las siguientes N-1 filas contiene la rotación de la fila anterior un
lugar a la derecha.
Ejemplo: Cuadrado latino de orden 4.
1 2 3 4
4 1 2 3
3 4 1 2
2 3 4 1 """

n = int(input("Ingrese el orden de la matriz: "))
matriz =[]


for fila in range(n):
    aux = []
    for columna in range(n):
        if fila == 0:
            aux.append(columna+1)
        else:
            aux.append(0)
    matriz.append(aux)


for fila in range(1, n):
    for columna in range(n):
        if columna == 0:
            matriz[fila][columna] = matriz[fila-1][n-1] 
        else:
            matriz[fila][columna] = matriz[fila-1][columna-1] 


for fila in range(n):
    for columna in range(n):
        aux_matriz = str(matriz[fila][columna])
        print(aux_matriz.rjust(3, ' '), end=' ')
    print()
