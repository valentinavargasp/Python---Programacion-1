#Funciones
def funcion_param_lista (lista) :
    lista.append('d')

#Programa principal

lista = ['a' , 'b', 'c']
print(lista)
funcion_param_lista(lista) #le estoy diciendo donde está la lista para que la función vaya y la modifique
print(lista) #Devuelve: ['a', 'b', 'c'] ['Nuevo elemento', 'b', 'c']