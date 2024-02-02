#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 60
# 
# Erick Marroquin - 123456
# Solicion del ejercicio individual 1 - Pitagoras
# 31/01/24
#==========================================================

import math

modo = input("¿Conoces el valor de la hipotenusa? ")

if modo != "si":
    a = int(input("Ingese el valor de A: "))
    b = input("Ingese el valor de B: ")
    b = int(b)

    c = math.sqrt((a * a) + (b * b))

    print("El valor de la hipotenusa es:", c)
else:
    c = int(input("Ingese el valor de la hipotenusa: "))
    b = input("Ingese el valor de B: ")
    b = int(b)

    if b >= c:
        print("Imposible de calcular ya que el cateto es mayor a la hipotenusa.")
    else:
        a = math.sqrt((c * c) - (b * b))

        print("El valor del cateto A es:", a)