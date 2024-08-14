#Ejercicio 1
"""Diseñaremos un programa que obtendrá números pares desde el número 2. (25%)
Nuestro programa deberá:
a) Solicitar al usuario un valor de tipo entero y guardarlo en una variable.
b) Imprimir los números pares desde el 2 y hasta el valor ingresado por el
usuario (inclusive), según el inciso anterior.
c) Calcular la suma de estos números pares.
d) Imprimir la suma obtenida en el inciso anterior, con el mensaje: “La suma de
los números pares es:” seguida del valor obtenido."""

suma=0
numPar=int(input('Ingrese un número: '))
for x in range (2, numPar+1, 2):
    print(x)
    suma= suma + x
print('La suma de los números pares es:' , suma)


