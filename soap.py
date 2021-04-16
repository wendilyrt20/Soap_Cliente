import zeep
import json

wsdl_Uri = 'http://localhost:7000/ws/EstudianteWebServices?wsdl'
cliente = zeep.Client(wsdl=wsdl_Uri)



def ListarEstudiantes():
 return cliente.service.getListaEstudiante()

def ConsultEstudiante(matricula):
    return cliente.service.getEstudiante(matricula)

def CrearEstudiante(matricula, carrera, nombre):
    EstudianteOBJ = cliente.get_type("ns0:estudiante")
    Estudiante = EstudianteOBJ(matricula= matricula , nombre= nombre , carrera= carrera)
   # print(Estudiante)
    return cliente.service.crearEstudiante(Estudiante)

def EliminarEstudiante(matricula):
    return cliente.service.eliminarEstudiante(matricula)
print("----------------------------------------------------")
print("LISTAR ESTUDIANTES:")
print("----------------------------------------------------")

print(ListarEstudiantes())


print("----------------------------------------------------")
print("CONSULTAR ESTUDIANTE:")
print("----------------------------------------------------")
matricula = 20011136
#print(ConsultEstudiante(matricula))

print("----------------------------------------------------")
print("CREAR ESTUDIANTE:")
print("----------------------------------------------------")
matricula = 20161565
carrera = "ITT"
nombre = "Anthony Sakamoto O."
#print(CrearEstudiante(matricula, carrera,nombre))

print("----------------------------------------------------")
print("ELIMINAR ESTUDIANTE:")
print("----------------------------------------------------")
#print(EliminarEstudiante(0))
print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
