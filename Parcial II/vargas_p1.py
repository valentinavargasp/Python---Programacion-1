# Ejercicio 1
"""Escribir un programa en Python que permita ingresar n cantidad de empleados por teclado. Los datos deberán ser almacenados en dos listas, una con los nombres de los empleados y otra con sus respectivos sueldos . Luego, implemente las siguientes funciones:
1. calcular_promedio_sueldos: toma como argumento la lista de sueldos de los empleados y devuelve el promedio de los sueldos.
2. obtener_empleado_sueldo_max: toma como argumento la lista de sueldos de los empleados y la lista de nombres de los empleados y devuelve el nombre del empleado con el sueldo más alto.
3. ordenar_por_sueldo: toma como argumento la lista de nombres de empleados y la lista de sueldos y devuelve dos listas ordenadas de menor a mayor, una con los nombres de los empleados y otra con sus respectivos sueldos.
El programa deberá utilizar estas funciones para imprimir en pantalla el sueldo promedio de los empleados y el nombre del empleado con el sueldo más alto."""


def calcular_promedio_sueldos (sueldos) :
    suma = 0
    for x in range (len(sueldos)) : # Recorro la lista de sueldos para sumarlos.
        suma = suma+sueldos[x]
    promedio = suma/len(sueldos)
    return promedio

def obtener_empleado_sueldo_max (sueldos , empleados) :
    mayor_sueldo = sueldos[0]
    empleado = empleados[0]
    for x in range(1 , len(sueldos)) : # Recorro la lista de sueldos desde el segundo elemento
        if sueldos[x] > mayor_sueldo :  # Si encuentra un sueldo mayor, actualiza el mayor sueldo y el empleado correspondiente
            mayor_sueldo = sueldos[x]
            empleado = empleados[x]
    return  [empleado , mayor_sueldo]  # Retorna el empleado con el mayor sueldo y el valor del mayor sueldo

def ordenar_por_sueldo (sueldos, empleados) :
    #Algoritmo de ordenamiento burbuja.
    for k in range (len(sueldos)) :
        for x in range (n-1) :
            if sueldos[x] > sueldos[x+1] :
                aux1 = sueldos[x]
                sueldos[x] = sueldos [x+1]
                sueldos[x+1] = aux1
                aux2 = empleados[x]
                empleados[x] = empleados[x+1]
                empleados[x+1] = aux2
    return [empleados , sueldos]


#Bloque principal del programa: 

empleados = []
sueldos = []
n = int(input('Ingrese la cantidad de empleados: '))
for x in range (n):
    empleado = input('Ingrese el nombre del empleado: ')
    empleados.append(empleado)
    sueldo = float(input('Ingrese el sueldo del empleado: '))
    sueldos.append(sueldo)

# Le asigno las funciones a una variable.

promedio_sueldos = calcular_promedio_sueldos(sueldos) 
empleado_mayor_sueldo = obtener_empleado_sueldo_max(sueldos , empleados)
sueldos_ordenados = ordenar_por_sueldo(sueldos, empleados)

#Imprimo los resultados.
print('*****************************************************')
print('El promedio de sueldos es: ', promedio_sueldos) # Imprimo el valor de la variable que almacena la función.
print('El empleado con mayor sueldo es: ', empleado_mayor_sueldo[0], empleado_mayor_sueldo[1])

print("Lista de empleados y sus respectivos sueldos ordenados de menor a mayor: ")
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])
print('*****************************************************')