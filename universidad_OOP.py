
class Persona:
    def __init__(self, nombre, apellido, email, asistencia):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.asistencia = asistencia

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

class Profesor(Persona):
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

class Alumno(Persona):
    def __init__(self, numero_alumno, nombre, apellido, email, asistencia):
        self.numero_alumno = numero_alumno
        super().__init__(nombre,apellido,email,asistencia)

class Materia:
    def __init__(self, codigo, nombre):
        None

profesor_pepe:Profesor = Profesor("Pepe", "jose@um.edu.ar")
print(id(profesor_pepe))
print("el nombre es: ")
print(profesor_pepe.nombre)
print("el email es: ")
print(profesor_pepe.email)
print("su asistencia es: ")
print(profesor_pepe.asistencia)

print("EL PROFESOR FUE A CLASE...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("su asistencia es: ")
print(profesor_pepe.asistencia)

profesor_pepe.cambiar_nombre("JOSE!")

print(profesor_pepe.nombre)


profesor_walter = Profesor("Walter", "Walter@gmail.com")
profesor_daniel = Profesor("Daniel", "Daniel@um.com")



alumno_stefano = Alumno("0101", "Stefano", "Palazzo", "S.palazzo@um.edu.ar", 8)
print ("----------------------------")
print ("id: ",id(alumno_stefano))
print ("Nombre: ",alumno_stefano.nombre)
print ("Apellido: ",alumno_stefano.apellido)
print ("Email: ",alumno_stefano.email)
print ("Numero alumno: ",alumno_stefano.numero_alumno)
print ("Asistencias: ",alumno_stefano.asistencia)