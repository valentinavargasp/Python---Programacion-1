#Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.

lista = []
#Disponemos un ciclo de 5 vueltas
for x in range (5) :
    valor = int(input('Ingrese un valor: '))
    lista.append(valor)
#Imprimimos la lista
print('Lista cargada: ', lista)