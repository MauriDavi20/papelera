n = 60
opcion = None
while opcion != 4:
 print("="*n)
 print("PAPELERA".center(n))
 print("="*n)

 print("1. Añadir datos")
 print("2. Eliminar datos")
 print("3. Buscar datos")
 print("4. salir")
 opcion = int(input("Que quieres hacer hoy?: "))

    
 if opcion == 1:
      print("="*n)
      print("AÑADIR DATOS".center(n))
      print("="*n)
      
      nombre = input("Ingrese su nombre: ")
      print(f"Su nombre es")
      input("ingrese ENTER para volver al menu: ")
 elif opcion == 2:
     print("="*n)
     print("ELIMINAR DATOS".center(n))
     print("="*n)
     nombre = input("Ingrese su nombre: ")
     input("ingrese ENTER para volver al menu: ")
 elif opcion == 3:
      print("="*n)
      print("BUSCAR DATOS".center(n))
      print("="*n)
      nombre = input("Ingrese su nombre: ")
      input("ingrese ENTER para volver al menu: ")
 else:
    print("solo opcion entre 1 y 4")
    