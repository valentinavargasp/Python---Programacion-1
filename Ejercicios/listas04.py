#Listas - Eliminación de elementos.
# Otra característica fundamental de las listas en Python es que podemos eliminar cualquiera de sus componentes llamando al método pop e indicando la posición del elemento a borrar:

#Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.

#lista = [5, 8, 6, 3, 9]
# print(lista)
# lista.pop(0)
# print(lista)
# lista.pop(1)
# print(lista)
# lista.pop(2)
# print(lista)

#Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado. Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa. Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

empleados = []
sueldos = []
cantidad = int(input('Cuantos empleados itene la empresa? '))
for x in range (cantidad) : 
    name = input('Ingrese nombre del empleado: ')
    empleados.append(name)
    sueldo = int(input('Ingrese sueldo del empleado: '))
    sueldos.append(sueldo)
print('Listado completo de empleados: ')

for x in range (len(sueldos)) :
    print (empleados[x], sueldos[x])

position = 0
while position < len(sueldos) :
    if sueldos [position] > 10000 :
        sueldos.pop(position)
        empleados.pop(position)
    else:
        position = position+1

print('Listado de empleaods que cobran 10000 o menos: ')
for x in range (len(sueldos)) :
    print(empleados[x] , sueldos[x])

