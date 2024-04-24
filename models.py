from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=[('M', 'Macho'), ('F', 'Hembra')])
    especie = models.CharField(max_length=50)
    propietario = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
