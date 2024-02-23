def cuadrado(tortuga, lado):
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)

def cuadradoRelleno(tortuga, lado, color):
    tortuga.fillcolor(color)
    tortuga.begin_fill()

    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)
    tortuga.forward(lado)
    tortuga.left(90)

    tortuga.end_fill()