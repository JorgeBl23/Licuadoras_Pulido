from django.db import models
from django.utils.translation import gettext_lazy as _

class Rol(models.Model):
    Rid=models.AutoField(primary_key=True)
    Rnombre=models.CharField(max_length=20)
    class Meta:
        db_table="usuarios_rol"
    def __str__(self) -> str:
        return "%s "% (self.Rnombre)
    
    
class Usuario(models.Model):
    Uid=models.AutoField(primary_key=True)
    documento=models.CharField(unique=True,max_length=10)
    class Tipo_documento(models.TextChoices):
        Cedula_ciudadania='C.C', _('C.C')
        Tarjeta_identidad='T.I', _('T.I')
        Cedula_extranjeria='C.E', _('C.E')
    tipo_documento= models.CharField(max_length=3, choices=Tipo_documento.choices, verbose_name="Tipo documento")  
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Proveedor='Proveedor', _('Proveedor')
        Asociada='Trabajador', _('Trabajador')
        Cliente='Cliente', _('Cliente')
    rol= models.CharField(max_length=13, choices=Rol.choices, verbose_name="rol",blank=True)  
    Unombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    celular=models.CharField(unique=True,max_length=10)
    correo= models.EmailField( max_length=25)
    ciudad= models.CharField(max_length=50)
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
        ANULADO='Anulado', _('Anulado')
    estado= models.CharField(max_length=10, choices=Estado.choices, verbose_name="Estado", default=Estado.ACTIVO) 
    class Meta:
        db_table="usuarios_usuario"
    def __str__(self) -> str:
        return "%s / %s  "% (self.Unombre, self.rol)
    def clean(self):
        self.nombre= self.Unombre.title()
    
class Uadministrador(models.Model):
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Proveedor='Proveedor', _('Proveedor')
        Asociada='Trabajador', _('Trabajador')
        Cliente='Cliente', _('Cliente')
    rol= models.CharField(max_length=13, choices=Rol.choices, verbose_name="rol")  
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    documento=models.CharField(unique=True,max_length=10)
    celular=models.CharField(unique=True,max_length=10)
    class Tipo_documento(models.TextChoices):
        Cedula_ciudadania='C.C', _('C.C')
        Tarjeta_identidad='T.I', _('T.I')
        Cedula_extranjeria='C.E', _('C.E')
    tipo_documento= models.CharField(max_length=3, choices=Tipo_documento.choices, verbose_name="Tipo documento")
    def __str__(self) -> str:
        return "%s"% (self.nombre, self.apellido)
    def clean(self):
        self.nombre= self.nombre.capitalize()
        self.apellido= self.apellido.capitalize()