import turtle

ventana = turtle.Screen()

mbappe = turtle.Turtle()

mbappe.forward(100)
mbappe.right(45)
mbappe.backward(250)
mbappe.left(90)
mbappe.forward(50)

mbappe.up()
mbappe.goto(200, 250)
mbappe.down()

# mbappe.clear()
# mbappe.reset()

mbappe.pensize(10)

mbappe.home()

pos = mbappe.position()
print(pos)


ventana.exitonclick()
turtle.done()