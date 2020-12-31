#Ejercicio 15.- Programa que calcule el m.c.d. de dos números A y B (A>=B). Algoritmo:
#1. Hacer dd = A y d = B.
#2. Calcular q cociente entero de la división de dd por d y el resto r.
#3. Si r != 0 hacer dd = d y d = r e ir al paso 1o. Si r = 0, d es el m.c.d.

a = int(input("Ingresa un numero:"))
b = int(input("Ingresa un segundo numero:")) 

if a >= b and b > 0:
    dd = a
    d = b
    q = int(dd / d)
    r = int(dd % d)
    while r != 0:
        dd = d
        d = r
        q = int(dd / d)
        r = int(dd % d)

    print("El M.C.D de {} y {} es: {}".format(a,b, d))
else:
    print("operacion invalida!! ")
