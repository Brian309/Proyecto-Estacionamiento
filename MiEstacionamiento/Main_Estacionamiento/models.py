from django.db import models
from django.db.models.expressions import F
from django.urls import reverse
import uuid

# Create your models here.



class Vehiculo(models.Model):
    id_vehiculo = models.UUIDField(primary_key=True, default = uuid.uuid4, help_text='Id del vehiculo')
    patente = models.CharField(max_length=8,null=False, blank=False, help_text='Ingrese la patente de su automovil')
    marca = models.CharField(max_length=8,null=False, blank=False, help_text='Ingrese la marca de su automovil')
    color = models.CharField(max_length=8,null=False, blank=False, help_text='ingrese el color del vehiculo')
    año = models.CharField(max_length=8,null=False, blank=False, help_text='Ingrese el año de su vehiculo')

    def __str__(self):
        return f'{self.patente},{self.marca},{self.color}'
    
    def get_absolute_url(self):
        pass

class Usuario(models.Model):
    id_user = models.UUIDField(primary_key=True, default = uuid.uuid4, help_text='Id del usuario (Se crea solo)')
    rut_user = models.CharField(max_length=10, null=False, blank=False,help_text="Indique su rut")
    nom_user = models.CharField(max_length=30, help_text="Indique su Nombre")
    password = models.CharField(max_length=16, null=False, help_text="Indique su contraseña")
    email = models.EmailField(max_length=50, error_messages={"Error":"Digite un formato de correo valido"}, help_text="Indique su Email")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{str(self.rut_user)}, {self.nom_user}, {str(self.email)}, {self.vehiculo}'
    
    def get_absolute_url(self):
        pass



