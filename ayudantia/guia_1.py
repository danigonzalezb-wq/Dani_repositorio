def mostrar_menu():
    print("""---Menu---
1._Agregar tarea
2._Eliminar tarea
3._Ver tareas ordenadas
4._Salir
          """)
    


def imprimir_tareas(lista_tareas):
    if len(lista_tareas)==0:
        print("No hay tareas")
    else:
        lista_tareas.sort()
        print("Tareas pedientes")
        for tareas in lista_tareas:
            print(f"-{tareas}")

tareas=[]
op=0
while True:
    mostrar_menu()
    try:
        op=int(input("Ingrese su opcion"))
        break
    except ValueError:
        print("Opcion invalida")


    if op==1:
        Agregar=input().strip().capitalize()
        tareas.append(Agregar)
        print("tarea agregada")

    elif op==2:
        quitar=input().strip().capitalize
        if quitar in tareas:
            print("tarea eliminada")
            tareas.remove(quitar)
        else:
            print("tarea no esta agregada a la lista")

    elif op==3:
        imprimir_tareas(tareas)

    elif op==4:
        print("Saliendo")
        break
    else:
        print("Opcion no valida")