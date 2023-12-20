from django.urls import path
from portal import views


urlpatterns = [
    # Usar una cadena vacía para que sea la URL de inicio.
    path("", views.index, name="index"),
    path("contacto/", views.contacto, name="contacto"),
    path("gestores/", views.gestores, name="gestores"),
    path("base/", views.base, name="base"),
    path("acerca/", views.acerca, name="acerca"),
    path("form_fechas/", views.form_fechas, name="form_fechas"),
    path("genealogistas/", views.genealogistas, name="genealogistas"),
    
    #Crud gestores
    path('listado_gestores/', views.listado_gestores, name='listado_gestores'),
    path('create_gestor/', views.GestoresCreateView.as_view(), name = "create_gestor"),
    path('gestoria/<int:pk>/editar/', views.GestoresUpdateView.as_view(), name='gestor_editar'),
    path('gestoria/<int:pk>/eliminar/', views.GestoresDeleteView.as_view(), name='gestor_eliminar'),
    
]
