"""Ejercicio 41.- Hacer un programa que hace “eco” del flujo de entrada y convierte las palabras en
palabras iguales que comienzan con letra mayúscula.
Ejemplo:
“cáceres patrimonio de la humanidad”
“Cáceres Patrimonio De La Humanidad”"""

palabra = str (input (" Ingrese una oracion: \n "))
palabras = []

espacio = True
for i in range(len(palabra)):
    if palabra[i] == " ":
        palabras.append(palabra[i])
        espacio = True
    else:
        if espacio:
            palabras.append(palabra[i].capitalize()) 
            espacio = False
        else:
            palabras.append(palabra[i])


print("".join(map(str, palabras)))