#Ejercicio 22: Generar  20 valores pares entre 0 y 100
import random
par = []

for i in range(20):
    numero = random.randrange(0, 100, 2)
    par.append(numero)

print("los siguientes numeros de esta lista: {} son valores pares".format(par))