cantidad=0
x=1
n=int(input("Cuantas piezas cargará: "))
while x<=n:
    largo=float(input("Ingrese la medida de la pieza: "))
    if largo>=1.2 and largo<= 1.3:
        cantidad=cantidad+1
x=x+1
print("La cantidad de piezas aptas son: " , cantidad)
