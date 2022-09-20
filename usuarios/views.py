from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from administrador.forms import UsuarioForm
from usuarios.models import Usuario
from .Carrito import Carrito
from administrador.models import Elemento, Tipos_Elemento

def cusuario(request):
    titulo_pagina="usuario"
    usuario_db = Usuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario_nombre= form.cleaned_data.get('Unombre')
            messages.success(request,f'El usuario {usuario_nombre} se agregó correctamente!')
            return redirect('usuario-tablaUsuario')
    else:
        form = UsuarioForm()
    context={
        "titulo_pagina": titulo_pagina,
        "usuario_db": usuario_db,
        "form":form
    }
    return render(request,'usuarios/usuario-crear.html', context)

def tusuario(request):
    titulo_pagina="Usuarios"
    tusuarios= Usuario.objects.all()
    context={
        "tusuarios": tusuarios,
        "titulo_pagina":titulo_pagina
    }
    return render(request, "usuarios/tablaUsuario.html",context)

def vusuario (request,pk):
    titulo_pagina="Producto"
    usuario= Usuario.objects.get(Uid=pk) 
    print(usuario)
    context={
        "usuario": usuario,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"usuarios/verusuario.html", context)

def Editarusuario(request,pk):
    titulo_pagina="Producto"
    tusuarios= Usuario.objects.get(Uid=pk)
    if request.method == 'POST':
        form= UsuarioForm(request.POST, instance=tusuarios)
        if form.is_valid():
            form.save()
        return redirect('usuario-tablaUsuario')
    else:
        form= UsuarioForm(instance=tusuarios)
        
        context={
        "tusuarios": tusuarios,
        "titulo_pagina": titulo_pagina,
        "form":form
    }
    return render(request, "usuarios/crearUsuario.html", context)

def usuario_eliminar(request,pk):
    titulo_pagina='Usuarios'
    tusuarios= Usuario.objects.all()
    tusuario= Usuario.objects.get(Uid=pk)
    accion_txt= f"usuario {tusuario.Uid}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        Usuario.objects.filter(Uid=pk).update(
                    estado='Inactivo'
                )
        tusuario_nombre=  tusuario.Unombre
        messages.success(request,f'El usuario {tusuario_nombre} se eliminó correctamente!')
        return redirect('usuario-tablaUsuario')                           
    else:
        form:UsuarioForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "tusuarios": tusuarios,   
    }
    return render(request, "usuarios/usuario-eliminar.html", context)


def restablecercontraseña(request):
    titulo_pagina='Restablecer Contraseña'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/restablecercontraseña.html", context)

def accesorio(request):
    titulo_pagina='Accesorios'
    subcategorias= Tipos_Elemento.objects.filter(categoria="Accesorios")
    elementos = Elemento.objects.filter(tipo_elemento__categoria="Accesorios")
    context={
        "subcategorias":subcategorias,
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "usuarios/accesorios.html", context)

def producto(request):
    titulo_pagina='Productos'
    subcategorias= Tipos_Elemento.objects.filter(categoria="Productos")
    elementos = Elemento.objects.filter(tipo_elemento__categoria="Productos")
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
        "subcategorias":subcategorias,
    }
    return render(request, "usuarios/productos.html", context)

def serviciocliente(request):
    titulo_pagina='Servicios Cliente'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/servicioscliente.html", context)

def nosotros(request):
    titulo_pagina='Nosotros'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/nosotros.html", context)

def politicasprivacidad(request):
    titulo_pagina='Politicas de Privacidad'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/politicasprivacidad.html", context) 
    
def carrito(request):
    titulo_pagina='Carrito'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/carrito.html", context)

def agregar_elemento(request, elemento_id):   
    carrito = Carrito(request) 
    elemento = Elemento.objects.get(id=elemento_id) 
    carrito.agregar(elemento=elemento)
    return redirect("usuarios-carrito")

def eliminar_elemento(request, elemento_id):
    carrito = Carrito(request)
    elemento = Elemento.objects.get(id=elemento_id)
    carrito.eliminar(elemento=elemento)
    return redirect("usuarios-carrito")

def restar_elemento(request, elemento_id):
    carrito = Carrito(request)
    elemento = Elemento.objects.get(id=elemento_id)
    carrito.restar(elemento=elemento)
    return redirect("usuarios-carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("usuarios-carrito")

def detalle(request, pk, url_back):
    titulo_pagina='Detalles'
    db_elemento = Elemento.objects.get(id = pk)
    _url_back = f"/{url_back}"
    contex = {
        "titulo_pagina": titulo_pagina,
        'elemento': db_elemento,
        'url_back': _url_back,
    }
    return render(request, 'usuarios/detalles.html', contex)