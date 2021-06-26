import geocoder

from django.db import models
from django.contrib.auth.models import (AbstractUser, User)


mapbox_token = 'pk.eyJ1Ijoid2F6b3dza2lkZXZlbG9wIiwiYSI6ImNrcTdneXZ4ejA2M2Uyd3VoY29hZTVjYXYifQ.wUjItHT_F5ZCMXUcwx5_xA'

class Place(models.Model):
    address = models.CharField(max_length=100)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Place, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.address

class Vehiculo(models.Model):
    patente = models.CharField(max_length=8,null=False, blank=False, help_text='Ingrese la patente de su automovil')
    marca = models.CharField(max_length=8,null=False, blank=False, help_text='Ingrese la marca de su automovil')
    color = models.CharField(max_length=8,null=False, blank=False, help_text='ingrese el color del vehiculo')
    año = models.CharField(max_length=8,null=False, blank=False, help_text='Ingrese el año de su vehiculo')


    class Meta:
        ordering = ['patente']


    def __str__(self):
        return f'{self.patente}'
    
    def get_absolute_url(self):
        pass

class Usuario(AbstractUser):
    rut_user = models.CharField(max_length=10, null=False, blank=False,help_text="Indique su rut")
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    vehiculo = models.ManyToManyField(Vehiculo, blank=True)
    address = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f'{self.name},{self.rut_user}'
