class Hotel:
    def __init__(self):
        # Diccionario con opciones de habitaciones y precios por noche
        self.habitaciones = {
            'suite con vista al mar': 200.0,
            'habitación estándar': 100.0,
            'suite familiar': 150.0
        }
        # Servicios extra y sus precios
        self.serviciosextra = {
            'Uso de la Piscina': 20.0,
            'Cancha de Golf': 50.0
        }
        # Lista para almacenar las reservas realizadas
        self.reservas = []

    # Método para mostrar las opciones de habitaciones y precios
    def mostrarhabitaciones(self):
        print("Opciones de Habitaciones:")
        for habitacion, precio in self.habitaciones.items():
            print(f"{habitacion}: ${precio:.2f} por noche")

    # Método para mostrar los servicios extra y sus precios
    def mostrarserviciosextra(self):
        print("Servicios Extra Disponibles:")
        for servicio, precio in self.serviciosextra.items():
            print(f"{servicio}: ${precio:.2f}")

    # Método para realizar una reserva
    def realizarreserva(self):
        print("\nRealizar Reserva:")
        self.mostrarhabitaciones()
        
        # Solicita al cliente que seleccione una habitación
        eleccionhabitacion = input("Seleccione una habitación: ")
        if eleccionhabitacion not in self.habitaciones:
            print("Habitación no válida. Intente de nuevo.")
            return
        
        # Solicita los datos personales y el número de noches
        nombrecliente = input("Ingrese su nombre completo: ")
        noches = int(input("Ingrese el número de noches: "))
        
        # Solicita los servicios extra
        self.mostrarserviciosextra()
        serviciosseleccionados = []
        while True:
            servicio = input("Seleccione un servicio extra (o 'fin' para terminar): ")
            if servicio.lower() == 'fin':
                break
            if servicio in self.servicios_extra:
                serviciosseleccionados.append(servicio)
            else:
                print("Servicio no válido. Intente de nuevo.")
        
        # Calcula el costo total
        preciohabitacion = self.habitaciones[eleccionhabitacion]
        costohabitacion = preciohabitacion * noches
        costoservicios = sum(self.servicios_extra[servicio] for servicio in serviciosseleccionados)
        totalfactura = costohabitacion + costoservicios
        
        # Almacena la reserva
        reserva = {
            'nombre': nombrecliente,
            'habitacion': eleccionhabitacion,
            'noches': noches,
            'servicios': serviciosseleccionados,
            'costo_habitacion': costohabitacion,
            'costo_servicios': costoservicios,
            'total': totalfactura
        }
        self.reservas.append(reserva)
        
        # Muestra la factura detallada
        print("\nFactura Detallada:")
        print(f"Nombre del Cliente: {nombrecliente}")
        print(f"Habitación: {eleccionhabitacion}")
        print(f"Noches: {noches}")
        print(f"Costo de Habitación: ${costohabitacion:.2f}")
        print("Servicios Extras:")
        for servicio in serviciosseleccionados:
            print(f"  {servicio}: ${self.serviciosextra[servicio]:.2f}")
        print(f"Costo de Servicios Extras: ${costoservicios:.2f}")
        print(f"Total a Pagar: ${totalfactura:.2f}")

    # Método para mostrar todas las reservas
    def mostrarreservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return
        for idx, reserva in enumerate(self.reservas):
            print(f"\nReserva {idx + 1}:")
            print(f"Nombre del Cliente: {reserva['nombre']}")
            print(f"Habitación: {reserva['habitacion']}")
            print(f"Noches: {reserva['noches']}")
            print(f"Costo de Habitación: ${reserva['costohabitacion']:.2f}")
            print("Servicios Extras:")
            for servicio in reserva['servicios']:
                print(f"  {servicio}: ${self.servicios_extra[servicio]:.2f}")
            print(f"Costo de Servicios Extras: ${reserva['costoservicios']:.2f}")
            print(f"Total a Pagar: ${reserva['total']:.2f}")

def main():
    hotel = Hotel()
    
    while True:
        print("-----------------------------------------")
        print("\nMenú:")
        print("1. Realizar Reserva")
        print("2. Mostrar Reservas")
        print("3. Salir")
        print("-----------------------------------------")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            hotel.realizarreserva()
        elif opcion == 2:
            hotel.mostrarreservas()
        elif opcion == 3:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
