from django.shortcuts import render
from usuarios.Carrito import Carrito
from administrador.models import Elemento, Favorito

def inicio(request):
    favoritos= Elemento.objects.filter(favorito=True)
    print(favoritos)
    titulo_pagina='Inicio'
    carrito = Carrito(request) 
    context={
        "carrito": carrito,
        "favoritos":favoritos,
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "index.html", context)