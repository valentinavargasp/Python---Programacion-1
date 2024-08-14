#Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

sueldos = []
for x in range (5) :
    valor = int(input('Ingresa sueldo: '))
    sueldos.append(valor)
print('Lista sin ordenar: ', sueldos) 
#Se utilizan dos for. Un recorrido exterior y uno interior.
#ALGORITMO DE ORDENAMIENTO:
for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux
print('Lista ordenada de sueldos: ', sueldos)