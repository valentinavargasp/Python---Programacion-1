#Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.

def cuadrados () :
    print('Programa que calcula el cuadrado: ')
    valor1 = int(input('Ingrese valor: '))
    cuadrado = valor1 * valor1
    print('El cuadrado es: ', cuadrado)

def productos () :
    print('Programa que calcula el producto: ')
    valor1 = int(input('Ingrese valor 1: '))
    valor2 = int(input('Ingrese valor 2: '))
    producto = valor1 * valor2
    print('El producto es: ', producto)

cuadrados()
productos()