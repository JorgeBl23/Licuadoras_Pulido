from tkinter import Widget
from django import forms
from facturas.models import Factura, Detalle

class FacturaForm(forms.ModelForm):
    class Meta: 
        model = Factura
        fields = [ 'tipofactura']
        
class DetalleForm(forms.ModelForm):
    class Meta: 
        model = Detalle
        fields = ['elemento', 'cantidad']

