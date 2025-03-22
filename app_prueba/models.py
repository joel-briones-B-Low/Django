from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    apellido = models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return self.nombre
    
    @classmethod
    def crear(cls,nombre, apellido):
        persona = cls(nombre=nombre, apellido=apellido)
        return persona
class Usuario(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=50, null=False)
    contrasenia = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.nombre_usuario
    
# persona.usuario_set.create(nombre_usuario='joel123', contrasenia='joel123') 
# usuario = persona.usuario_set.create(nombre_usuario='joel321', contrasenia='joel321') 

"""
    el id_persona es la relacion con django, ejemplo
    si to quiero ver la relacion con los objetos personas
    Usuario.objects.filter(id_persona__nombre__contains='Joel') 
    <QuerySet [<Usuario: joel123>, <Usuario: joel321>]>
    esto lo que hace es la relacion que hace django con los campos
    usuario en persona
    en cambio si se quiere poner el valor tal cual del id que vincula es
    Usuario.objects.filter(id_persona_id=1)
"""