#Ejercicios 24.- Escribir un programa que lea un número natural de 4 cifras, no todos iguales.
#Implementa la función Mayor(N), que calcula el mayor número que se puede formar
#con las cifras de N, y la función Menor(N) que calcula el menor número que se puede
#formar con las cifras de N.

numero = int(input('Ingrese un numero natural: '))
n=numero
num=[]

while(n>0):
    num.append(n%10)
    n //= 10


def menor(num):
    num.sort()
    return ''.join([str(i) for i in num])


def mayor(num):
    num.sort(reverse=True)
    return ''.join([str(i) for i in num])


if(len(num) != 4 or num[0]==num[1]==num[2]==num[3]):
    print("Numero incorrecto intenta con otro!!!")

else:
    print("El menor numero es: {} ".format(menor(num)))
    print("El mayor numero es: {} ".format(mayor(num)))