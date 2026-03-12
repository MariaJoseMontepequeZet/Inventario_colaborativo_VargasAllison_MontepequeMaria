inventario = {}

def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
<<<<<<< HEAD

    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print("Producto agregado correctamente.\n")


=======
    
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print("Producto agregado correctamente.\n")

>>>>>>> inventario
def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
<<<<<<< HEAD
        print("\n===== INVENTARIO DE LA TIENDA =====")
=======
        print("\nInventario de la tienda:")
>>>>>>> inventario
        for producto, datos in inventario.items():
            print(f"Producto: {producto}")
            print(f"Cantidad: {datos['cantidad']}")
            print(f"Precio: Q{datos['precio']}")
<<<<<<< HEAD
            print("--------------------------")


def actualizar_producto():
    nombre = input("Ingrese el producto a actualizar: ")

=======
            print("----------------------")

def actualizar_producto():
    nombre = input("Ingrese el producto a actualizar: ")
    
>>>>>>> inventario
    if nombre in inventario:
        cantidad = int(input("Nueva cantidad: "))
        precio = float(input("Nuevo precio: "))
        inventario[nombre]["cantidad"] = cantidad
        inventario[nombre]["precio"] = precio
        print("Producto actualizado.\n")
    else:
        print("El producto no existe.\n")

<<<<<<< HEAD

def eliminar_producto():
    nombre = input("Producto a eliminar: ")

=======
def eliminar_producto():
    nombre = input("Producto a eliminar: ")
    
>>>>>>> inventario
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado.\n")
    else:
        print("Producto no encontrado.\n")

<<<<<<< HEAD

def buscar_producto():
    nombre = input("Ingrese el producto a buscar: ")

    if nombre in inventario:
        datos = inventario[nombre]
        print("\nProducto encontrado:")
        print(f"Cantidad: {datos['cantidad']}")
        print(f"Precio: Q{datos['precio']}\n")
    else:
        print("El producto no existe en el inventario.\n")


def valor_total():
    total = 0

    for datos in inventario.values():
        total += datos["cantidad"] * datos["precio"]

    print(f"\nValor total del inventario: Q{total}\n")


=======
>>>>>>> inventario
while True:
    print("===== INVENTARIO DE TIENDA =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
<<<<<<< HEAD
    print("5. Buscar producto")
    print("6. Ver valor total del inventario")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

=======
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
>>>>>>> inventario
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
<<<<<<< HEAD
        buscar_producto()
    elif opcion == "6":
        valor_total()
    elif opcion == "7":
=======
>>>>>>> inventario
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.\n")