import calculos

# cuadrado
def cuadrado(tortuga, lado):
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)

def cuadrado_relleno(tortuga, lado, color):
    tortuga.fillcolor(color)
    tortuga.begin_fill()

    cuadrado(tortuga, lado)

    tortuga.end_fill()

# triangulo
def triangulo(tortuga, largo):
    tortuga.forward(largo)
    tortuga.left(120)
    tortuga.forward(largo)
    tortuga.left(120)
    tortuga.forward(largo)
    tortuga.left(120)

def triangulo_relleno(tortuga, lado, color):
    tortuga.fillcolor(color)
    tortuga.begin_fill()

    triangulo(tortuga, lado)

    tortuga.end_fill()

def hexagono(tortuga, largo, angulo):
    tortuga.forward(largo)
    tortuga.left(angulo)
    tortuga.forward(largo)
    tortuga.left(angulo)
    tortuga.forward(largo)
    tortuga.left(angulo)
    tortuga.forward(largo)
    tortuga.left(angulo)
    tortuga.forward(largo)
    tortuga.left(angulo)
    tortuga.forward(largo)
    tortuga.left(angulo)

#  POLIGONO
def poligono(figura, tortuga, largo):
    if figura == 'cuadrado':
        cuadrado(tortuga, largo)
    elif figura == 'triangulo':
        triangulo(tortuga, largo)
    elif figura == 'hexagono':
        angulo = calculos.angulo(figura)
        hexagono(tortuga, largo, angulo)
    else:
        print("Lo siento no tengo la figura en el catálogo")