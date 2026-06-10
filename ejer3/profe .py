"""usuario={
    "dani":{"sexo":"M",
            "pass":"123jjgjhsfu"
            }
    
}"""
#funciones
def ingresar_usuario():
    while True:
        nombre=input("ingrese nombre de usuario")

        if nombre in usuario:
            print("el usuario ya existe")
        else:
            break

    
    while True:
        sexo=input("ingrese sexo(M/F): ").upper()
        if sexo=="M" or sexo=="F":
            break
        else:
            print("debe ingresar genero")
    
    while True:
        contraseña=input("ingrese contraseña: ")
        validar_contraseña(contraseña)
        if validar_contraseña(contraseña):
            #print("contraseña valida")
            break
        else:
            print("contraseña invalida, debe tener 8 caracteres en letras y numeros")
    
    usuario[nombre]={
        "sexo": sexo,
        "contraseña": contraseña
    }

    print("datos ingresado correctamente")

def validar_contraseña(contraseña):
    if len(contraseña) <8:
        return False
    
    if " " in contraseña:
        return False
    
    num=False
    letra=False

    for caracter in contraseña:
        if caracter.isdigit():
            num=True
        if caracter.isalpha():
            letra=True
    
    return num and letra

def buscar_usuario():
    nombre=input("ingrese el usuario a buscar: ")

    if nombre in usuario:
       
        print(f"sexo:{usuario[nombre]["sexo"]}")
        print(f"contraseña:{usuario[nombre]["contraseña"]}")
    else:
        print("usuario no encontrado")
    

def eliminar_usuario():
    nombre = input("Ingrese usuario para buscar: ")

    if nombre in usuarios:
         del usuarios[nombre]
         print("Usuario eliminado")
    else:
         print("No existe usuario!")

#menu principal
usuario={}

while True:
    print("---menu principal")
    print("1._Ingresar usuario")
    print("2._buscar usuario")
    print("3._eliminar usuario")
    print("4._salir")

    while True:
        try:
            op=int(input("ingrese su opcion"))
            break
        except ValueError:
            print("error, ingrese un valor valido, intente de nuevo")
    
    if op==1:
        ingresar_usuario()
    elif op==2:
       buscar_usuario
    elif op==3:
       eliminar_usuario
    elif op==4:
        print("saliendo...")
        break
    else:
        print("error")
