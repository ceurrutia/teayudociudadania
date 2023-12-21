import re
from django import forms
from django.core.exceptions import ValidationError


def custom_validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')

def clean_edad(self):
    if self.cleaned_data['edad'] < 18:
        raise ValidationError('El usuario no puede tener menos de 18 años')

class contactForm(forms.Form):
    
    nombre = forms.CharField(
        label="Nombre",
        max_length=20, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'})
        )
    apellido = forms.CharField(
        label="Apellido",
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido'})
        )
    mail = forms.EmailField(
        label="Email ",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu email'})
        )
    edad = forms.IntegerField(
        label="Edad",
        required= True, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu edad'})
    )
    telefono = forms.IntegerField(
        label="Telefono",  
        required= True, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu telefono' })
    )
    mensaje = forms.CharField(
        label="Mensaje", 
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe aqui tu consulta'})
        )
    
#Form calculador de fechas   
    
class form_dif_fechas(forms.Form):
    fecha_inicio = forms.DateField(
        label="Fecha inicial", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la fecha de nacimiento en formato dd/mm/aaaa' })
        )
    fecha_final = forms.DateField(
        label="Fecha final", 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la fecha de casamiento o defunción formato dd/mm/aaaa' })
        )
    
    #Forms gestores
    
    
class FormCreateGestor(forms.Form):
    nombre_gestoria = forms.CharField(label='Nombre gestoria:', required=True)
    logo_gestoria = forms.ImageField(label='Logo gestoria:', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url de la imagen: '}))
    
class FormEditGestor(forms.Form):
    nombre_gestoria = forms.CharField(label='Nombre gestoria', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nuevo nombre de la gestoria'}))
    logo_gestoria = forms.ImageField(label='Logo gestoria', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url nuevo logo de la gestoria'}))


#Forms genealogistas
    
    
class FormCreateGnealogista(forms.Form):
    nombre_genalogista = forms.CharField(label='Nombre genealogista:', required=True)
    logo_genalogista = forms.ImageField(label='Logo genalogista:', required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url de la imagen: '}))
    
class FormEditGenealogista(forms.Form):
    nombre_genealogista = forms.CharField(label='Nombre genealogista', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nuevo nombre de la genealogista'}))
    logo_genalogista = forms.ImageField(label='Logo genalogistaa', required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese url nuevo logo de genalogista'}))


#Forms consulados

class FormCreateConsulado(forms.Form):
    nombre_consulado = forms.CharField(label='Nombre consulado:', required=True)
    horarios = forms.CharField(label='horarios:', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese horarios del consulado: '}))
    
class FormEditConsulado(forms.Form):
    nombre_consulado = forms.CharField(label='Nombre consulado', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nuevo nombre del consulado: '}))
    horarios = forms.CharField(label='horarios:', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese horarios del consulado: '}))
