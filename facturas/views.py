from django.shortcuts import render, redirect
from django.template import context
from facturas.models import Factura, Detalle
from facturas.forms import FacturaForm, DetalleForm
from django.contrib import messages 
from usuarios.models import Rol, Usuario
from usuarios.Carrito import Carrito
from administrador.models import *

def carrito(request):
    titulo_pagina='Carrito'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/carrito.html", context)

def factura(request):
    if request.method == 'POST':
        print(request.POST)
        aux= Factura.objects.create(
            tipofactura= request.POST['tipofactura']
        )
        messages.success(request,f'!La factura se agregó correctamente!')
        return redirect('factura-detalle',aux.id)
    else:
        messages.error(request,f'!Error al agregar Factura!')
    context={
    }
    return render(request,'factura/crearFactura.html', context)

def tfactura(request):
    titulo_pagina="Facturas"
    Rol_c=Rol.objects.all()
    Usuario_c=Usuario.objects.all()
    renew = '/factura/factura'
    tfacturas= Factura.objects.all()
    context={
        "tfacturas": tfacturas,
        "renew":renew,
        "titulo_pagina":titulo_pagina,
        "Rol":Rol_c,
        "Usuario":Usuario_c
    }
    return render(request, "factura/factura.html",context)

def vfactura (request,pk):
    renew = 'hola mundo'
    titulo_pagina="Factura"
    factura= Factura.objects.get(id=pk)
    detalles= Detalle.objects.filter(factura_id=pk)
    print(detalles)
    context={
        "factura": factura,
        "titulo_pagina":titulo_pagina,
        "renew":renew,
        "detalles":detalles
    }
    return render(request,"factura/verfactura.html", context)

def detalle(request,pk):
    titulo_pagina="facturas"
    detalles= Detalle.objects.filter(factura_id=pk)
    factura_u= Factura.objects.get(id=pk)
    if factura_u.tipofactura == "Compra":
        rol_aux= "Proveedor"
    elif factura_u.tipofactura == "Venta":    
        rol_aux= "Cliente"
    else:
        rol_aux= "servicio"
    usuario= Usuario.objects.filter(rol=rol_aux)
    servicio= Servicio.objects.all()
    if request.method == 'POST' and "form-detalle" in request.POST:
        form= DetalleForm(request.POST)
        detalle_aux= Detalle.objects.filter(factura_id=pk,elemento_id=request.POST['elemento'])
        if detalle_aux.exists():
            detalle_aux= Detalle.objects.filter(factura_id=pk,elemento_id=request.POST['elemento'])
        else:
            detalle_aux=None
        if detalle_aux == None:
            if form.is_valid():
                factura= Detalle.objects.create(
                cantidad=form.cleaned_data.get('cantidad'),
                elemento= form.cleaned_data.get('elemento'),
                factura=factura_u,        
                )
                if factura_u.tipofactura == "Venta":
                    id = Detalle.objects.values_list('id', flat=True)
                    cantidadp = Detalle.objects.all()[len(id)-1].elemento_id
                    cantidad_stock = Detalle.objects.all()[len(id)-1].cantidad
                    elemento = Elemento.objects.get(id=cantidadp)
                    if cantidad_stock > elemento.stock_elemento:
                       Detalle.objects.filter(id= len(id) ).update(
                            cantidad = elemento.stock_elemento  
                            )
                       cantidad_resta = Detalle.objects.get(id = len(id) ).cantidad
                       Elemento.objects.filter(id = cantidadp ).update(
                           stock_elemento = elemento.stock_elemento - cantidad_resta
                       )
                    else:
                        Elemento.objects.filter(id=cantidadp).update(
                        stock_elemento = elemento.stock_elemento   -  cantidad_stock
                        )
                elif  factura_u.tipofactura == "Compra":
                      id = Detalle.objects.values_list('id', flat=True)
                      cantidadp = Detalle.objects.all()[len(id)-1].elemento_id
                      cantidad_stock = Detalle.objects.all()[len(id)-1].cantidad
                      elemento = Elemento.objects.get(id=cantidadp)
                      Elemento.objects.filter(id=cantidadp).update(
                        stock_elemento = elemento.stock_elemento   +  cantidad_stock
                        )
                # messages.success(request,f' se agregó {elemento} al la factura correctamente!')
                return redirect('factura-detalle', pk=pk)    
        else:
        #     stock_elemento = Detalle.objects.get(id=pk)
        #     elemento = Elemento.objects.get(id=pk)
        #     stock_elemento = int(request.POST["cantidad"])
        #     Elemento.objects.filter(id=pk).update(
        #     stock_elemento = elemento.stock_elemento + stock_elemento
        #     )
          if factura_u.tipofactura == "Venta":
            id = Detalle.objects.values_list('id', flat=True)
            # este elemento tiene que ser dinamico 
            cantidadp = Detalle.objects.all()[15].elemento_id
            stock_elemento = int(request.POST["cantidad"])
            elemento__xd = Elemento.objects.filter(id=cantidadp)
            print('abshabvghsgfagscf3', elemento__xd)
            return redirect('factura-detalle', pk=pk)  
    else:
        form= DetalleForm()
    if request.method == 'POST' and "form-serv" in request.POST:
        print(request.POST)
        if request.POST["servicio"] and request.POST["servicio"] != "--- Seleccione el servicio ---":
            usuario_final=Servicio.objects.get(id=request.POST["servicio"]).usuario
            Factura.objects.filter(id=pk).update(
                usuario=usuario_final,
                servicio= request.POST["servicio"]
            )
            return redirect('factura-detalle', pk=pk)
    else:
            print('Seleccione un sevicio!')
            messages.warning(request,f'Seleccione un servicio!')
    if request.method == 'POST' and "form-user" in request.POST:
            print(request.POST)
            if request.POST["usuario"] and request.POST["usuario"] != "null":
                usuario_final=Usuario.objects.get(Uid=request.POST["usuario"])
                Factura.objects.filter(id=pk).update(
                    usuario=usuario_final,
                )
            return redirect('factura-detalle', pk=pk)
    else:
            print('Seleccione un usuario!')
            messages.warning(request,f'Seleccione un usuario!')
    context={
        "usuario":usuario,
        "servicio":servicio,
        "titulo_pagina": titulo_pagina,
        "detalles": detalles,
        "form":form,
        "factura":factura_u
    }
    return render(request, "factura/detalle-factura.html", context)


