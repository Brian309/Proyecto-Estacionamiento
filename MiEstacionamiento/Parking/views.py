from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import Place,Vehiculo,Usuario
from django.urls import reverse_lazy


#Nombre y clave para mapbox
token='mapbox_token'
key='pk.eyJ1Ijoid2F6b3dza2lkZXZlbG9wIiwiYSI6ImNrcTdneXZ4ejA2M2Uyd3VoY29hZTVjYXYifQ.wUjItHT_F5ZCMXUcwx5_xA'
parkings='lugares'

class PlaceView(CreateView):
    #Atributos del CRUD 
    model = Place
    fields = ['address']
    template_name = 'places/home.html'
    success_url = '/'
    #Objetos del modelo
    placeObjects=Place.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[token] = key
        context[parkings] = Place.objects.all()
        return context

def inicio(request):
    return render(request, 'inicio.html', context={token:key, parkings:PlaceView.placeObjects},)

