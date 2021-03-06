"""Proyecto_Curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto_Curso.views import saludo, datosAlumno, fecha, calcularEdad, plantilla_1, cursoDjango, cursoDjango2



urlpatterns = [
    path('admin/', admin.site.urls),
    path('vista_Saludo/', saludo),
    path('vista_DatosAlumno/', datosAlumno),
    path('vista_FechaActual/', fecha),
    path('vista_EdadFutura/<int:edad>/<int:anio>', calcularEdad),
    path('vista_plantilla1', plantilla_1),
    path('vista_cursoDjango/', cursoDjango),
    path('vista_cursoDjango2/', cursoDjango2)
]
