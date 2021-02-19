"""Ejercicio 44.- Leer 5 cadenas, almacenarlas en un array separadas por blanco y a continuación
visualizarla."""

array = []

for i in range(5):
    palabras = str (input (' Ingrese una palabra : '))
    array.append(palabras)
    array.append(' ')

print(array)