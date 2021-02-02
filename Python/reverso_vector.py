""" Ejercicio 28.- Programa un vector aleatorio e imprime su inverso. """

import random

n = int(input("Ingrese el tamano del vector: "))
vector = []


for i in range(n):
    numero = random.randrange(-50, 50)
    vector.append(numero)
    invertido = vector[::-1]

print(vector)
print(invertido)