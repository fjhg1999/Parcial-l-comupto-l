class Empleado:
    def __init__(self, nombre, anios_trabajados):
        self.nombre = nombre  # Nombre del empleado
        self.anios_trabajados = anios_trabajados  # Años trabajados por el empleado

    def calcular_bono(self):
        # Bono adicional para empleados con más de 5 años trabajados
        if self.anios_trabajados > 5:
            return 500  # Monto fijo del bono, por ejemplo $500
        return 0  # Sin bono si los años trabajados son 5 o menos

    def calcular_salario(self):
        # Método abstracto, debe ser implementado por las subclases
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, anios_trabajados, salario_base, comisiones):
        super().__init__(nombre, anios_trabajados)  # Inicializar nombre y años trabajados
        self.salario_base = salario_base  # Salario base para empleados de plaza fija
        self.comisiones = comisiones  # Comisiones adicionales

    def calcular_salario(self):
        # Calcular el salario total sumando el salario base, comisiones y bono (si aplica)
        salario_total = self.salario_base + self.comisiones + self.calcular_bono()
        return salario_total  # Retornar el salario total calculado

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anios_trabajados, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, anios_trabajados)  # Inicializar nombre y años trabajados
        self.horas_trabajadas = horas_trabajadas  # Horas trabajadas por el empleado
        self.tarifa_por_hora = tarifa_por_hora  # Tarifa de pago por hora

    def calcular_salario(self):
        # Calcular el salario total multiplicando horas trabajadas por tarifa y sumando bono (si aplica)
        salario_total = (self.horas_trabajadas * self.tarifa_por_hora) + self.calcular_bono()
        return salario_total  # Retornar el salario total calculado

# Función para ingresar datos de empleados
def ingresar_datos_empleados():
    empleados = []  # Lista para almacenar los empleados

    while True:
        # Solicitar al usuario el tipo de empleado
        tipo = input("Ingrese el tipo de empleado ('fijo' para plaza fija, 'horas' para por horas, 'salir' para terminar): ").lower()

        if tipo == 'salir':
            break  # Salir del bucle si el usuario elige terminar

        nombre = input("Ingrese el nombre del empleado: ")  # Solicitar el nombre del empleado
        anios_trabajados = int(input("Ingrese los años trabajados: "))  # Solicitar los años trabajados

        if tipo == 'fijo':
            # Solicitar datos específicos para empleados de plaza fija
            salario_base = float(input("Ingrese el salario base: "))
            comisiones = float(input("Ingrese las comisiones: "))
            empleado = EmpleadoPlazaFija(nombre, anios_trabajados, salario_base, comisiones)
        
        elif tipo == 'horas':
            # Solicitar datos específicos para empleados por horas
            horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
            tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
            empleado = EmpleadoPorHoras(nombre, anios_trabajados, horas_trabajadas, tarifa_por_hora)
        
        else:
            print("Tipo de empleado no reconocido, intente nuevamente.")
            continue  # Continuar con la próxima iteración si el tipo es inválido
        
        empleados.append(empleado)  # Agregar el empleado a la lista
    
    return empleados  # Retornar la lista de empleados

# Función para calcular y mostrar los salarios
def mostrar_salarios(empleados):
    for empleado in empleados:
        # Mostrar el salario calculado para cada empleado
        print(f"Salario de {empleado.nombre}: ${empleado.calcular_salario()}")

# Ejemplo de uso
def main():
    empleados = ingresar_datos_empleados()  # Ingresar los datos de los empleados
    mostrar_salarios(empleados)  # Mostrar los salarios de los empleados

if __name__ == "__main__":
    main()  # Llamar a la función principal para ejecutar el programa
