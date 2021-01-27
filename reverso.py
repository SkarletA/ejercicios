#Ejercicio 21.-Escribe un programa que, dado un número entero positivo y lo devuelva al revés.
#Por ejemplo, si el número de entrada es 1234, la rutina debería devolver 4321.

numero = int(input('Ingresa un numero positivo: '))
n = numero

acum = 0
while(n > 0):
    a = n % 10
    acum = (acum * 10) + a
    n //= 10
    
print("El reverso de {} es {}".format(numero, acum))



