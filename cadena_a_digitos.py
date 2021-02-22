"""Ejercicio 48.- Leer una línea de entrada. Descartar todos los símbolos excepto los dígitos.
Convertir la cadena de dígitos en un entero y fijar el valor del entero a la variable n."""

cadena = str (input (" Ingrese una oracion : "))
digitos = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolos = ['$', '%', '&', '#', '@', '!', '/', '?' , '-', '=', '+', '*', ':', ';', ',' , ' ']

n = 0
for i in range(len(cadena)):
    for j in range(len(digitos)):
        if cadena[i] == digitos[j]:
            d = int(cadena[i])
            n = n * 10 + d

print(f"n = {n}")