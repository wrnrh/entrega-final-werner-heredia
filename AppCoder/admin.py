from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(suscripcion)

admin.site.register(betatester)

admin.site.register(inscripcion)

admin.site.register(items)
