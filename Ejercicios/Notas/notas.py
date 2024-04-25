# ==========================================
# Universidad del valle de Guatemala
# CC2005 - Algoritmos y Programacion Basica
# 60
#
# Erick Marroquin
#
# 05/04/24
#
# PROGRAMA QUE LLEVA REGISTRO DE NOTAS
# ==========================================

import csv

def promedio(notas):
    n = len(notas)
    suma = 0
    for nota in notas:
        suma += nota
    
    return (suma / n)

seccion = input("Ingrese la sección que quiere trabajar: ")

if seccion == "60":
    filename = "Estudiantes-60.csv"
elif seccion == "70":
    filename = "Estudiantes-70.csv"
else:
    filename = ""

estudiantes = []
if filename != "":
    with open(filename, mode="r") as archivo:
        lineas = csv.DictReader(archivo)

        for linea in lineas:
            estudiante = {
                "carnet": linea["Carnet"],
                "nombre": linea["Nombre"],
                "notas": []
            }

            estudiantes.append(estudiante)

    print("Archivo importado exitosamente...")
else:
    print("Archivo no encotrado, no se importan datos...")

opcion = ""
while opcion != "6":
    print("\n=== NOTAS++ ===\n")
    print("1. Agregar estudiante")
    print("2. Agregar nota")
    print("3. Promedio estudiante")
    print("4. Promedio general")
    print("5. Listar estudiantes")
    print("5.5. Eliminar estudiante")
    print("6. Salir\n")

    opcion = input("Seleccione una de las opciones anteriores: ")

    if opcion == "1":
        carnet = input("Ingrese el carnet: ")
        nombre = input("Ingrese el nombre: ")
        notas = []

        estudiante = {"carnet": carnet, "nombre": nombre, "notas": notas}
        
        estudiantes.append(estudiante)

    elif opcion == "2":
        carnet = input("Ingrese el número de carnet: ")
        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                nota = int(input("Ingrese la nota: "))
                estudiante["notas"].append(nota)

    elif opcion == "3":
        carnet = input("Ingrese el número de carnet: ")
        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                x = promedio(estudiante["notas"])
                print("El promedio de", estudiante["nombre"], "(", estudiante["carnet"], ") es de:", x)

    elif opcion == "4":
        print("promedio general")
        
    elif opcion == "5":
        for estudiante in estudiantes:
            print(estudiante)

    elif opcion == "5.5":
        carnet = input("Ingrese el número de carnet: ")

        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                estudiantes.remove(estudiante)

    elif opcion == "6":
        print("Adiós")

    else:
        print("opcion invalida")

with open(filename, mode="w") as archivo:
    columnas = ["Carnet", "Nombre"]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)

    escritor.writeheader()

    for estudiante in estudiantes:
        escritor.writerow({
            "Carnet": estudiante["carnet"],
            "Nombre": estudiante["nombre"]
        })