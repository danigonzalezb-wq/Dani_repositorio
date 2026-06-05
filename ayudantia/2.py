def pedir_opcion():
    print(""" 
A._ Agregar Contacto
B._ Buscar
S._ Salir """)
    
while True:
   pedir_opcion()
   try:
        op=input("Ingrese su opcion: ")
        break
   except:
        print("Opcion invalida")
    
  #  if op=="A":
    #   print
   # else:
     #  print
       