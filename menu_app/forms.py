from django import forms

class Img(forms.Form):
    Ingresa_imagenes = forms.ImageField()