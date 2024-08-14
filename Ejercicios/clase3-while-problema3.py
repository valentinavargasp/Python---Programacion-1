n=int(input("Cuántos empleados tiene la empresa?: "))
x=1
contador1=0
contador2=0
gastos=0
while x<=n:
    sueldo=float(input("Ingrese el sueldo del empleado: "))
    if sueldo<=300:
        contador1=contador1+1
    else:
        contador2=contador2+1
    gastos=gastos+sueldo
    x=x+1
print("Cantidad de empleados con sueldos entre 100 y 300: ", contador1)
print("Cantidad de empleados con sueldos mayores a 300: ", contador2)
print("Los gastos totales en sueldos es de: ", gastos)
