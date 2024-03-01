import calculos

#  POLIGONO
# def poligono(lados, tortuga, largo):
#     angulo = calculos.angulo(lados)

#     x = 1
#     while x <= lados:
#         tortuga.forward(largo)
#         tortuga.left(angulo)

#         x = x + 1

def poligono(lados, tortuga, largo):
    angulo = calculos.angulo(lados)
    
    for i in range(lados):
        tortuga.forward(largo)
        tortuga.left(angulo)