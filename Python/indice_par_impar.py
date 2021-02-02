"""Ejercicio 27.- Programa que genere un vector aleatorio y calcule e imprima las
sumas de las componentes de índice par y las de índice impar."""

import random

n = int(input("Ingrese el tamano del vector: "))
vector = []

acum_par = 0
acum_impar = 0


for i in range(n):
    numero = random.randrange(-50, 50)
    vector.append(numero)

print(vector)

for i in range(n):
    if i % 2 == 0:
        acum_par += vector[i]
    else:
        acum_impar += vector[i]

print('La suma de los indice par es: {}'.format(acum_par))
print('La suma de los indice impar es: {}'.format(acum_impar))
