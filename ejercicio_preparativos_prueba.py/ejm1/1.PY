#definicion de funciones
def agregar_producto(productos):
    nombre=input("Nombre del producto: ").strip()

    if nombre.isdigit():
        print("Debe ingresar letras")
        return

    if nombre== "  ":
        print("El nombre no puede ser vacio")
        return
    
    if nombre in productos:
        print("El producto ya existe")
        return
    
    while True:
        try:
            stock = int(input("Ingrese stock:  "))
            if stock>0:
                break
            else:
                print("el stock debe mayor a cero")
        except ValueError:
            print("Debe ingresar un numero para stock!!, vuelva a intentar")
            

    
    while True:
        try:
            precio = int(input("Ingrese precio:  "))
            if precio>0:
                break
            else:
                print("Debe ingresar un numero para el precio")
        except:
            print("debe ingresar un numero!!, vuelve a intentar")
    
    

    productos[nombre] = [stock, precio]
    print("Productos agregados correctamente")

def mostrar_producto(productos):
    if len(productos)==0:
        print("No existen productos ")
        return
    for nombre in productos:
        print(nombre,"-stock",productos[nombre][1],"--precio:", productos[nombre[0]])


def buscar_producto(productos):
    if len(productos)==0:
        print("No existen productos ")
        return
    
    nombre= input("nombre producto a buscar:  ").strip()

    if nombre in productos:
        print("producto encontrado")
        print (f"stock: {productos[nombre][0]}")
        print (f"precio: $ {productos[nombre][1]}")
    else:
        print("Producto no existe o agotado!!")

def producto_mas_caro(productos):
    if len(productos)==0:
        print("no existen productos")
        return
    
    mayor=0
    mayor_nombre=" "

    for nombre in productos:
        precio =productos[nombre][1]

        if precio>mayor:
            mayor_nombre=nombre
    
    print(f"Producto mas caroes {mayor_nombre}")
    print(f"")




productos={ }

while True:
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto mas caro")
    print("5. Salir")

    while True:
        try:
            op=int(input("Seleccione una opcion:  "))
            break
        except ValueError:
            print("Error, debe ingresar un numero entre 1 y5, intente nuevamente")

    if op==1:
        agregar_producto(productos)
    elif op==2:
        mostrar_producto(productos)
      # print(productos)

    elif op==3:
        buscar_producto(productos)
       # print
    elif op==4:
        producto_mas_caro(productos)
        #print
    elif op==5:
        print("Fin del programa")
    else:
        print("Opcion Invalida")
