from django import forms

class formPersona(forms.Form):
    nombre = forms.CharField(label='Nombre de la persona', max_length=199)
    apellido = forms.CharField(label='Apellido de la persona', max_length=199)
    