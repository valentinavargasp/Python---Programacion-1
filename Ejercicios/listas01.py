#Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.
#Debe quedar claro que cuando intercambiamos las notas para dejarlas ordenadas de mayor a menor debemos intercambiar los nombres para que las listas continúen paralelas (es decir que en los mismos subíndices de cada lista continúe la información relacionada)

#Definimos y cargamos dos listas con cinco elementos cada una: 

alumnos = []
notas = []
for x in range (5):
    name = input('Ingrese el nombre del alumno: ')
    alumnos.append(name)
    note = int(input('Ingrese nota del alumno: '))
    notas.append(note)
#Lo nuevo se presenta cuando ordenamos la lista de notas de mayor a menor. La condición dentro de los dos ciclos repetitivos depende de la lista notas, pero en el caso que se verifique verdadera intercambiamos tanto los elementos de la lista notas como el de la lista alumnos con el fin que continúen paralelas:
for k in range(4):
    for x in range(4-k):
        if notas[x] < notas[x+1]:
            aux1=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux2
for x in range(5):
    print(alumnos[x],notas[x]) #Algo que no habíamos utilizado en Python hasta ahora es imprimir varios datos en la misma línea, esto se logra pasando más de un parámetro a la función print separándolos por una coma.
    