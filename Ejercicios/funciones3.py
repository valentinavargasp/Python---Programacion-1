#Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma. Repetir la carga e impresion de la suma 5 veces. Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.

def carga_suma () :
    valor1 = int(input('Ingrese valor 1: '))
    valor2 = int(input('Ingrese valor 2: '))
    suma = valor1 + valor2
    print('La suma de los valores es: ' , suma)

def separacion () :
    print('***************************************')

#programa principal
for x in range (5) :
    carga_suma()
    separacion()