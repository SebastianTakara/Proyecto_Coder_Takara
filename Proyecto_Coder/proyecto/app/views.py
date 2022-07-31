from ast import Return
from urllib import request
from django.shortcuts import render
from app.models import Historias
from app.forms import UserRegisterForm
#crud
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def about_me(request):
    return render (request, "app/about_me.html")

def historias(request):
    historias = Historias.objects.all()
    return render (request, "app/historias.html", {"historias": historias })

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


def login_request(request):
      
      if request.method == "POST":

            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "app/home.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "app/home.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "app/home.html", {"mensaje":"Formulario erroneo"})
      

      form = AuthenticationForm()
    
      return render(request, "app/login.html", {'form': form})


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, "app/home.html", {"mensaje": "usuario creado"})

    else:
        form = UserRegisterForm()

    return render(request, "app/registro.html", {"form": form})        

