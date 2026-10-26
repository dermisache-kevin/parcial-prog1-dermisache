

def validar_cantidad():
    valido = False

    while not valido:
        cantidad = input("Ingrese la cantidad de alumnos (1 - 30): ")
        es_entero = True

        for i in range(len(cantidad)):
            if not ("0" <= cantidad[i] <= "9"):
                es_entero = False

        if es_entero and len(cantidad) > 0:
            cantidad = int(cantidad)

            if 1 <= cantidad <= 30:
                valido = True
            else:
                print("Error, ingrese una cantidad entre 1 y 30")
        else:
            print("Error, ingrese un número entero")

    return cantidad


def validar_nota(numero_parcial):
    valido = False

    while not valido:
        nota = input(f"Ingrese la nota del {numero_parcial} parcial (0 - 10): ")
        es_entero = True

        for i in range(len(nota)):
            if not ("0" <= nota[i] <= "9"):
                es_entero = False

        if es_entero and len(nota) > 0:
            nota = int(nota)

            if 0 <= nota <= 10:
                valido = True
            else:
                print("Error, ingrese una nota entre 0 - 10")
        else:
            print("Error, ingrese un número entero")

    return nota


def validar_nombre(alumnos):
    if len(alumnos) < 5:
        return False

    for i in range(len(alumnos)):
        caracter = alumnos[i]

        minuscula = "a" <= caracter <= "z"
        mayuscula = "A"<= caracter <= "Z"
        espacio = caracter == " "

        if not (minuscula or mayuscula or espacio):
            return False
        

    return True


def crear_lista(cantidad, valor_inicial):
    lista = [valor_inicial] * cantidad
    return lista


def cargar_datos(alumnos, nota1, nota2, cantidad):
    for i in range(cantidad):
        alumnos[i] = input("Ingrese el nombre del alumno: ")
        while not validar_nombre(alumnos[i]):
            print("Error, el nombre debe tener al menos 5 caracteres y solo letras y espacios")
            alumnos[i] = input("Ingrese el nombre del alumno: ")
        nota1[i] = validar_nota("primer")
        nota2[i] = validar_nota("segundo")


def mostrar_datos(alumnos, nota1, nota2, cantidad):
    for i in range(cantidad):
        print(f"El alumno {alumnos[i]} se saco un {nota1[i]} en el primer parcial y un {nota2[i]} en el segundo")

def main():
    cantidad =validar_cantidad()

    alumnos = crear_lista(cantidad, "")
    nota1 = crear_lista(cantidad, 0)
    nota2 = crear_lista(cantidad, 0)

    cargar_datos(alumnos, nota1, nota2, cantidad)
    #mostrar_datos(alumnos, nota1, nota2, cantidad)

    return alumnos, nota1, nota2, cantidad

