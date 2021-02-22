"""Ejercicio 49.- Mediante el generador de números aleatorios generar un texto (mayúsculas -65 a 90- y
minúsculas -97 a 122-) de 250 caracteres. Convertir todo a mayúsculas. Ver cuántas A, B,
C...Z hay en el texto.
El texto debe aparecer en 5 líneas de 50 caracteres cada una al principio de la pantalla y a
doble espacio."""

from random import choice
from tabulate import tabulate
parrafo = ""

for i in range(250):
    texto = choice([i for i in range(65,122) if i not in [91, 92, 93, 94, 95, 96]])
    parrafo += chr(texto).upper()

letras_aux = { 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0,
'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

for i in range(len(parrafo)):
    letras_aux[parrafo[i]] += 1

print()

for i in range(len(parrafo)):
    print(parrafo[i], end ="")
    if (i + 1) % 50 == 0:
        print('\n\n')


tabla = { "Letras Mayuscula": letras_aux.keys(), "Cantidad de Apariciones":letras_aux.values()}

print(tabulate(tabla, tablefmt ='fancy_grid', numalign = 'center', colalign=("right",)))