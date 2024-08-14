#Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición

sueldos = []
for x in range (5) :
    valor = int(input('Ingresa sueldo: '))
    sueldos.append(valor)
print('Lista sin ordenar: ', sueldos) 
for x in range (4) : #variable auxiliar para precargar y no borrar el valor.
    if sueldos[x] > sueldos [x+1] :
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux
print('Lista con el último elemento ordenado: ', sueldos)