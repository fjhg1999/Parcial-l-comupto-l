class Tienda:
    def __init__(self):
        self.ventas = []

    def registrar_venta(self):
        print("Registro de venta:")
        venta_actual = []
        while True:
            producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
            if producto.lower() == 'fin':
                break
            precio = float(input(f"Ingrese el precio de {producto}: "))
            cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
            total_producto = precio * cantidad
            venta_actual.append((producto, cantidad, precio, total_producto))
        
        total_venta = sum(item[3] for item in venta_actual)
        print(f"\nTotal de la venta: ${total_venta:.2f}")

        while True:
            pago_cliente = float(input("Ingrese el monto pagado por el cliente: "))
            if pago_cliente >= total_venta:
                vuelto = pago_cliente - total_venta
                print(f"Vuelto a devolver: ${vuelto:.2f}")
                break
            else:
                print("Monto insuficiente. Por favor, ingrese un monto mayor o igual al total de la venta.")

        self.ventas.append(venta_actual)
        print("Venta registrada con éxito.\n")

    def mostrar_ventas(self):
        if not self.ventas:
            print("No hay ventas registradas.")
            return
        for idx, venta in enumerate(self.ventas):
            print(f"\nVenta {idx + 1}:")
            for item in venta:
                print(f"Producto: {item[0]}, Cantidad: {item[1]}, Precio Unitario: ${item[2]:.2f}, Total: ${item[3]:.2f}")
            total_venta = sum(item[3] for item in venta)
            print(f"Total de la venta: ${total_venta:.2f}")

class Proveedor:
    def __init__(self):
        self.inventario = {}

    def registrar_producto(self):
        print("Registro de producto:")
        producto = input("Ingrese el nombre del producto: ")
        precio_sugerido = float(input(f"Ingrese el precio sugerido de venta para {producto}: "))
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        
        if producto in self.inventario:
            self.inventario[producto]['cantidad'] += cantidad
            self.inventario[producto]['precio_sugerido'] = precio_sugerido
        else:
            self.inventario[producto] = {'cantidad': cantidad, 'precio_sugerido': precio_sugerido}
        
        print(f"Producto {producto} registrado con éxito.\n")

    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
            return
        print("\nInventario de productos:")
        for producto, detalles in self.inventario.items():
            print(f"Producto: {producto}, Cantidad: {detalles['cantidad']}, Precio Sugerido: ${detalles['precio_sugerido']:.2f}")

def main():
    tienda = Tienda()
    proveedor = Proveedor()
    
    while True:
        print("Menú:")
        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Registrar producto de proveedor")
        print("4. Mostrar inventario")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            tienda.registrar_venta()
        elif opcion == 2:
            tienda.mostrar_ventas()
        elif opcion == 3:
            proveedor.registrar_producto()
        elif opcion == 4:
            proveedor.mostrar_inventario()
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()