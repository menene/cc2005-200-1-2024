#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 60
# 
# Erick Marroquin - 123456
# Ejercicio Individual 4 - Main
# 06/03/24
#==========================================================

# importar el modulo
import modulo

# variable de control
opcion = "algo"
while opcion != "salir":
    # pedirle al usuario un numero o salir
    opcion = input("Ingrese un número o salir para terminar: ")

    if opcion == "salir":
        # si es salir solo le pongo adios
        print("Adios")
    else:
        # si no es salir convierto a int y llamo a mi funcion
        num = int(opcion)
        modulo.tabla(num)