#Funciones con parámetros.
# Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.

def mostrar_mensaje (mensaje) :
    print('*******************************')
    print(mensaje)
    print('*******************************')

def carga_suma (a, b) :
    suma = a + b
    print('La suma de los valores es: ', suma)

#Programa principal:
mostrar_mensaje('El programa calcula la suma de dos valores.')

print('Ingrese valores.')
a = int(input('Ingrese valor a: '))
b = int(input('Ingrese valor b: '))

carga_suma(a,b)

mostrar_mensaje('Gracias por utilizar este programa.')