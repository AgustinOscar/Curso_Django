#Librerías necesarias.
from django.http import HttpResponse
from django.template import Template, Context
import datetime

#Clase persona para la plantilla 1.
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

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

#Se crea una vista con plantillas.
def plantilla_1(request):

    nombre = 'Agustin Oscar Reyes González'
    edad = 28
    fecha_actual = datetime.datetime.now()

    persona_1 = Persona('Oscar', 'Reyes')

    diccionario_contexto = {'persona': persona_1, 'fecha':fecha_actual}

    doc_externo = open('C:/Users/reyes/Desktop/Curso Django/Proyecto_Curso/Proyecto_Curso/Templates/plantilla_1.html')

    #Se crea objeto Template.
    template_1 = Template(doc_externo.read())

    doc_externo.close()

    #Se crea contexto vacío.
    contexto = Context(diccionario_contexto)

    documento = template_1.render(contexto)

    return HttpResponse(documento)
