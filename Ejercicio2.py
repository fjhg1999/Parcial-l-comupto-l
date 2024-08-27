from datetime import datetime

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registro_asistencia = []

    def registro_asi(self, estado, motivo=""):
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        self.registro_asistencia.append({'fecha': fecha_actual, 'estado': estado, 'motivo': motivo})

class Docente:
    def __init__(self, nombre, lista_estudiantes):
        self.nombre = nombre
        self.lista_estudiantes = {estudiante.nombre: estudiante for estudiante in lista_estudiantes}

    def tomar_asistencia(self):
        for nombre, estudiante in self.lista_estudiantes.items():
            print(f"Registrando asistencia para {nombre}:")
            estado = input("Ingrese 'P' para presente, 'R' para inasistencia, 'R' para permiso: ").upper()
            motivo = ""
            if estado == 'P':
                estado = "Presente"
            elif estado == 'A':
                estado = "Inasistencia"
            elif estado == 'R':
                estado = "Permiso"
                motivo = input("Ingrese la razón del permiso: ")
            else:
                print("Estado no válido. Se registrará como 'Inasistencia'.")
                estado = "Inasistencia"
            estudiante.registro_asi(estado, motivo)
            print(f"Asistencia registrada para {nombre}: {estado}. Motivo: {motivo if motivo else 'Ninguno'}.\n")

    def generar_reporte(self):
        print(f"\nReporte de Asistencia para el docente {self.nombre}:")
        for estudiante in self.lista_estudiantes.values():
            print(f"Estudiante: {estudiante.nombre}")
            for registro in estudiante.registro_asistencia:
                print(f"Fecha: {registro['fecha']}, Estado: {registro['estado']}, Motivo: {registro['motivo']}")
        print("\nFin del reporte.\n")

# Ejemplo de uso
estudiante1 = Estudiante("Juan Pérez")
estudiante2 = Estudiante("Ana Gómez")
estudiante3 = Estudiante("Carlos Ramírez")
docente = Docente("Profesor García", [estudiante1, estudiante2, estudiante3])

# Tomar asistencia
docente.tomar_asistencia()

# Generar reporte de asistencia
docente.generar_reporte()
