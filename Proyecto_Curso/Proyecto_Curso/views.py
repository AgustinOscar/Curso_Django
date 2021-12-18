#Librerías necesarias.
from django.http import HttpResponse

#Creando la primera vista.
def saludo(request):
    return HttpResponse("Hola, esta es mi primera página con Django.")

#Creando una segunda vista.
def datosAlumno(request):
    datos = (
    """ 
    Alumno: Reyes González Agustín Óscar
    Cuenta: 417095215
    Carrera: Ing. Computación
    """
    )
    return HttpResponse(datos)