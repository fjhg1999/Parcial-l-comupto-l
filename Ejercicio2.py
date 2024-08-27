from datetime import datetime

# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del estudiante
        self.registro_asistencia = []  # Lista para almacenar registros de asistencia

    # Método para registrar la asistencia del estudiante
    def registro_asi(self, estado, motivo=""):
        fecha_actual = datetime.now().strftime("%Y-%m-%d")  # Obtener la fecha actual en formato año-mes-día
        # Agregar un registro de asistencia con la fecha, estado y motivo (si existe)
        self.registro_asistencia.append({'fecha': fecha_actual, 'estado': estado, 'motivo': motivo})

# Clase que representa a un docente
class Docente:
    def __init__(self, nombre, lista_estudiantes):
        self.nombre = nombre  # Nombre del docente
        # Diccionario de estudiantes, donde la clave es el nombre del estudiante y el valor es el objeto Estudiante
        self.lista_estudiantes = {estudiante.nombre: estudiante for estudiante in lista_estudiantes}

    # Método para tomar la asistencia de los estudiantes
    def tomar_asistencia(self):
        for nombre, estudiante in self.lista_estudiantes.items():  # Iterar sobre cada estudiante
            print(f"Registrando asistencia para {nombre}:")
            # Solicitar al usuario que ingrese el estado de asistencia
            estado = input("Ingrese 'P' para presente, 'A' para inasistencia, 'R' para permiso: ").upper()
            motivo = ""  # Inicializar el motivo como cadena vacía
            if estado == 'P':
                estado = "Presente"
            elif estado == 'A':
                estado = "Inasistencia"
            elif estado == 'R':
                estado = "Permiso"
                # Solicitar el motivo del permiso
                motivo = input("Ingrese el motivo del permiso: ")
            else:
                print("Ingrese una opcion valida si no se tomara como 'Inasistencia'.")
                estado = "Inasistencia"  # Asumir inasistencia si el estado es inválido
            # Registrar la asistencia del estudiante
            estudiante.registro_asi(estado, motivo)
            print(f"Asistencia registrada para {nombre}: {estado}. Motivo: {motivo if motivo else 'Ninguno'}.\n")

    # Método para generar un reporte de asistencia
    def generar_reporte(self):
        print(f"\nReporte de Asistencia para el docente {self.nombre}:")
        for estudiante in self.lista_estudiantes.values():  # Iterar sobre cada estudiante
            print(f"Estudiante: {estudiante.nombre}")
            for registro in estudiante.registro_asistencia:  # Iterar sobre los registros de asistencia de cada estudiante
                # Imprimir cada registro con fecha, estado y motivo
                print(f"Fecha: {registro['fecha']}, Estado: {registro['estado']}, Motivo: {registro['motivo']}")
        print("\nFin del reporte.\n")

# Ejemplo de uso
estudiante1 = Estudiante("Juan Pérez")  # Crear un objeto Estudiante
estudiante2 = Estudiante("Yajaira Claros")
estudiante3 = Estudiante("Jose Alvaro")
docente = Docente("Profesor García", [estudiante1, estudiante2, estudiante3])  # Crear un objeto Docente con una lista de estudiantes

# Tomar asistencia para los estudiantes
docente.tomar_asistencia()

# Generar un reporte de asistencia
docente.generar_reporte()
