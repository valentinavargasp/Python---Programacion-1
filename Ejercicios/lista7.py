#Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.

lista = []
for x in range (5) :
    valor = int(input('Ingrese un valor: '))
    lista.append(valor) # Para agregar un valor por cada recorrido

mayor = lista[0] # Para identificar el mayor de una lista primero tomamos como referencia el 1er elemento, considerando a este en principio como el mayor de la lista.

for x in range (1,5) :
    if lista[x] > mayor :
        mayor = lista[x]

print('Lista completa: ', lista)
print('Valor mayor de la lista: ', mayor)
