# Clase que maneja la gestión de ventas en la tienda
class Tienda:
    def __init__(self):
        # Lista para almacenar las ventas realizadas
        self.ventas = []

    # Metodo para registrar una nueva venta
    def registrarventa(self):
        print("Registro de venta:")
        ventaactual = []
        while True:
            # Solicita el nombre del producto al usuario
            producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
            if producto.lower() == 'fin':
                break
            # Solicita el precio del producto
            precio = float(input(f"Ingrese el precio de {producto}: "))
            # Solicita la cantidad del producto
            cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
            # Calcula el total para este producto
            totalproducto = precio * cantidad
            # Añade los detalles del producto a la venta actual
            ventaactual.append((producto, cantidad, precio, totalproducto))
        
        # Calcula el total de la venta
        totalventa = sum(item[3] for item in ventaactual)
        print(f"\nTotal de la venta: ${totalventa:.2f}")

        while True:
            # Solicita el monto pagado por el cliente
            pagocliente = float(input("Ingrese el monto pagado por el cliente: "))
            if pagocliente >= totalventa:
                # Calcula el vuelto
                vuelto = pagocliente - totalventa
                print(f"Vuelto a devolver: ${vuelto:.2f}")
                break
            else:
                print("Monto insuficiente. Por favor, ingrese un monto mayor o igual al total de la venta.")

        # Añade la venta a la lista de ventas
        self.ventas.append(ventaactual)
        print("Venta registrada con éxito.\n")

    # Metodo para mostrar todas las ventas registradas
    def mostrarventas(self):
        if not self.ventas:
            print("No hay ventas registradas.")
            return
        for idx, venta in enumerate(self.ventas):
            print(f"\nVenta {idx + 1}:")
            for item in venta:
                print(f"Producto: {item[0]}, Cantidad: {item[1]}, Precio Unitario: ${item[2]:.2f}, Total: ${item[3]:.2f}")
                print("-----------------------------------------")
            # Calcula el total de la venta
            total_venta = sum(item[3] for item in venta)
            print(f"Total de la venta: ${total_venta:.2f}")

# Clase que maneja la gestión de productos de proveedores
class Proveedor:
    def __init__(self):
        # Diccionario para almacenar el inventario de productos
        self.inventario = {}

    # Metodo para registrar un nuevo producto de proveedor
    def registrarproducto(self):
        print("Registro de producto:")
        # Solicita el nombre del producto
        producto = input("Ingrese el nombre del producto: ")
        # Solicita el precio sugerido de venta
        precio_sugerido = float(input(f"Ingrese el precio sugerido de venta para {producto}: "))
        # Solicita la cantidad del producto
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        
        # Si el producto ya existe en el inventario, actualiza la cantidad y el precio sugerido
        if producto in self.inventario:
            self.inventario[producto]['cantidad'] += cantidad
            self.inventario[producto]['precio_sugerido'] = precio_sugerido
        else:
            # Si el producto es nuevo, añade una nueva entrada en el inventario
            self.inventario[producto] = {'cantidad': cantidad, 'precio_sugerido': precio_sugerido}
        
        print(f"Producto {producto} registrado con éxito.\n")

    # Metodo para mostrar el inventario de productos
    def mostrarinventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
            return
        print("\nInventario de productos:")
        for producto, detalles in self.inventario.items():
            print(f"Producto: {producto}, Cantidad: {detalles['cantidad']}, Precio Sugerido: ${detalles['preciosugerido']:.2f}")

# Funcion principal que ejecuta el programa
def main():
    # Crea instancias de las clases Tienda y Proveedor
    tienda = Tienda()
    proveedor = Proveedor()
    
    while True:
        # Muestra el menú de opciones
        print("-----------------------------------------")
        print("Menú:")
        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Registrar producto de proveedor")
        print("4. Mostrar inventario")
        print("5. Salir")
        print("-----------------------------------------")
        
        # Solicita al usuario que seleccione una opción
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            # Llama al método para registrar una venta
            tienda.registrarventa()
        elif opcion == 2:
            # Llama al método para mostrar las ventas
            tienda.mostrarventas()
        elif opcion == 3:
            # Llama al método para registrar un producto de proveedor
            proveedor.registrarproducto()
        elif opcion == 4:
            # Llama al método para mostrar el inventario
            proveedor.mostrarinventario()
        elif opcion == 5:
            # Sale del programa
            print("Saliendo del programa.")
            break
        else:
            # Muestra un mensaje de error si la opción es inválida
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecuta la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
