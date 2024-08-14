# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético.

names = []
for x in range (5) :
    name = input('Ingrese nombre: ')
    names.append(name)
name_menor = names[0]
for x in range (1,5) :
    if names[x] < name_menor:
        name_menor = name[x]
print('La lista de nombres es: ', names)
print('El nombre menor en orden alfabético es: ', name_menor)

