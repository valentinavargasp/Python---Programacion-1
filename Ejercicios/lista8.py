# Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

lista = []
for x in range (5) :
    valor = int(input('Ingrese un valor: '))
    lista.append(valor)

menor = lista[0] 
position = 0

for x in range (1,5) :
    if lista[x] < menor :
        menor = lista[x]
        position = x #Si quiero marcar la posición sin validar el 0 pongo position = x+1.

print('Lista completa: ', lista)
print('Valor menor de la lista: ', menor)
print('Posición del menor de la lista: ', position)