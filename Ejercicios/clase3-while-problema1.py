mayores=0
menores=0
x=0
while x<=10:
    nota=int(input("Ingrese nota: "))
    if nota>=7:
        mayores=mayores+1
    else:
        menores=menores+1
    x=x+1
print("La cantidad de estudiantes con nota mayor o igual a 7 es: " , mayores)
print("La cantidad de estudiantes con nota menor a 7 es: " , menores)
