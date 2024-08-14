#Se tiene que cargar la siguiente información: · Nombres de 3 empleados · Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses. Confeccionar el programa para:
#a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado. b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
# c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses 
# d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

nombres = []
sueldos = []
total_sueldos = []

#En el primer for realizamos la carga de cada nombre de empleado y sus tres últimos sueldos, en la lista nombres añadimos strings y en la lista sueldos añadimos otra lista con tres enteros que representan los sueldos:
for x in range(3) :
    name = input('Ingrese el nombre del empleado: ')
    nombres.append(name)
    sueldo1 = int(input('Ingrese el primer sueldo: '))
    sueldo2 = int(input('Ingrese el segundo sueldo: '))
    sueldo3 = int(input('Ingrese el tercer sueldo: '))
    sueldos.append([sueldo1, sueldo2, sueldo3])
#En el segundo ciclo repetitivo generamos automáticamente la lista total_sueldos (es decir no cargamos por teclado), este valor resulta de sumar los tres sueldos de cada empleado que se encuentran en cada una de las listas contenidas en la lista sueldos:
for x in range (3) :
    total = sueldos[x][0] + sueldos[x][1] + sueldos[x][2]
    total_sueldos.append(total)
#Imprimimos ahora el nombre del empleado seguido por el ingreso total en sueldos de los últimos tres meses:
for x in range (3) : 
    print (nombres[x] , total_sueldos[x])
#Finalmente el problema requiere mostrar el nombre del empleado que recaudó más en sueldos en los últimos tres meses. Iniciamos dos variables previas al for indicando en una la posición de importe en sueldos mayor y en otra dicho importe. Hacemos la suposición antes de ingresar al for que el mayor está en la posición 0:
posmayor = 0
mayor = total_sueldos[0]
#Disponemos un for cuya variable se inicia en 1 y dentro del for controlamos el importe del total de sueldos si supera al que hemos considerado mayor hasta ese momento "mayor" procedemos a actualizar las dos variables: mayor y posmayor:
for x in range (1, 3) :
    if total_sueldos[x] > mayor :
        mayor = total_sueldos[x]
        posmayor = x
#Finalmente cuando salimos del ciclo procedemos a mostrar el nombre del empleado que recaudó más en los últimos tres meses:
print("Empleado con mayores ingresos en los ultimos tres meses: ")
print(nombres[posmayor])
print("con un ingreso de",mayor)