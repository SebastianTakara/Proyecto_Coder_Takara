from django.urls import path

from app import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about_me', views.about_me, name='about_me'),
    #crud
    path('historia/list', views.Historias_lista.as_view(), name='List'), 
    path(r'^(?P<pk>\d+)$', views.Historias_detalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.Historias_crear.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.Historias_editar.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.Historias_borrar.as_view(), name='Delete'),



]