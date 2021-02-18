"""Ejercicios 42.- Hacer un programa que haga “eco” de la entrada poniendo cada palabra en una
línea. """

frase = str (input (" Ingrese una oracion: "))

m = []

palabra = []

for i in range(len(frase)):
    if frase[i] == ' ' :
        m.append(palabra)
        palabra = []
    else:
        palabra.append(frase[i])

m.append(palabra)

for i in range(len(m)):
    print("".join(m[i]))