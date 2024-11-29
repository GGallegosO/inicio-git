opcion = ""

while opcion != 6:

    print("\n","Bienvenido, las opciones son: ")
    print("\n","1. Crear un libro")
    print("2. Actualizar un libro")
    print("3. Eliminar un libro")
    print("4. Consultar un libro")
    print("5. Mostrar todo el inventario")
    print("6. Terminar")


    opcion = int(input("\nIngresa una opción que quieras hacer: "))


    if opcion == 1:
        print("Vamos a crear")
    elif opcion == 2:
        print("Vamos a actualziar")
    elif opcion == 3:
        print("Vamos a eliminar")
    elif opcion == 4:
        print("Vamos a consultar")
    elif opcion == 5:
        print("Vamos a mostrar")
    else:
        print("Ingrese una opción válida")