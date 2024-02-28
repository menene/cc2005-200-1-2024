import math

# cuadrado
# def perimetro_cuadrado(largo):
#     return (largo * 4)

# def area_cuadrado(largo):
#     return (largo * largo)

# triangulo
# def perimetro_triangulo(largo):
#     return (largo * 3)

# def area_triangulo(largo):
#     b = (largo / 2)
#     h = math.sqrt(largo ** 2 -  b ** 2)
#     area = (b * h) / 2

#     return area

# def lados(figura):    
#     if figura == 'cuadrado':
#         lados = 4
#     elif figura == 'triangulo':
#         lados = 3
#     elif figura == 'hexagono':
#         lados = 6
#     else:
#         lados = 0

#     return lados

def angulo(lados):
    if lados == 0:
        a = 0
    else:
        a = 360 / lados

    return a

# def perimetro(figura, largo):
#     l = lados(figura)
#     perimetro = (l * largo)

#     return perimetro

# def area_hexagono(figura, largo):
#     l = lados(figura)
#     angulo = (360 / (2 * l)) 
#     apotema = (largo / (2 * math.tan(angulo)))
#     p = perimetro(figura, largo)

#     area = (p * apotema) / 2

#     if area < 0:
#         area = area * -1

#     return area