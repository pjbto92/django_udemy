

from django.urls import path
from django.contrib import admin
from miapp.views import index,pagina3,pagina2,contacto



urlpatterns = [
    path('',index),
    path('index/',index),
    path('pagina3/',pagina3),
    path('pagina2/',pagina2),
    path('contacto/',contacto),
    path('contacto/<str:nombre>',contacto),
    path('contacto/<str:nombre>/<str:apellidos>',contacto),

    path('admin/', admin.site.urls),
    #path('hola-mundo/',views.holamundo, name="hola_mundo")
]
