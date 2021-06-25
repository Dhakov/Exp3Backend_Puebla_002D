from django.urls import path
from . import views
from .views import form_software, index, software, formulario, videojuego

urlpatterns = [
    path('', views.index, name="index"),

    path('juegos/', views.videojuego, name="videojuego"),
    path('software/', views.software, name="software"),
    path('core/', views.form_software, name="formulario"),
    path('modificar/', views.verTodo, name="verTodo"),
    path('modificar/<id>', views.mod_software, name="mod_software"),
    path('modificar/eliminar/<id>', views.del_software, name="del_software"),
]