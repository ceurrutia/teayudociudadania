from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from datetime import datetime
from django.template import Template
from portal.forms import contactForm, form_dif_fechas
from .models import Contacto
from datetime import datetime
from dateutil import relativedelta
from datetime import datetime

# Create your views here.


def index(request) -> HttpResponse:
    return render(request, 'index.html')


def base(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')

def gestores(request: HttpRequest) -> HttpResponse:
    return render(request, 'gestores.html')

def genealogistas(request: HttpRequest) -> HttpResponse:
    return render(request, 'genealogistas.html')

def acerca(request: HttpRequest) -> HttpResponse:
    return render(request, 'acerca.html')


def contacto(request):
    formulario_contacto = contactForm()

    if request.method == 'POST':
        formulario_contacto = contactForm(request.POST)
        if formulario_contacto.is_valid():
            nombre = formulario_contacto.cleaned_data.get('nombre')
            apellido=formulario_contacto.cleaned_data.get('apellido')
            mail = formulario_contacto.cleaned_data.get('mail')
            telefono = formulario_contacto.cleaned_data.get('telefono')
            mensaje = formulario_contacto.cleaned_data.get('mensaje')
            edad = formulario_contacto.cleaned_data.get('edad')
            if edad is not None and edad < 18:
                messages.error(request, 'Debes tener al menos 18 años para enviar el mensaje.')
            else:
                messages.success(request, 'Gracias! Hemos recibido tus datos. Muy pronto nos pondremos en contacto contigo.')
               
                # Crear una instancia del modelo Contacto y guardarla en la base de datos
                nuevo_contacto = Contacto(
                    nombre=nombre,
                    apellido=apellido,
                    mail=mail,
                    edad=edad,
                    telefono=telefono,
                    mensaje=mensaje,
                )
                nuevo_contacto.save()

                # Redireccionar a algún lugar después de guardar
                return redirect('contacto')

    # Si la solicitud es GET o no es válida, renderizar el formulario
    contexto = {
        'ahora': datetime.now,
        'formulario_contacto': formulario_contacto 
    }
    return render(request, "contacto.html", contexto)





def form_fechas(request):
    if request.method == 'POST':
        form = form_dif_fechas(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data.get('fecha_inicio')
            fecha_final = form.cleaned_data.get('fecha_final')

            diferencia = fecha_final - fecha_inicio
            diferencia_anios = diferencia.days // 365
            diferencia_meses = (diferencia.days % 365) // 30  # Asumiendo un mes como 30 días
            diferencia_dias = (diferencia.days % 365) % 30

            contexto = {
                'ahora': datetime.now(),
                'form_dif_fechas': form,
                'diferencia_anios': diferencia_anios,
                'diferencia_meses': diferencia_meses,
                'diferencia_dias': diferencia_dias,
            }

            return render(request, "form_fechas.html", contexto)
        else:
            # Si el formulario no es válido, muestra un mensaje de error
            messages.error(request, 'Error en el formulario')
    else:
        form = form_dif_fechas()  # Crea una nueva instancia del formulario

    contexto = {
        'ahora': datetime.now(),
        'form_dif_fechas': form
    }
    return render(request, "form_fechas.html", contexto)



            