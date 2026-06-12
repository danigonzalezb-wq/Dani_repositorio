contactos={}

def pedir_opcion():
    op=input("[A]agregar contacto,[B]buscar contacto,[S]salir")
    return op

def buscar_numero(agenda,nombre_buscado):
    if nombre_buscado in agenda:
        return agenda[nombre_buscado]
    else:
        return"el contato no existe en la agenda"
    
while True:
    opcion=pedir_opcion()

    if opcion=="A":
        nombre=input("ingresa el nombre").strip().title()
        numero=input("ingresar elm telefono").strip().title()

        contactos[nombre]=numero
        print(f"contacto {nombre} guardado")
    
    elif opcion=="B":
        nombre=input("Buscandocontacto:  ").strip().title()

        resultado=buscar_numero(contactos, nombre)
        print(f"Resultado: {resultado}")
    
    elif opcion=="S":
        print("saliendo..")
    
    else:
        print("opcion invalida")