#Componentes de tipo LISTA
lista = [[1, 1, 1, 1, 1] , [2, 2, 2, 2, 2]]

#Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.

#Si cargáramos los datos por asiganción sería algo como esto:
alumnos=["juan", "ana", "luis"]
nota=[[10,8], [6,5], [2,8]]

#Cargando por teclado :
nombres = []
notas = []
for x in range (3) :
    name = input('Ingrese nombre del alumno: ')
    nombres.append(name)
    #Lo nuevo se presenta cuando queremos añadir elementos a la lista notas, lo hacemos con el mismo método append pero le pasamos como parámetro una lista con dos elementos:
    note1 = int(input('Ingrese la primer nota: '))
    note2 = int(input('Ingrese la segunda nota: '))
    notas.append([note1, note2])
#Cuando imprimimos el nombre lo accedemos por un solo subíndice, pero para acceder a cada una de las notas debemos indicar dos subíndices, el primer subíndice es con respecto a que elemento accedemos de la lista principal y el segundo subíndice hace referencia a la lista contenida en dicha componente:
for x in range (3) :
    print(nombres[x], notas[x] [0] , notas[x] [1])