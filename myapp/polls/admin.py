from django.contrib import admin

from .models import Preguntas
from .models import Opciones

admin.site.register(Preguntas)
admin.site.register(Opciones)

# Register your models here.
