bd_estudiantes=[]

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes ")
    print("6. Salir")

def leer_opcion():
    op=input("..")

    if op in ["1","2","3","4","5","6"]:
        return int(op)
    return False

def validar_nombre(nombre):
    if len(nombre.strip())>0:
        return True
    return False

def validar_nota(nota):
    try:
        numero=float(nota)
        if 1.0<= numero<= 7.0:
            return True
        return False
    except ValueError:
        return False
    
def validar_edad(edad):
    if edad.isdigit() and int(edad)>0:
        return True
    return False

def agregar_estudiante(lista):
    nombre=input("ingresa el nombre del estudiante")
    if validar_nombre(nombre)==False:
        print("el nombre no puede estar vacio")
        return
    
    edad = input("ingresa la edad")
    if validar_edad(edad)==False:
        print("la edad debe ser mayor a cero")
        return
    
    nota=input("(1.0 a 7.0) ingrese la nota")
    if validar_nota(nota)==False:
        print("la nota debe ser entre 1.0 a 7.0")
        return
    
    estudiante={"nombre": nombre,
                "edad": int(edad),
                "nota": float(nota),
                "aprobado": False
                }
    
    lista.append(estudiante)
    print("estudiante registrado con exito")


def buscar_estudiante(lista, nombre_buscado):
    for i in range(lista):
        if lista[i]["nombre"]==nombre_buscado:
            return i
        
def actualiza_estado(lista):
    for estudiante in lista:
        if estudiante["nota"]>=4.0:
            estudiante["aprobado"]= True
        else:
            estudiante["aprobado"]= False

def mostrar_estudiante(lista):
    actualizar_estado(lista)

    if len(lista)==0:
        print("")
        return
    
    print(" ")
    for estudiantes in lista["aprobado"]== True:
        estado="aprobado"
    else:
        estado="reprobado"





