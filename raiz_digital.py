""" Ejercicios 20.- Dado un número natural N, se calcula la raíz digital de N sumando los dígitos que
lo componen. El proceso se repite sobre el nuevo número hasta que el resultado
obtenido tiene un sólo dígito. Este último número es la raíz digital del número N.
Ejemplo: 347 ->3 + 4 + 7 = 14 -> 1 + 4 -> 5 -> Raíz digital (347) = 5.
Escribir un programa que calcule la raíz digital de un número. """

n= int(input("Escribir un numero natural: "))

while (n //10 != 0):
    acum=0
    aux_n=n
    while (aux_n // 10 != 0):
        mod=aux_n%10
        acum+=mod
        aux_n //= 10
    
    acum+=aux_n
    n = acum
print("La raiz digital es :".format(n))