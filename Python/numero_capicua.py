"""Ejercicio 29.- Dado un número entero positivo de 10 cifras. Programa que compruebe si un
número es capicúa utilizando vectores."""

numero = int(input('Ingrese un numero entero de 10 cifras: '))
n = numero
vector = []


while(n>0):
    vector.append(n%10)
    n //= 10


if len(vector) != 10:
    print("Error, numero invalido!! tiene que ser de 10 cifras.!!! ")
else:
    capicua = True
    j=9
    for i in range(5):
        if vector[i] != vector[j]:
            capicua = False
        j-=1

    if capicua:
        print('El numero: {} es capicua '.format(numero))
    else:
        print('El numero: {} no es capicua '.format(numero))