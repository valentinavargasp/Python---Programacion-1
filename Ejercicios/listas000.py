#NO ES VÁLIDO PARA EL PARCIAL
sueldos = []
for x in range (5) :
    valor = int(input('Ingresa sueldo: '))
    sueldos.append(valor)
print('Lista sin ordenar: ', sueldos) 
sueldos.sort()
print('Lista ordenada: ', sueldos)
sueldos.reverse()
print('Lista ordenada descendente: ', sueldos)