# Ejercicio 2
"""Escribir un programa en Python que permita ingresar n cantidad de palabras por teclado. Los datos deberán ser almacenados en una lista de strings. Luego, implemente las siguientes funciones:
1. encontrar_palabras_con_letra: toma como argumentos la lista de palabras y una letra y devuelve una lista con todas las palabras que contienen esa letra.
2. ordenar_palabras_longitud: toma como argumento la lista de palabras y devuelve una lista con las palabras ordenadas por longitud, de menor a mayor.
El programa deberá utilizar estas funciones para imprimir en pantalla la lista de palabras que contienen determinada letra y la lista de palabras ordenada por longitud.
Desde el bloque principal :
palabras = ingresar_palabras()
letra = input("Ingrese la letra que quiere buscar: ")
palabras_con_letra = encontrar_palabras_con_letra(palabras, letra)
palabras_ordenadas_por_longitud = ordenar_palabras_longitud(palabras)"""


def ingresar_palabras() :
    lista_palabras = []
    n = int(input('Ingrese la cantidad de palabras: ')) #El usuario define la cantidad de palabras por teclado.
    for x in range (n) : #Con esas palabras se crea una lista de 'n' elementos. 
        palabra = input('Ingrese una palabra: ') 
        lista_palabras.append(palabra)
    return lista_palabras


#En esta función se recorren los elementos de la lista letra por letra para comprobar que la letra solicitada se encuentra dentro de la palabra:
def encontrar_palabras_con_letra(palabras, letra) :
    lista_palabras_letras= []
    for x in range (len(palabras)) :
        for k in range (len(palabras[x])):
            if letra == ((palabras[x])[k]):
                lista_palabras_letras.append(palabras[x])
    return lista_palabras_letras

def ordenar_palabras_longitud(palabras) :
    for k in range (len(palabras) -1) : #Uso de algoritmo de ordenamiento burbuja.
            for x in range(len(palabras) -1 -k) :
                if len(palabras[x]) > len(palabras[x+1]) :
                    aux = palabras[x]
                    palabras[x] = palabras [x+1]
                    palabras[x+1] = aux
    return palabras


#Bloque principal
print('Inicio del programa')
palabras = ingresar_palabras()
letra = input("Ingrese la letra que quiere buscar: ")
palabras_con_letra = encontrar_palabras_con_letra(palabras, letra)
palabras_ordenadas_por_longitud = ordenar_palabras_longitud(palabras)

nueva_lista=[]
for x in (palabras_con_letra):
    ya_existe = False #Utilicé flags y una lista auxiliar para poder hacer el filtrado de palabras repetidas.
    for j in (nueva_lista):
        if x ==j:
            ya_existe= True
            break
    if ya_existe == False:
        nueva_lista.append(x)

print('*****************************************************')
print ('Las palabras que contienen la letra', letra ,'son: ')
for x in (nueva_lista):
    print(x)
print('*****************************************************')
print ('Lista de palabras ordenada por longitud, de menor a mayor: ')
for x in (palabras_ordenadas_por_longitud):
    print(x)
print('*****************************************************')
print('Fin del programa')