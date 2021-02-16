"""Ejercicio 39.- Llenar dos tablas de 10 posiciones cada una con números enteros comprendidos entre
el 1 y el 99. Ordenar dichas tablas y fusionarlas en una tercera de 20 posiciones, de forma
que vaya quedando ordenada de menor a mayor. Ir visualizando el proceso."""

from tabulate import tabulate
import random

tabla_uno = []
tabla_dos = []

for i in range(10):
    n1 = random.randrange(1, 99)
    n2 = random.randrange(1, 99)
    tabla_uno.append(n1)
    tabla_dos.append(n2)

tabla_resultado = [0 for x in range(len(tabla_uno) + len(tabla_dos))]


for i in range(10):
    tabla_resultado[i] = tabla_uno[i]

j = 0
for i in range(10, 20):
    tabla_resultado[i] = tabla_dos[j]
    j += 1

for num in range(len(tabla_resultado)-1, 0, -1):
    for n in range(num):
        if tabla_resultado[n] > tabla_resultado[n+1]:
            r = tabla_resultado[n]
            tabla_resultado[n] = tabla_resultado[n+1]
            tabla_resultado[n+1] = r


print()

tabla = { "Tabla_1":tabla_uno, "Tabla_2":tabla_dos, "T_Resultado":tabla_resultado}

print(tabulate(tabla, headers = 'keys', tablefmt ='presto', numalign = 'center'))


