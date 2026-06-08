dicc={}

def mostrar_menu():
    print("""1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir. """)

def ingreso_usuario(dicc):
   #nombre_usuario
    nombre_usuario =input("ingrese nombre: ")
    if nombre_usuario == " ":
        print("El nombre no puede estar vacio")
        return
    
    if nombre_usuario in ingreso_usuario:
        print("El alumno ya existe")
        return
    
    if nombre_usuario.isdigit():
        print("El nombre debe ser letras ")
        return
    
    nombre_usuario
    
    # sexo_usuario
    sexo_usuario=input("ingrese su genero(F/M): ").strip()

    if sexo_usuario=="F":

        print()
    elif sexo_usuario=="M":
        print()
    else:
        print("ingrese genero")
        return
    
    # contraseña_usuario
    contraseña_usuario=input("Ingrese su contraseña").strip()

    if contraseña_usuario==" ":
        print("ingrese contraseña")
    else:
        print("contraseña agregada ")

    contra=[]

    for i in range(contraseña_usuario):
        contra=input("contraseña: ")
    
    dicc[nombre_usuario]=contra


   
def buscar_usuario():
   buscar=input("ingrese usuario a buscar: ")
   for nombre_usuario in ingreso_usuario:
       nombre_usuario

def eliminar_usuario():
     quitar=input().strip().capitalize
     if quitar in dicc:
        print("Nombre eliminada")
        dicc.remove(quitar)


op=0
while True:
    mostrar_menu()

    while True:
        try:
            op=int(input("ingrese su opcion a elegir:  "))
            break
        except ValueError:
            print("error, opcion invalida")
        
        
    if op==1:
         
         ingreso_usuario(dicc)

    elif op==2:
            buscar_usuario
            print
    elif op==3:
            eliminar_usuario()
    elif op==4:
            print("saliendo")
            break
    else:
            print("Opcion no valida, intente nuevamente")

        

