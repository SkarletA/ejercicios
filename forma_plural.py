"""Ejercicio 46.- Escribir un programa que devuelve la forma plural de la palabra española que se le
pase."""

p = str (input (' Ingresa una palabra: '))
palabra = p

vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = ['d', 'j', 'l', 'n', 'r']

letra = palabra[len(palabra)-1]

def termina_en(letra, arreglo):
    esta = False
    i = 0
    while (i< len(arreglo) and not esta):
        if arreglo[i] == letra:
            esta = True
        i += 1
    return esta

if termina_en(letra, vocales):
    palabra += 's'
elif termina_en(letra, consonantes):
    palabra += 'es'
elif letra == 'z':
    palabra = palabra.replace('z', 'ces')
else:
    print("Error intenta con otra palabra ")

print(f"El plural de la palabra {p} es {palabra}")