from django.db import models

# Create your models here.

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fechaingreso = models.DateField()
   

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Asignaturas(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    horas = models.IntegerField()

    def __str__(self):
        return self.nombre

class Enrolamiento(models.Model):
    id = models.AutoField(primary_key=True)
    idestudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    idasignatura = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)

    def __str__(self):
        return self.estudiante + ' ' + self.asignatura