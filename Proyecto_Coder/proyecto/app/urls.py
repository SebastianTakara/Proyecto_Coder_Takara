from django.urls import path

from app import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', views.home, name='home'),
    path('about_me', views.about_me, name='about_me'),
    path('historias', views.historias, name = 'historias'),
    path('historia/list', views.Historias_lista.as_view(), name='List'), 
    path(r'^(?P<pk>\d+)$', views.Historias_detalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.Historias_crear.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.Historias_editar.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.Historias_borrar.as_view(), name='Delete'),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name= 'app/logout.html'), name='logout'),
    path('editarperfil', views.editarPerfil, name="editarperfil")

]