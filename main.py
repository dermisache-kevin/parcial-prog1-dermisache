cantidad = 0
alumnos = ""
nota1 = 0
nota2 = 0
promedio = 0
menu = False


while not menu:
    print(f"""Bienvenido al MENÚ
    (1) Cargar alumnos
    (2) Mostrar Listado
    (3) Mostrar estadisticas
    (4) Ver ranking (ordenado)
    (5) Buscar alumno
    (6) Juegos con un nombre
    (0) Salir
        """)
    
    opcion = (input("Ingrese el numero de la tarea a realizar: "))

    match opcion:
        case "1":
            from validaciones import main
            alumnos, nota1, nota2, cantidad = main()
            from procesamiento import sacar_promedio
            promedio = sacar_promedio(nota1, nota2, cantidad)
        case "2":
            from validaciones import mostrar_datos
            mostrar_datos(alumnos, nota1, nota2, cantidad)
            from procesamiento import mostrar_promedio
            mostrar_promedio(alumnos, nota1, nota2, cantidad, promedio)
        case "3":
            pass
        case "4":
            pass
        case "5":
            from procesamiento import buscar_alumno
            buscar_alumno(alumnos, nota1, nota2, cantidad, promedio)
        case "6":
            from procesamiento import invertir_nombre, contar_vocales
            nombre_alumno = input("Ingrese el nombre del alumno/a para el juego: ")
            nombre_invertido = invertir_nombre(nombre_alumno)
            vocales = contar_vocales(nombre_alumno)
            print(f"El nombre elegido fue:{nombre_alumno}, tiene {vocales} vocales, y el nombre al reves es: {nombre_invertido}")
        case "0":
            print("Saliendo del programa")
            menu = True
            pass
        case _:
            print("La opcion elegida no existe!")