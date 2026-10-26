def invertir_nombre(nombre):
    """
    Invertir el orden de los caracteres de un nombre.

    Args:
        nombre (str): Nombre que se desea invertir.

    Returns:
        str: Nombre con los caracteres en orden inverso.
    """
    return nombre[::-1]


def contar_vocales(alumno):
    """
    Contar la cantidad de vocales que contiene un nombre.

    Args:
        alumno (str): Nombre del alumno en el que se contarán las vocales.

    Returns:
        int: Cantidad de vocales encontradas en el nombre.
    """
    vocales = "aeiou"
    contador = 0

    for i in range(len(alumno)):
        es_vocalo = False

        for j in range(len(vocales)):
            if alumno[i] == vocales[j]:
                contador += 1
    return contador


def sacar_promedio(nota1, nota2, cantidad):
    """
    Calcular el promedio de dos notas para cada alumno.

    Args:
        nota1 (list): Lista con las primeras notas de los alumnos.
        nota2 (list): Lista con las segundas notas de los alumnos.
        cantidad (int): Cantidad de alumnos cuyas notas se promediarán.

    Returns:
        list: Lista con los promedios de cada alumno.
    """
    promedio = [0] * cantidad
    for i in range(cantidad):
        promedio[i] = (nota1[i] + nota2[i]) /2
    return promedio


def mostrar_promedio(alumnos, nota1, nota2, cantidad, promedio):
    """
    Mostrar por pantalla el promedio de cada alumno.

    Args:
        alumnos (list): Lista con los nombres de los alumnos.
        nota1 (list): Lista con las primeras notas de los alumnos.
        nota2 (list): Lista con las segundas notas de los alumnos.
        cantidad (int): Cantidad de alumnos cuyos promedios se mostrarán.
        promedio (list): Lista con los promedios de cada alumno.
    """
    for i in range(cantidad):
        print(f"El promedio del alumno {alumnos[i]} es: {promedio[i]}")


def buscar_alumno(alumnos, nota1, nota2, cantidad, promedio):
    """
    Buscar un alumno por su nombre y mostrar sus notas y promedio.

    Args:
        alumnos (list): Lista con los nombres de los alumnos.
        nota1 (list): Lista con las notas del primer parcial de los alumnos.
        nota2 (list): Lista con las notas del segundo parcial de los alumnos.
        cantidad (int): Cantidad de alumnos registrados.
        promedio (list): Lista con los promedios de los alumnos.
    """
    alumno_buscado = input("Ingrese el nombre del alumno a buscar: ")
    alumno_encontrado = False
    for i in range(cantidad):
        if alumno_buscado == alumnos[i]:
            alumno_encontrado = True
            print(f""" 
        El alumno {alumnos[i]} se saco un {nota1[i]} en el primer parcial y un {nota2[i]} en el segundo,
        y tiene un promedio de {promedio[i]}""")
    if not alumno_encontrado:
        print(f"El alumno buscado no existe")