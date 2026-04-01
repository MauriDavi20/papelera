n = 60
opcion = None
lista = []
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
      eleccion = "si"
      while eleccion == "si":
          nombre = input("Ingrese su nombre: ")
          datos = {"Nombre":nombre}
          lista.append(datos)
          print(f"Su nombre es: {nombre}")
          eleccion = input("Desea seguir registrando? (si/no): ").lower()
      input("ingrese ENTER para volver al menu: ")
      
      
 elif opcion == 2:
     print("="*n)
     print("ELIMINAR DATOS".center(n))
     print("="*n)
     nombre = input("Ingrese su nombre: ")
     for datos in lista:
          if datos['Nombre'] == nombre:
               lista.remove(datos)
               print(f"El nombre: {datos['Nombre']} fue eliminado")
          else:
               print("Ese nombre no se encuentra registrado")
     input("ingrese ENTER para volver al menu: ")
     
     
 elif opcion == 3:
      print("="*n)
      print("BUSCAR DATOS".center(n))
      print("="*n)
      nombre = input("Ingrese su nombre: ")
      
      for datos in lista:
          if datos['Nombre'] == nombre:
             print(f"El nombre: {datos['Nombre']} se encuentra registrado") 
             break
      else:
          print("Este nombre no se encuentra")  
          
      input("ingrese ENTER para volver al menu: ")

 else:
    print("solo opcion entre 1 y 4")
    