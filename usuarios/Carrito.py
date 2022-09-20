class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]={}
        # else:
        self.carrito = carrito

    def agregar(self, elemento):
        if(str(elemento.id) not in self.carrito.keys()):
            self.carrito[elemento.id]={
                "elemento_id": elemento.id,
                "nombre": elemento.nombre,
                "precio": str(elemento.precio),
                "cantidad": 1,
                "foto": elemento.foto.url
            }
        else:
            for key, value in self.carrito.items():
                if key==str(elemento.id): 
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+elemento.precio
                    break
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, elemento):
        elemento.id=str(elemento.id)
        if elemento.id in self.carrito:
            del self.carrito[elemento.id]
            self.guardar_carrito()

    def restar(self, elemento):
        for key, value in self.carrito.items():
            if key==str(elemento.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-elemento.precio
                if value["cantidad"]<1:
                    self.eliminar(elemento)
                break
        self.guardar_carrito()
                    
            
    def limpiar (self):
        self.session["carrito"] = {}
        self.session.modified = True
                