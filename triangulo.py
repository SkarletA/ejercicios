#Ejercicio 17.- Escribe un programa que lea un número e imprime un triángulo de números de la
#forma siguiente. Si el número leído es 4, imprimirá:

numero = int ( input (" Ingresa un numero: "))

for i in range(1, numero+1):
    for j in range(1, i+1):
        print(str(i), end=" ")
    print()