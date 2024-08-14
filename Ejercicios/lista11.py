#LISTAS PARALELAS: DOS LISTAS QUE SE CARGAN A LA VEZ.

nombres = []
edades = []
for x in range (5) :
    nombre = input('Ingrese su nombre: ')
    nombres.append(nombre)
    edad = int(input('Ingrese su edad: '))
    edades.append(edad)
print('Nombres de las personas y su edad: ', nombres, edades)
print('Nombre de las personas mayores de edad: ')
for x in range (5):
    if edades[x] >= 18:
        print(nombres[x])
