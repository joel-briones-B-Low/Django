from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    apellido = models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=50, null=False)
    contrasenia = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.nombre_usuario