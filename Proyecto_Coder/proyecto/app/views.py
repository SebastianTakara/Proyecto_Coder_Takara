
from django.shortcuts import render
from psutil import users
from app.models import Historias, Avatar
from app.forms import UserRegisterForm, UserEditForm
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
@login_required
def home(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "app/home.html",{"url": avatares[0].imagen.url })

def about_me(request):
    return render (request, "app/about_me.html")

@login_required
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


@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "app/home.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "app/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


