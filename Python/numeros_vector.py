"""Ejercicio 26.- Programa que lee 50 números enteros sobre un vector y obtiene e imprime cuáles
son el mayor y el menor número almacenados y cuántas veces se repiten ambos."""

import random

vector = []
mayor = -51
menor = 51
cont_mayor = 0
cont_menor = 0


for i in range(50):
    numero = random.randrange(-50, 50)
    vector.append(numero)


for i in vector:
    #Obteniendo el valor mayor en el vector    
    if mayor < i:
        mayor = i
        cont_mayor = 1
    elif mayor == i:
        cont_mayor += 1

    #Obteniendo el valor menor en el vector          
    if menor > i:
        menor = i
        cont_menor = 1
    elif menor == i:
        cont_menor+= 1

print("EL numero mayor es {} y se repite {} ".format(mayor, cont_mayor))
print("EL numero menor es {} y se repite {} ".format(menor, cont_menor))
