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
    
    