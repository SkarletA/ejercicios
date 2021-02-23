"""Ejercicio 50.- Introducid un texto por teclado (de 250 caracteres). Se debe realizar un programa que
cuente el número de preposiciones existentes en dicho texto, listando la frecuencia de cada
una de ellas.
El texto debe aparecer en cinco líneas de 50 caracteres cada una al principio de la pantalla
y a doble espacio. A continuación se indicará el número total de preposiciones y después
una lista de todas las preposiciones y cuántas veces aparece cada una."""

from tabulate import tabulate
parrafo = str (input (' Escribe un parrafo de 250 caracteres: ')).lower()

print()

for i in range(len(parrafo)):
    print(parrafo[i], end ="")
    if (i + 1) % 50 == 0:
        print('\n\n')

if len(parrafo) == 250:
    preposiciones = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde','durante', 'en' ,'entre',
    'hacia', 'hasta', 'mediante', 'para', 'por', 'según','sin', 'so', 'sobre', 'tras','versus', 'vía']
    array = [0 for x in range(len(preposiciones))]
    for i in range(len(preposiciones)):
        array[i] = parrafo.count(f' {preposiciones[i]} ')
        if parrafo.startswith(f'{preposiciones[i]} '):
            array[i] += 1
    suma = sum(array)
else:
    print('Error, vuelva a intentarlo el texto debe ser de 250 caracteres ')


print(f'El numero total de preposiciones es : {suma}')

tabla = { "Preposiciones": preposiciones, "Cantidad de Apariciones":array}

print(tabulate(tabla, headers = 'keys', tablefmt ='fancy_grid', numalign = 'center'))