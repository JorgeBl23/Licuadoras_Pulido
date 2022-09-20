from dataclasses import field
from django.forms import ModelForm, Textarea
from administrador.models import *
from usuarios.models import Usuario
# from usuarios.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rol','Unombre','apellido','tipo_documento','documento','celular']
           
class TipoElementoForm(ModelForm):
    class Meta:
        model= Tipos_Elemento
        fields=['categoria','subcategoria']
        
class TipoElementoEditarForm(ModelForm):
    class Meta:
        model= Tipos_Elemento
        fields=['categoria','subcategoria']
        
class ElementoForm(ModelForm):
    class Meta:
        model= Elemento
        fields= ['tipo_elemento','nombre','marca','descripcion','precio', 'foto']

class ElementoEditarForm(ModelForm):
    class Meta:
        model= Elemento
        fields= ['tipo_elemento','nombre','marca' ,'descripcion','precio', 'foto','favorito']
        
class TipoElementoFavoritoForm(ModelForm):
    class Meta:
        model= Favorito
        fields= ['favorito']
                
class MarcaForm(ModelForm):
    class Meta:
        model= Marca
        fields= ['nombre']
        
class MarcaEditarForm(ModelForm):
    class Meta:
        model= Marca
        fields= ['nombre']

class ElectrodomesticoForm(ModelForm):
    class Meta:
        model= Electrodomestico
        fields=['nombre', 'marca', 'referencia']

class ElectrodomesticoEditarForm(ModelForm):
    class Meta:
        model= Electrodomestico
        fields=['nombre', 'marca', 'referencia']
        
class ServicioForm(ModelForm):
    class Meta:
        model= Servicio
        fields=['usuario','tiposervicio', 'electrodomestico','observacion', 'fallas_basicas', 'diagnostico']
        widgets = {
            'observacion': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class ServicioEditarForm(ModelForm):
    class Meta:
        model= Servicio
        fields=['tiposervicio', 'electrodomestico', 'fallas_basicas','observacion', 'diagnostico']
        
class StockForm(ModelForm):
    class Meta:
        model= Stock
        fields=['stock_stock']
           
class CopiaseguridadForm(ModelForm):
    class Meta:
        model= Copiaseguridad
        fields= ['nombre','archivo']