from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class suscformulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    contrasena= forms.CharField(max_length=30)
    email= forms.EmailField()


class betaformulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()


class inscformulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        #sacar los mensajes de ayuda
        help_texts = {k:"" for k in fields}

        
class itemsformulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    tipo= forms.CharField(max_length=30)
    dano_f= forms.CharField(max_length=30)
    dano_m= forms.CharField(max_length=30)
    descripcion= forms.CharField(max_length=400)
    imagen = forms.ImageField()