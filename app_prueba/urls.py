
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.home, name='home'),
    path('hola/<str:id>',views.saludar),
    path('crearPersona/', views.crearPersona, name='crear'),
    path('listaPersona/', views.listaPersonas, name='lista'),
]