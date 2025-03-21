
from django.urls import path
from . import views
urlpatterns = [
    path('<str:usuario>',views.index),
    path('login/',views.home),
    path('hola/<str:nombre>',views.saludar),
]