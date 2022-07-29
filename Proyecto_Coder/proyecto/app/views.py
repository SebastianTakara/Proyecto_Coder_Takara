from urllib import request
from django.shortcuts import render
from app.models import Historias
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def about_me(request):
    return render (request, "app/about_me.html")

class Historias_lista(ListView):
    
    model= Historias
    template_name= "app/historia_lista.html"

class Historias_detalle(DetailView):

    model= Historias
    template_name= "app/historia_detalle.html"

class Historias_crear(CreateView):

    model= Historias
    success_url = '/app/historia/list'
    fields= ['titulo','subtitulo', 'cuerpo', 'autor', 'fecha' ]

class Historias_editar(UpdateView):

    model= Historias
    success_url = '/app/historia/list'
    fields = ['titulo','subtitulo', 'cuerpo', 'autor', 'fecha']

class Historias_borrar(DeleteView):
    
    model = Historias
    success_url = "/app/historia/list"