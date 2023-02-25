from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import items, suscripcion, betatester, inscripcion, resenas
from AppCoder.forms import itemsformulario, suscformulario, betaformulario, inscformulario, UserRegisterForm, itemsformulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

from django.views.generic import TemplateView
# usar @login_required sobre el def


# Create your views here.

def inicio(request):
      return render(request, "AppCoder/inicio.html")

def Sobremi(request):
      return render(request, "AppCoder/sobremi.html")

def Suscripcion(request):
      return render(request, "AppCoder/suscripcion.html")

def Betatester(request):
      return render(request, "AppCoder/betatester.html")

def Inscripcion(request):
      return render(request, "AppCoder/inscripcion.html")

def Items(request):
      return render(request, "AppCoder/items.html")


@login_required
def Suscripcion(request):
      if request.method == 'POST':
            miFormulario = suscformulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  susc = suscripcion (nombre=informacion['nombre'],contrasena=informacion['contrasena'],
                        email=informacion['email'],) 
                  susc.save()
                  return render(request, "AppCoder/suscripcion.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= suscformulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/suscripcion.html", {"miFormulario":miFormulario})

def Betatester(request):
      if request.method == 'POST':
            miFormulario = betaformulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  beta = betatester (nombre=informacion['nombre'], email=informacion['email'],) 
                  beta.save()
                  return render(request, "AppCoder/betatester.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= betaformulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/betatester.html", {"miFormulario":miFormulario})

def Inscripcion(request):
      if request.method == 'POST':
            miFormulario = inscformulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  insc = inscripcion (nombre=informacion['nombre'], email=informacion['email'],) 
                  insc.save()
                  return render(request, "AppCoder/inscripcion.html") #Vuelvo al inicio o a donde quieran

      else: 
            miFormulario= inscformulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/inscripcion.html", {"miFormulario":miFormulario})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"form": form})

def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"AppCoder/registro.html" ,  {"form":form})  #"form es el nombre para mandar al html"

def leer_items(request):
    dato = items.objects.all()
    contexto = {'dato': dato } 
    return render(request, 'AppCoder/items.html', contexto)

@login_required
def Itemsformulario(request):
      if request.method == 'POST':
            form = itemsformulario(request.POST, request.FILES)
            if form.is_valid(): 
                  informacion = form.cleaned_data
                  dato = items(nombre = informacion['nombre'],
                  tipo = informacion['tipo'],
                  dano_f = informacion['dano_f'],
                  dano_m = informacion['dano_m'],
                  descripcion = informacion['descripcion' ], 
                  imagen = informacion['imagen' ]) 
                  dato.save()
                  return render(request, 'AppCoder/items.html')    
      else:
            form = itemsformulario() 
      return render(request, 'AppCoder/itemsformulario.html', {'form': form}) 


@login_required
def itemsdelete(request, items_nom):
      item = items.objects.get(nombre=items_nom)
      item.delete()
      item_ = items.objects.all()
      contexto = {"items":item_}
      return render(request, "AppCoder/items.html", contexto)

@login_required
def itemseditar(request, items_nom):

      # Recibe el nombre del profesor que vamos a modificar
      item = items.objects.get(nombre=items_nom)

      # Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            # aquí mellega toda la información del html
            form = itemsformulario(request.POST)

            print(form)

            if form.is_valid:  # Si pasó la validación de Django

                  informacion = form.cleaned_data

                  item.nombre = informacion['nombre']
                  item.tipo = informacion['tipo']
                  item.dano_f = informacion['dano_f']
                  item.dano_m = informacion['dano_m']
                  item.imagen = informacion['imagen']

                  item.save()

                  # Vuelvo al inicio o a donde quieran
                  return render(request, "AppCoder/items.html")
      # En caso que no sea post
      else:
            # Creo el formulario con los datos que voy a modificar
            form = itemsformulario(initial={'nombre': item.nombre, 'tipo': item.tipo,
                                                      'dano_f': item.dano_f, 'dano_m': item.dano_m,
                                                      'descripcion': item.descripcion,
                                                      'imagen': item.imagen,})

      # Voy al html que me permite editar
      return render(request, "AppCoder/itemseditar.html", {"form": form, "items_nom": items_nom})


## ITEMS
class itemslista(ListView):
      model = items

class itemsdetalle(DetailView):
      model = items

class itemscreacion(PermissionRequiredMixin, CreateView):
      permission_required = 'accounts.template_all'
      model = items
      success_url = reverse_lazy("listaitems")
      fields = ["nombre","tipo","dano_f","dano_m","descripcion","imagen"]

class itemscambiar(PermissionRequiredMixin, UpdateView):
      permission_required = 'accounts.template_all'
      model = items
      success_url = reverse_lazy("listaitems")
      fields = ["nombre","tipo","dano_f","dano_m","descripcion","imagen"]

class itemsborrar(PermissionRequiredMixin, DeleteView):
      permission_required = 'accounts.template_all'
      model = items
      success_url = reverse_lazy("listaitems")



## RESEÑAS
class resenaslista(ListView):
      model = resenas

class resenascreacion(LoginRequiredMixin, CreateView):
      model = resenas
      success_url = reverse_lazy("listaresenas")
      fields = ["puntaje","titulo","mensaje","imagen"]

class resenascambiar(PermissionRequiredMixin, UpdateView):
      permission_required = 'accounts.template_all'
      model = resenas
      success_url = reverse_lazy("listaresenas")
      fields = ["puntaje","titulo","mensaje","imagen"]

class resenasborrar(PermissionRequiredMixin, DeleteView):
      permission_required = 'accounts.template_all'
      model = resenas
      success_url = reverse_lazy("listaresenas")