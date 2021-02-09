"""Ejercicio 33.- Programa que lee un vector de N elementos y rota todas sus componentes un lugar
hacia su derecha. Teniendo en cuenta que la última componente se ha de desplazar al
primer lugar."""

import random

n = int(input("Ingrese el tamano del vector: "))
vector = []
aux_vector = [0 for x in range(n)]

for i in range(n):
    numero = random.randrange(-50, 50)
    vector.append(numero)

for i in range(n):
    if i == n-1:
        aux_vector[0] = vector[n-1]
    else:
        aux_vector[i+1]= vector[i]

print(f"El siguiente vector {vector} es desplazdo un numero a la derecha quedando asi: {aux_vector} ")
