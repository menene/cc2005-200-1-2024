import turtle
# from misfiguras import cuadrado
from misfiguras import *

ventana = turtle.Screen()

mbappe = turtle.Turtle()
mbappe.shape("turtle")
mbappe.color("red")
mbappe.speed(8)


figura = input("Ingrese la figura que desea dibujar: ")
if figura == 'cuadrado':
    largo = int(input("Ingrese el largo: "))
    pintado = input("Lo quieres relleno? (si|no): ")
    if pintado == 'si':
        color = input("Ingrese el color: ")
        cuadradoRelleno(mbappe, largo, color)
    else:
        cuadrado(mbappe, largo)
else:
    print("No tengo esa figura en el catálogo")



ventana.exitonclick()
turtle.Terminator()