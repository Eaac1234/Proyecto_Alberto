import os
productos=["Essential Force 5500","Essential Force(Tabletas)",
"Galombrix","Tyfenicol","Galocox 2.5%","Galocox(Tabletas)"]

productos_subtipos={"Essential Force 5500":{"10ml":245,"30ml":500,"100ml":1125},
                    "Essential Force(Tabletas)":{"50 Tabletas":215,"100 Tabletas":400,"500 Tabletas":1490},
                    "Galombrix":{"25 Tabletas":130,"50 Tabletas":210,"100 Tabletas":350,"500 Tabletas":1490},
                    "Tyfenicol":{"30ml":250,"100ml":480,"250ml":1150,"10x10ml":990},
                    "Galocox 2.5%":{"120ml":250,"1 litro":1750,"10x20ml":495},
                    "Galocox(Tabletas)":{"100 Tabletas":450,"500 Tabletas":1470}}

pedido={}

ciclo=True
def producto(numero):
    return productos[numero-1]

def subtipo(producto,subtipos):
    os.system("cls")
    i=1
    print("Producto\t\t\t\t\t"+"Precio MXM")
    for a,b in subtipos.items():
        print(str(i)+" "+str(producto)+" "+str(a)+"\t\t\t"+str(b))
        i=i+1
    numero=int(input("Ingrese el numero del producto a seleccionar:"))
    cantidad=int(input("ingrese el numero de piezas del producto:"))
    i=1
    for a,b in subtipos.items():
        if i==numero:
            pedido[str(producto)+" "+str(a)]={"precio":b,"cantidad":cantidad}
            break
        i=i+1

def precio(descuento):
    total=0
    os.system("cls")
    print("Producto\t\t\tCantidad\t\t\tTotal sin descuento(MXM)")
    for a,b in pedido.items():
        print(str(a)+"\t\t"+str(b["cantidad"])+"\t\t\t\t\t"+str(b["precio"]*b["cantidad"]))
        total=total+(b["precio"]*b["cantidad"])
    
    print("\n\n")
    print("El total sin descuento es: $"+str(total))
    descuento_precio=total*descuento
    print("El descuento del "+str(descuento*100)+"% es de: $"+str(descuento_precio))
    total=total-descuento_precio
    print("El precio a pagar es: $"+str(total))
        


while ciclo:
    os.system("cls")
    print("Seleccion de Productos\n")
    i=1
    for a in productos:
        print(str(i)+" "+a)
        i=i+1
    selector=int(input("Ingresa el numero del producto a seleccionar:"))
    seleccion=producto(selector)
    subtipo(seleccion,productos_subtipos[seleccion])
    os.system("cls")
    logica=int(input("Escribe 1 para ingresar otro producto o escribe 0 para ingresar el descuento:"))
    if logica!=1:
        ciclo=False

os.system("cls")
descuento=float(input("Ingresa el descuento en numero decimal:"))
precio(descuento)








