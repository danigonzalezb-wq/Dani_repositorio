#Agregado
def leer_nota(mensaje):
    while True:
        try:
            nota=float(input(mensaje))
            if nota >=1.0 and nota <=7.0:
                return nota
            print("La nota debe estar entre 1.0 y 7.0")
        except ValueError:
            print("debe ingresar una nota valida")
#1
def agregar_alumno(alumnos):
    nombre = input("Nombre del alumno:  ").strip()

    if nombre=="":
        print("El nombre no puede estar vacio")
        return
    
    if nombre in alumnos:
        print("El alumno ya existe")
        return
    
    if nombre.isdigit():
        print("El nombre debe ser letras ")
        return
    
    cantidad=int(input("Cantidad de notas"))

    notas=[]

    for i in range(cantidad):
        nota=leer_nota("Ingrese nota: ")
        notas.append(nota)
    
    alumnos[nombre]=notas  # Agregar al dicc los datos
    print("Alumno agregado correctamente!")
#2
def mostrar_alumnos(alumnos):
    if len(alumnos)==0:
        print("No hay alumnos registrados")
        return
    
    for nombre in alumnos:
        print(nombre,": ", alumnos[nombre])

#3
def ver_promedios(alumnos):
    if len(alumnos)==0:
        print("No hay alumnos registrados, no se pueden ver promedios")
        return
    
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])
        print(nombre,"tiene un Promedio de: ", round(promedio,1))


#4
def mejor_alumno(alumnos):
    if len(alumnos)==0:
        print("No hay alumnos registrados, no se pueden ver promedios")
        return
    
    mejor_promedio=0
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])
        
        if promedio > mejor_promedio:
            mejor_promedio=promedio
            mejor_alumno= nombre
    print("Mejor alumno: ", mejor_alumno)
    print("Promedio es: ", round(mejor_promedio,1))

#5
def cantidad_aprobados(alumnos):
    if len(alumnos)==0:
        print("No hay alumnos registrados, no se pueden ver aprobados")
        return
    
    for nombre in alumnos:
        promedio = sum(alumnos[nombre])/len(alumnos[nombre])

        if promedio>=4.0:
            aprobados= aprobados+1

    print("cantidad de aprobados es:  ", aprobados)
     