"""Ejercicios 19.- En el mismo supermercado quieren montar también pilas del mismo número de
latas de alto que de ancho.
* * *
* * *
* * *
Ahora bien no todas las cantidades de latas que pueden apilarse triangularmente pueden
ponerse en estructuras cuadradas. Diseñas un programa que indique si un número
natural es válido para realizar los dos tipos de estructuras. (Un ejemplo válido es el
número 36)."""

numero = int (input (" Ingresa un numero: "))
aux_triangulo = numero

posible_cuadrado = True

i = 2
if numero < 4:
    posible_cuadrado = False
else:
    while numero > 4 and posible_cuadrado:
        if numero >= i*2+1:
            numero = numero-(i*2+1)
            i+=1
        else:
            posible_cuadrado = False


posible_triangulo = True

j= 1
if aux_triangulo <= 0:
    posible_triangulo = False
else:
    while aux_triangulo > 0 and posible_triangulo :
        if aux_triangulo>= j:
            aux_triangulo-= j
            j += 1
        else:
            posible_triangulo = False



if posible_cuadrado and posible_triangulo:
    print(" Si se puede montar filas en forma triangular y cuadrada")
else:
    print(" No es posible, intente con otro numero!!")