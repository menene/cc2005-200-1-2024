#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 60
# 
# Erick Marroquin - 123456
# Condicionales simples
# 31/01/24
#==========================================================

dia = 6
hora = 8.25

ir_clase = (dia == 3 or dia == 5) and (hora >= 7 and hora <= 8.5)

if ir_clase:
    print("Voy a clase")
else:
    print("Me salve")