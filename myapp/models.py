from django.db import models

class Project(models.Model):
    nombre = models.CharField(max_length=200)

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)