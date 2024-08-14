from django import forms
from .models import Producto 

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']
