"""Ejercicio 45.- Leer una secuencia de nombres, uno por línea, terminado por el valor centinela’$’.
A continuación visualizar los nombres almacenados en el array_nombres nombres."""

array_nombres = []
nombre = str (input(' Ingresa un nombre : '))

while(nombre != '$'):
    array_nombres.append(nombre)
    nombre = str (input(' Ingresa un nombre : '))
print(array_nombres)