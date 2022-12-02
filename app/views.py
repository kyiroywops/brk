from django.shortcuts import render
from .models import Estudiante, Asignaturas, Enrolamiento


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def asignaturas(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'asignaturas.html', {'asignaturas': asignaturas})

def enrolamiento(request):
    enrolamiento = Enrolamiento.objects.all()
    return render(request, 'enrolamiento.html', {'enrolamiento': enrolamiento})
