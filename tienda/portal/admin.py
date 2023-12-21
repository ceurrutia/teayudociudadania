from django.contrib import admin
from portal.models import Gestor, Contacto, Genealogista, Consulado

# Register your models here.

admin.site.register(Gestor)
admin.site.register(Genealogista)
admin.site.register(Contacto)
admin.site.register(Consulado)