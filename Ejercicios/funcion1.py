#LISTAS

#Esta función toma dos número a y b y los debe agregar a la lista
def funcion (a,b,lista) : 
    lista.append(a)
    lista.append(b)

#Programa principal: 
lista=[]
funcion(12, 34, lista)
print(lista)