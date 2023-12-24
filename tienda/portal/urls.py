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
    path("consulados/", views.consulados, name="consulados"),
    path("ciudadania_italiana/", views.ciudadania_italiana, name="ciudadania_italiana"),
    path("ciudadania_espanola/", views.ciudadania_espanola, name="ciudadania_espanola"),
    
    
    #Crud gestores
    path('listado_gestores/', views.listado_gestores, name='listado_gestores'),
    path('create_gestor/', views.GestoresCreateView.as_view(), name = "create_gestor"),
    path('gestoria/<int:pk>/editar/', views.GestoresUpdateView.as_view(), name='gestor_editar'),
    path('gestoria/<int:pk>/eliminar/', views.GestoresDeleteView.as_view(), name='gestor_eliminar'),
    
    #Crud consulados
    path('listado_consulados/', views.listado_consulados, name='listado_consulados'),
    path('create_consulado/', views.ConsuladosCreateView.as_view(), name = "create_consulado"),
    path('consulados/<int:pk>/editar/', views.ConsuladosUpdateView.as_view(), name='consulado_editar'),
    path('consulados/<int:pk>/eliminar/', views.ConsuladosDeleteView.as_view(), name='consulado_eliminar'),
    
]
