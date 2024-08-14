#Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

lista = []
for x in range (5):
    valor = int(input('Ingrese valor: '))
    lista.append(valor)
mayor = lista[0]
for x in range (1,5):
    if lista[x] > mayor:
        mayor = lista[x]
print('La lista es: ', lista)
print('El mayor es: ', mayor)
#Contamos las veces que se repite el mayor.
cantidad = 0 #contador
for x in range(5):
    if lista[x] == mayor:
        cantidad = cantidad+1
if cantidad > 1 :
    print('El número mayor se repite estas veces: ', cantidad)
    
    #Podemos hacer: 
    cantidad_repetida = lista.count (23)
    print('La cant de veces que se repite el 23 es: ', cantidad_repetida)
