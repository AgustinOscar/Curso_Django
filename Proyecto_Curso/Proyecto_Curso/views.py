#Librerías necesarias.
from django.http import HttpResponse
import datetime

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

#Creando una tercer vista con formato html.
def fecha(request):

    fecha_actual = datetime.datetime.now()

    dato = """
    <html>
    <body>
    <h1>
    Fecha y hora actual: %s
    </html>
    </body>
    </h1>
    """ %fecha_actual

    return HttpResponse(dato)

#Creando vista que recibe parámetros a través de URL.
def calcularEdad(request, edad, anio):
    
    edad_actual = edad
    periodo = anio-2021
    edad_futura = edad_actual+periodo

    dato = """
    <html>
    <body>
    <h2>
    En el año %s tendrás %s.
    </html>
    </body>
    </h2>
    """ %(anio,edad_futura)

    return HttpResponse(dato)