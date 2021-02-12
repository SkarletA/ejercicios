""" Ejercicio 36.- Generar 30 números entre el 1 y el 99 y dar como resultados de salida:
a) Número más alto.
b) Número más bajo.
c) Media aritmética.
d) Moda.
e) Mediana.
f) Cantidad de 1,2...10 y sus porcentajes."""

import random

numero = []
numero_mayor = 0
numero_menor = 100
cont_mayor = 0
cont_menor = 0

#Generando los 30 numeros en un rango del 1 al 99
for i in range(30):
    n = random.randrange(1, 99)
    numero.append(n)


for i in numero:
    #Obteniendo el valor numero mas alto  
    if numero_mayor < i:
        numero_mayor = i
        cont_mayor = 1
    elif numero_mayor == i:
        cont_mayor += 1

    #Obteniendo el valor numero mas bajo         
    if numero_menor > i:
        numero_menor = i
        cont_menor = 1
    elif numero_menor == i:
        cont_menor+= 1

print(numero)
print(f"EL numero menor es: {numero_menor}")
print(f"EL numero mayor es: {numero_mayor}")

#Obteniendo la Media aritmetica
acum = 0
for i in range(30):
    acum += numero[i]
    media = (acum  / len(numero))
print("La Media es: {}".format(round(media, 2)))

#Obteniendo la Moda
repeticiones = 0                                                                         
for i in numero:                                                                              
    apariciones = numero.count(i)                                                             
    if apariciones > repeticiones:                                                       
        repeticiones = apariciones                                                                                                                                             
moda = []                                                                               
for i in numero:                                                                              
    apariciones = numero.count(i)                                                             
    if apariciones == repeticiones and i not in moda:                                   
        moda.append(i) 

if len(moda) != len(numero):
    print("La Moda es: {} ".format(moda))
else:
    print ("No hay moda")

#Obteniendo la Mediana
numero.sort()
longitud = len(numero)

if longitud % 2 == 0:
    mediana = (numero[int(longitud /2)-1]+ numero[int(longitud / 2)]) / 2
else:
    mediana = numero[int(longitud / 2)]

print("La Mediana es: {}" .format(mediana))

# Obteniendo la Cantidad de 1,2...10 y sus porcentajes

cont = [0 for x in range(10)]
for i in range(len(numero)):
    if numero[i] <= 10:
        cont[numero[i] - 1] += 1

for i in range(len(cont)):
    porcentaje = (cont[i] *100) / len(cont)
    print(f" El numero {i + 1} esta {cont[i]} veces y su porcentaje es: {porcentaje} % ")
