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
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Categorias
from typing import Any
from django.urls import reverse_lazy
from .models import Gestor, Genealogista

# Create your views here.


def index(request) -> HttpResponse:
    return render(request, 'index.html')


def base(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')

def gestores(request):
    gestores = Gestor.objects.all()  
    return render(request, 'gestores.html', {'gestores': gestores})

def genealogistas(request):
    genealogistas = Genealogista.objects.all()  
    return render(request, 'genealogistas.html', {'genealogistas': genealogistas})


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


#Caluclador de fechas


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

#Crud gestores

    
def listado_gestores(request):
    gestores = Gestor.objects.all() 
    return render(request, "administracion/listado_gestores.html", {'gestores': gestores})


class Gestores(ListView):
    model = Gestor
    context_object_name = 'gestores'
    template_name = 'administracion/listado_gestores.html'
    ordering = ['nombre_gestoria']

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if 'nombre_gestoria' in request.GET:
            self.queryset = self.queryset.filter(nombre_gestoria__contains=request.GET['nombre_gestoria'])

        return super().get(request, *args, **kwargs)


class GestoresCreateView(CreateView):
    model = Gestor
    fields = ['nombre_gestoria', 'logo_gestoria', 'servicios', 'email', 'telefono', 'pais', 'ciudad']
    template_name = 'administracion/create_gestor.html'
    success_url = reverse_lazy('administracion/create_gestor')


class GestoresUpdateView(UpdateView):
    model = Gestor
    fields = ['nombre_gestoria', 'logo_gestoria', 'servicios', 'email', 'telefono', 'pais', 'ciudad']
    template_name = 'administracion/create_gestor.html'
    success_url = reverse_lazy('listado_gestores')


class GestoresDeleteView(DeleteView):
    model = Gestor
    template_name = 'administracion/gestor_eliminar.html'
    success_url = reverse_lazy('listado_gestores')
    
    #Genealogistas
    
def listado_genealogistas(request):
    genealogistas = Genealogista.objects.all() 
    return render(request, "administracion/listado_genealogistas.html", {'genealogistas': genealogistas})


class Genealogistas(ListView):
    model = Genealogista
    context_object_name = 'genealogistas'
    template_name = 'administracion/listado_genealogistas.html'
    ordering = ['nombre_genealogista']

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if 'nombre_genealogista' in request.GET:
            self.queryset = self.queryset.filter(nombre_genealogista__contains=request.GET['nombre_genealogista'])

        return super().get(request, *args, **kwargs)


class GenealogistasCreateView(CreateView):
    model = Genealogista
    fields = ['nombre_genealogista', 'logo_genealogista', 'servicios', 'email', 'telefono', 'pais', 'ciudad']
    template_name = 'administracion/create_genealogista.html'
    success_url = reverse_lazy('administracion/create_genealogista')


class GenealogistasUpdateView(UpdateView):
    model = Genealogista
    fields = ['nombre_genealogista', 'logo_genealogista', 'servicios', 'email', 'telefono', 'pais', 'ciudad']
    template_name = 'administracion/create_genealogista.html'
    success_url = reverse_lazy('listado_genealogistas')


class GenealogistasDeleteView(DeleteView):
    model = Genealogista
    template_name = 'administracion/genealogista_eliminar.html'
    success_url = reverse_lazy('listado_genealogistas')