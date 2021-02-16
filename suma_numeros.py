"""Ejercicios 37.- Obtener diez números (0..9) mediante el generador de números aleatorios. Con
estos diez números se formarán dos de cinco cifras cada uno.
Sumar los dos números de cinco cifras obtenidos. La suma se realizará cifra a cifra
(unidades, decenas, centenas, etc.), apareciendo los sumandos,
también se indicará si llevas una y aparecerá un "1" encima del sumando correspondiente."""

import random

n = []
numero_uno = []
numero_dos = []

for i in range(10):
    numero = random.randrange(0,9)
    n.append(numero)

for i in range(5):
    numero_uno.append(n[i])
    
for i in range(5, 10):
    numero_dos.append(n[i])   



resultado = [0, 0, 0, 0, 0]
carries = [0, 0, 0, 0, 0]
for j in range(4, -1, -1):
    suma = numero_uno[j]+numero_dos[j]+carries[j]
    if suma > 9:
        if j == 0:
            resultado[j] = suma
        else:
            resultado[j] = suma % 10
            carries[j-1]  = suma // 10
    else:
        resultado[j] = suma

print("La siguiente es una representacion de la suma: ")


def sustituir_ceros(carry):
    if carry == 0:
        return " "
    else:
        return f"{carry}"

print("   ".join(map(sustituir_ceros, carries)))



for j in range(5):
    print(numero_uno[j], end = "   ")
print()

for j in range(5):
    print(numero_dos[j], end ="   ")
print()

print("------------------")

for j in range(5):
    print(resultado[j], end ="   ")
print()