def detalle_estado(request,pk ):
    titulo_pagina='elemento'
    u_detalles= Detalle.objects.get(id=pk)
    factura_u= u_detalles.factura
    detalles= Detalle.objects.filter(factura_id=factura_u.id)
    accion_txt= f"Eliminando detalle {u_detalles.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= DetalleForm(request.POST)
        form = DetalleForm(request.POST)
        u_detalles.delete()
        messages.success(request,f'El detalle de factura  se eliminó correctamente!')
        return redirect('factura-detalle',factura_u.id)    
    else:
        form=DetalleForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "detalles": detalles,
            "factura":factura_u,
            "form":form,    
        }
    return render(request, "factura/detalle-eliminar.html", context) 

def detalle_eliminar(request,pk):
    titulo_pagina='Marca'
    detalles= Detalle.objects.all()
    detalle= Detalle.objects.get(id=pk)
    accion_txt= f"la marca {detalle.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        detalle.delete()
        detalle_elemento= detalle.elemento
        messages.success(request,f'La marca {detalle_elemento} se eliminó correctamente!')
        return redirect('detalle_estado')
    else:
        form:DetalleForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "detalles": detalles,
        }
    return render(request, "factura/detalle-factura.html", context)
    
def factura_estado(request,pk, estado):
    titulo_pagina='Factura'
    tfacturas= Factura.objects.all()
    tfactura= Factura.objects.get(id=pk)
    eliminacion= Detalle.objects.filter(factura=tfactura)
    estado_msj=""
    estado_txt=""
    if estado == "Abierta":
        if not eliminacion.exists():
            estado_txt= "Eliminar"
            estado_msj= f"factura {tfactura.id}, una vez Eliminada ETC!"
            if request.method == 'POST':
                form = FacturaForm(request.POST)  
                tfactura.delete()
                messages.success(request,f'factura {pk} se eliminó correctamente!')
                return redirect('factura-tfactura')
            else:
                form=FacturaForm()
        else:
            print("la factura {pk} no se puede eliminar tiene elementos registrados!")
            messages.warning(request,f'la factura {pk} no se puede eliminar tiene elementos registrados!')
            return redirect('factura-tfactura')
    elif estado == "Cerrada":
        estado_txt= "Anular"
        estado_msj= f"factura {tfactura.id}, una vez Anulada ETC!"
        if request.method == 'POST':
            form = FacturaForm(request.POST)
            Factura.objects.filter(id=pk).update(
                        estado='Anulada'
                    )
            tfactura_usuario=  tfactura.usuario
            messages.success(request,f'factura {tfactura.id} se anuló correctamente!')
            return redirect('factura-tfactura')
        else:
            form=FacturaForm()
    else:
        estado_txt= "Cerrar"
        estado_msj= f"{estado_txt} la factura {tfactura.id}, una vez Cerrada ETC!"
        if request.method == 'POST':
            form = FacturaForm(request.POST)
            Factura.objects.filter(id=pk).update(
                        estado='Cerrada'
                    )
            tfactura_usuario=  tfactura.usuario
            messages.success(request,f'factura {tfactura.id} se anuló correctamente!')
            return redirect('factura-tfactura')
        else:
            form:FacturaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "estado_msj":estado_msj,
            "estado_txt":estado_txt,
            "tfacturas": tfacturas,
    }
    return render(request, "factura/factura-estado.html", context)

def factura_anular(request,pk):
    titulo_pagina='Factura'
    tfacturas= Factura.objects.all()
    tfactura= Factura.objects.get(id=pk)
    accion_txt= f"factura {tfactura.id}, una vez anulada ETC!"
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        Factura.objects.filter(id=pk).update(
                    estado='Anulada'
                )
        tfactura_usuario=  tfactura.usuario
        messages.success(request,f'factura {tfactura.id} se anuló correctamente!')
        return redirect('factura-tfactura')                
    else:
        form:FacturaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "tfacturas": tfacturas,
        }
    return render(request, "factura/factura-eliminar.html", context)