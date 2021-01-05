#Ejercicio 18.- En el supermercado de la esquina colocan las latas de conservas apiladas
#triangularmente. Esto trae bastantes problemas a la hora de hacer los pedidos, ya que
#quieren un número de latas de manera que no sobre ni falte ninguna. Así, 6 latas se
#pueden apilar triangularmente de la siguiente manera.
#  *
# * *
# * * *
#Si tuvieran 7 latas, no podrían apilarse de forma triangular, ya que sobraría una.
#Escribir un programa, que dado un número natural, compruebe si es adecuado para
#montar pilas triangulares.

numero = int (input (" Ingresa un numero: "))


posible = True

i = 1
if numero<=0:
    posible = False
else:
    while numero > 0 and posible :
        if numero >= i:
            numero -= i
            i += 1
        else:
            posible = False

if posible:
    print(" Si se puede montar filas en forma triangular ")
else:
    print(" No es posible, intente con otro numero!! ")
