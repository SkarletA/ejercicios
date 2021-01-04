#Ejercicio 16.- Programa que lea dos números N1 y N2 enteros positivos y obtiene su mínimo
#común múltiplo. (Se sabe que el mínimo común múltiplo de dos números es igual a su
#producto N1 * N2 dividido entre su m.c.d).

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un segundo numero: ")) 

if n1 > n2 :
    a = n1
    b = n2
else:
    a = n2
    b = n1

while b:
    mcd = b
    b = a % b
    a = mcd
mcm = int((n1 * n2) / mcd) 
print(" El maximo comun divisor de {} y {} es: {}".format(n1, n2, mcd))
print(" El minimo comun mulltiplo de {} y {} es {}".format(n1, n2, mcm))