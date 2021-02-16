"""Ejercicio 38.- Llenar una tabla de 10 posiciones con números enteros comprendidos entre el 1 y el
99. Ordenar dicha tabla de menor a mayor y visualizarla por pantalla de la forma
siguiente: """

from tabulate import tabulate
import random

numero = []


for i in range(10): 
    n = random.randrange(1, 99)
    numero.append(n)


numero_ordenado = sorted(numero)

print()

tabla = { "Tabla_Inicial":numero, "Tabla_Ordenada":numero_ordenado}

print(tabulate(tabla, headers = 'keys', tablefmt ='fancy_grid', numalign = 'center'))