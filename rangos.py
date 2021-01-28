#Ejercicio 23: Generar 10 valores entre 5 y 50. Almacene esos valores en una lista.random

import random

valores = []
for s in range(10):
    rand_num = random.randint(5, 50)
    valores.append(rand_num)

print("los siguientes valores aleatorios entre 5 y 50 son: {}".format(valores))