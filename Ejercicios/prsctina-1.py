print("Bienvenidos al calculo de sueldos")
print("__________________________________")
horas=input("Ingrese la cantidad de horas trabajadas por dia: ")
horas=int(horas)
dias=input("Ingrese la cantidad de dias trabajados: ")
dias=int(dias)
sueldo=dias*horas
precio=input("Ingrese el valor por hora: ")
precio=float(precio)
salario=sueldo*precio
print("La cantidad de horas trabajada en el mes es de: ")
print(sueldo)
print("El salario generado este mes es de: ")
print(salario)
