# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def retornar_superficie (lado) :
    sup = lado * lado
    return sup #el valor devuelto por la función retornar_superficie se almacena en la variable superficie.

#Bloque principal del programa

valor = int(input('Ingrese el valor del lado del cuadrado: '))
superficie = retornar_superficie(valor)
print('La superficie del cuadrado es: ', superficie)
#La función retornar_superficie recibe un parámetro llamado lado, definimos una variable local llamada sup donde almacenamos el producto del parámetro lado por sí mismo. La variable local sup es la que retorna la función mediante la palabra clave return. 