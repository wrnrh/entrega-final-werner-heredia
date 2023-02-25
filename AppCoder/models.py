from django.db import models

# Create your models here.

class suscripcion(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - Contraseña: {self.contrasena} - Email: {self.email}"
    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=30)
    email= models.EmailField()

class betatester(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()

class inscripcion(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()


class items(models.Model):

    nombre = models.CharField(max_length=30)
    tipo= models.CharField(max_length=30)
    dano_f= models.CharField(max_length=30)
    dano_m= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=400)
    imagen = models.ImageField(upload_to='items', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.tipo} - {self.dano_f} -  {self.dano_m} -  {self.descripcion}'


Puntuacion = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)
class resenas(models.Model):
    puntaje= models.CharField(
        max_length = 20,
        choices = Puntuacion,
        default = '5'
        )
    titulo= models.CharField(max_length=30)
    mensaje= models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='items', null=True, blank=True)
    
    def __str__(self):
        return f'{self.puntaje} - {self.titulo}'