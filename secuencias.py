"""Ejercicio 47.- Escribir un programa que lea una secuencia de nombres, uno por línea, los ordene
y, a continuación , los presente por pantalla."""

n = int (input (' Ingrese el numero de la secuencia: '))
array_nombres = []

for i in range(n):
    nombre = str (input(' Ingresa un nombre : ').lower())
    array_nombres.append(nombre)


for palabra in range(len(array_nombres)-1, 0, -1):
    for j in range(palabra):
        if (array_nombres[j] > array_nombres[j+1]):
            aux_nombre = array_nombres[j]
            array_nombres[j] = array_nombres[j+1]
            array_nombres[j+1] = aux_nombre

print(array_nombres)