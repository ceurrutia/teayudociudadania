from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from portal import forms 

# Create your models here.

class Contacto(models.Model):
    nombre= models.CharField(verbose_name="Nombre", max_length=250, null=False, default="Usuario nombre")
    apellido= models.CharField(verbose_name="Apellido", max_length=250, null=False, default='Usuario Apellido')
    edad= models.IntegerField(verbose_name= "Edad")
    telefono= models.IntegerField(verbose_name="Teléfono")
    mail= models.EmailField(verbose_name="Mail", max_length=250, null=False, default="Mail defecto")
    mensaje = models.TextField(verbose_name="Mensaje", max_length=500)
    fecha_y_hora = models.DateTimeField(verbose_name="Fecha y hora", null=True,default=timezone.now)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} -{self.mail} - {self.mensaje}'


#recursos gestores y genealogistas

class Persona(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellido = models.CharField(verbose_name='Apellido', max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=250)
    telefono = models.IntegerField(verbose_name="telefono")
    pais = models.CharField(verbose_name='pais', max_length=50)
    ciudad = models.CharField(verbose_name='ciudad', max_length=50)
    sitio_web = models.CharField(verbose_name="sitio web", max_length=100, blank=False, default="website")
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.email} - {self.telefono} - {self.pais} - {self.ciudad} - {self.sitio_web}'

    def clean(self):
        if not (0 < self.telefono <= 999999999):
            raise ValidationError("El número de teléfono debe ser un número positivo y no tener más de 9 dígitos.")
        
    class Meta:
        abstract = True


class Gestor(Persona):
    nombre_gestoria = models.CharField(verbose_name="nombre_gestoria", max_length=16)
    logo_gestoria = models.ImageField(verbose_name="logo gestor", upload_to='imagenes/', null=True)

    
class Genealogista(Persona):
    nombre_genealogista = models.CharField(verbose_name="nombre_genealogista", max_length=16)
    logo_genealogista = models.ImageField(verbose_name="logo genealogista", upload_to='imagenes/', null=True)


    
#categorias de contenido

class Categorias(models.Model):
    nombre_categoria = models.CharField(verbose_name="Nombre categoria", max_length=100 , unique=True)
    
    def __str__(self) -> str:
        return f'{self.nombre_categoria} '
    
    class Meta:
       verbose_name_plural = "Categorias"
       
    
    class Selectfechas(models.Model):
        fecha_inicial = models.DateField(verbose_name="Fecha inicial")
        fecha_final = models.DateField(verbose_name="Fecha final ")
        
        def __str__(self) -> str:
            return f'{self.fecha_inicial} - {self.fecha_final} '
      