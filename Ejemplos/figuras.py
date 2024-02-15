import turtle

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


ventana = turtle.Screen()

mbappe = turtle.Turtle()
mbappe.shape("turtle")
mbappe.color("red")
mbappe.speed(8)

# cuadrado
# largo = 70
# mbappe.forward(largo)
# mbappe.left(90)
# mbappe.forward(largo)
# mbappe.left(90)
# mbappe.forward(largo)
# mbappe.left(90)
# mbappe.forward(largo)

# largo = 150
# mbappe.forward(largo)
# mbappe.left(90)
# mbappe.forward(largo)
# mbappe.left(90)
# mbappe.forward(largo)
# mbappe.left(90)
# mbappe.forward(largo)

# cuadrado(mbappe, 75)

# mbappe.fillcolor("orange")
# mbappe.begin_fill()
# cuadrado(mbappe, 150) 
# mbappe.end_fill()

# mbappe.fillcolor("red")
# mbappe.begin_fill()
# cuadrado(mbappe, 250) 
# mbappe.end_fill()

# mbappe.up()
# mbappe.goto(-150,0)
# mbappe.down()
# cuadrado(mbappe, 150)

# mbappe.up()
# mbappe.goto(150,0)
# mbappe.down()
# cuadradoRelleno(mbappe, 100, "blue")

cuadradoRelleno(mbappe, 200, "blue")
cuadradoRelleno(mbappe, 50, "red")

# mbappe.circle(30)



ventana.exitonclick()
turtle.done()