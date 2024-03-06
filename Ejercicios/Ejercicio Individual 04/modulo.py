#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 60
# 
# Erick Marroquin - 123456
# Ejercicio Individual 4 - Modulo
# 06/03/24
#==========================================================

# funcion que recibe un numero
# y imprime una tabla de ese
# numero del 1 al 10
def tabla(num):
    # se usa 11 ya que necesito generar una lista
    # de 1 a 10 y el ultimo valor
    # no se incluye
    for i in range(1, 11):
        # calculo el total
        total = num * i

        # imprimo la tabla
        print(num, "x", i, "=", total)