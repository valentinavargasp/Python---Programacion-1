# Consigna: Este coloquio podrá ser grupal, hasta cuatro y va a consistir en crear un programa con lo visto hasta ahora. Será libre, y se evaluará las características que agreguen. Serán evaluados en base a la explicación de los algoritmos y su correcta aplicación.  Se deberá Utilizar al menos dos de estos temas vistos:  Funciones, Listas, Tuplas, Ordenamiento. 

"""Este programa permite al usuario ingresar una lista de productos junto con sus categorías.
# Luego, agrupa estos productos por categoría y muestra la lista ordenada de acuerdo a las categorías.

Funcionamiento:
1. El programa solicita al usuario la cantidad de productos que desea ingresar.
2. Para cada producto, el usuario debe ingresar el nombre del producto y su categoría.
3. Una vez que todos los productos han sido ingresados, el programa agrupa los productos por categoría usando un diccionario.
4. Finalmente, imprime la lista de productos ordenada por categorías, mostrando cada categoría y los productos que pertenecen a ella.

Ejemplo de su uso:
Si el usuario ingresa los productos "Manzana" en la categoría "Frutas" y "Pan" en la categoría "Panadería", el programa agrupará "Manzana" bajo "Frutas" y "Leche" bajo "Lácteos", y mostrará estas categorías con sus respectivos productos."""

def ingresar_datos():
    # Solicita al usuario la cantidad de productos que desea ingresar.
    n = int(input("Ingrese la cantidad de productos: "))
    productos = []  # Lista para almacenar los productos y sus categorías.
    
    # Ciclo utilizado para ingresar el nombre y la categoría de cada producto.
    for i in range(n):
        nombre = input("Ingrese el nombre del producto: ")  # Entrada del nombre del producto.
        categoria = input("Ingrese la categoría del producto: ")  # Entrada de la categoría del producto.
        productos.append((nombre, categoria))  # Agrega el producto y su categoría a la lista.
    
    return productos  #Devuelve la lista de productos.

def agrupar_por_categoria(productos):
    # Crea un diccionario para agrupar los productos por categoría.
    productos_por_categoria = {}
    
    # Itera sobre la lista de productos para organizarlos por categoría.
    for producto, categoria in productos:
        # Si la categoría no está en el diccionario, la agrega con una lista vacía.
        if categoria not in productos_por_categoria: # Acá uso el operador de pertenencia not in.
            productos_por_categoria[categoria] = []
        # Añade el producto a la lista correspondiente a su categoría.
        productos_por_categoria[categoria].append(producto)
    
    return productos_por_categoria  #Devuelve el diccionario con productos agrupados por categoría.

def mostrar_resultados(productos_por_categoria):
    # Imprime los productos agrupados por categoría.
    print("Lista de compras ordenada por categoría:")
    print("--------------------------------------------------------------------")
    # Itera sobre cada categoría en el diccionario.
    for categoria, productos in productos_por_categoria.items():
        print("Categoría: " + categoria)  # Imprime el nombre de la categoría.
        
        # Itera sobre los productos en la categoría y los imprime.
        for producto in productos:
            print("Producto: " + producto)
        print("--------------------------------------------------------------------")

# Bloque principal del programa
print("*******************************************************************")
print(" Programa: Organizá tu lista de compras. Ingresá los productos y su categoría")
print("*******************************************************************")

productos = ingresar_datos()  # Llama a la función para ingresar los datos de los productos.
productos_por_categoria = agrupar_por_categoria(productos)  # Agrupa los productos por categoría.
print("*******************************************************************")
mostrar_resultados(productos_por_categoria)  # Muestra los resultados agrupados por categoría.
print("*******************************************************************")
