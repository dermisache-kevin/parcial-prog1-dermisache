def invertir_nombre(nombre):
    return nombre[::-1]


def contar_vocales(alumno):
    vocales = "aeiou"
    contador = 0

    for i in range(len(alumno)):
        es_vocalo = False

        for j in range(len(vocales)):
            if alumno[i] == vocales[j]:
                contador += 1
    return contador


def sacar_promedio(nota1, nota2, cantidad):
    promedio = [0] * cantidad
    for i in range(cantidad):
        promedio[i] = (nota1[i] + nota2[i]) /2
    return promedio


def mostrar_promedio(alumnos, nota1, nota2, cantidad, promedio):
    for i in range(cantidad):
        print(f"El promedio del alumno {alumnos[i]} es: {promedio[i]}")


def buscar_alumno(alumnos, nota1, nota2, cantidad, promedio):
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