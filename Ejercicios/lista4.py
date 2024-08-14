#Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.

lista = [1500, 70, 120, 30, 245, 68, 720, 320]
cantidad = 0
x = 0
while x < len(lista) :
    if lista[x] >100 :
        cantidad = cantidad+1
    x = x+1
print('La lista de valores es: ', lista)
print('La cantidad de valores mayores a 100: ', cantidad)