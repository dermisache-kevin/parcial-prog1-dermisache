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
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "0":
            print("Saliendo del programa")
            menu = True
            pass
        case _:
            print("La opcion elegida no existe!")