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

def promedio(notas):
    n = len(notas)
    suma = 0
    for nota in notas:
        suma += nota
    
    return (suma / n)

estudiantes = []

opcion = ""
while opcion != "6":
    print("\n=== NOTAS++ ===\n")
    print("1. Agregar estudiante")
    print("2. Agregar nota")
    print("3. Promedio estudiante")
    print("4. Promedio general")
    print("5. Listar estudiantes")
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
        print(estudiantes)
    elif opcion == "6":
        print("Adiós")
    else:
        print("opcion invalida")
