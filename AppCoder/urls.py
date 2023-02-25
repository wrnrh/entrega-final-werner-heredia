from django.urls import path

from AppCoder.views import *
from django.contrib.auth.views import LogoutView

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   
    path('', inicio, name="Inicio"), #esta era nuestra primer view
    path('suscripcion', Suscripcion, name="suscripcion"),
    path('betatester', Betatester, name="betatester"),
    path('inscripcion', Inscripcion, name="inscripcion"),
    #path('items', leer_items, name="items"),
    path('itemsformulario', Itemsformulario, name="itemsformulario"),
    path('login', login_request, name="Login"),
    path('register', register, name="Register"),
    path('logout', LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path('sobremi', Sobremi, name="sobremi"),
    
    #path('itemsdelete/<items_nom>', itemsdelete, name='borrar'),
    #path('itemseditar/<items_nom>', itemseditar, name='editar'),

# Items
    path("items/list", itemslista.as_view(), name="listaitems"),
    path("items/<int:pk>", itemsdetalle.as_view(), name="detalleitems"),
    path("items/crear/", itemscreacion.as_view(), name="crearitem"),
    path("items/cambiar/<int:pk>", itemscambiar.as_view(), name="cambiaritem"),
    path("items/borrar/<int:pk>", itemsborrar.as_view(), name="borraritem"),

# Reseñas
    path("resenas/list", resenaslista.as_view(), name="listaresenas"),
    path("resenas/crear/", resenascreacion.as_view(), name="crearresenas"),
    path("resenas/cambiar/<int:pk>", resenascambiar.as_view(), name="cambiarresenas"),
    path("resenas/borrar/<int:pk>", resenasborrar.as_view(), name="borrarresenas"),


]

