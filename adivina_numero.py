""" Ejercicio 35.- Generar un número de cuatro cifras (no debe repetirse ninguna de ellas).
Realizar un programa para adivinar el número anterior. Se introducirá otro número de
cuatro cifras (sin repetir ninguna) y se comparará con el generado anteriormente. Si
coincide la cifra y la posición se indicará con el signo “+”, si coincide sólo la cifra (y no
la posición) se indicará con el signo “-”.
Ej:
7 2 1 4 (número generado, que no aparecerá en pantalla)
2 0 6 4 (número que introduce el usuario)
A la derecha del número introducido aparecerá un signo “+” (el 4 está acertado y
además está en su sitio) y un signo “-” el 2 está acertado, pero no está en su sitio.
Se darán diez oportunidades para adivinar el número, si no se consigue en este plazo se
mostrará dicho por pantalla.
Tanto si se adivina el número como si no se dará la posibilidad de jugar de nuevo."""

import random

volver_jugar = True
while (volver_jugar):

    v = []

    while (len(v) < 4):
        numero = random.randrange(1, 9)
        if numero not in v:
            v.append(numero)

    no_gano = True
    intentos = 0

    while (intentos < 10 and no_gano):
        n = int (input("Ingrese un numero de 4 cifras : "))
        num = []
        intentos += 1

        while(n > 0):
            aux = n % 10

            if aux not in (num):
                num.insert(0, (aux))
            n //= 10

        if len(num) != 4:
            print("Error, numero invalido!! tiene que ser de 4 cifras.!!! ")

        else:
            count = 0

            for i in range(4):
                j = 0
                acertado_1 = True
                acertado_2 = True
                acertado = True

                while (acertado and j < 4):
                    if v[j] == num[i]:
                        if i == j :
                            acertado_1 = False
                            acertado = acertado_1
                            count += 1

                        else:
                            acertado_2 = False
                            acertado = acertado_2
                    j += 1

                if acertado_1 == False:
                    print(f"{num[i]}+ ", end = " ")

                elif acertado_2 ==False:
                    print(f"{num[i]}- ", end = " ")

                else:
                    print(f"{num[i]} ", end = " ")

            if count == 4:
                no_gano = False
            print()

    if no_gano:
        numero_random = "".join(map(str, v))
        print(f"Oh no perdiste! no acertaste el numero correcto era: {numero_random} ")  
    
    usuario = str(input("Quieres volver a jugar, responda Si o No?: "))
    
    if usuario != "Si":
        volver_jugar = False