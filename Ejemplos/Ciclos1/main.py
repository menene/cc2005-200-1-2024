import turtle
import dibujo
import calculos

ventana = turtle.Screen()
vamoacalmarno = turtle.Turtle()
vamoacalmarno.shape("turtle")
vamoacalmarno.color("red")
vamoacalmarno.speed(8)

# dibujo.poligono("cuadrado", vamoacalmarno, 100)
# vamoacalmarno.up()
# vamoacalmarno.goto(-200, -200)
# vamoacalmarno.down()
# dibujo.poligono("triangulo", vamoacalmarno, 100)
# dibujo.poligono("hexagono", vamoacalmarno, 100)
# dibujo.poligono("pentagono", vamoacalmarno, 150)
# dibujo.poligono("dodecagono", vamoacalmarno, 75)

opcion = "lo que sea"
while opcion != "salir":
    opcion = input("Ingrese la figura que quiere dibujar: ")

    if opcion == "cuadrado":
        dibujo.poligono(4, vamoacalmarno, 100)
    elif opcion == "triangulo":
        dibujo.poligono(3, vamoacalmarno, 100)
    elif opcion == "pentagono":
        dibujo.poligono(5, vamoacalmarno, 100)
    elif opcion == "hexagono":
        dibujo.poligono(6, vamoacalmarno, 100)
    elif opcion == "octagono":
        dibujo.poligono(8, vamoacalmarno, 100)
    elif opcion == 'salir':
        print("Feliz día 👋🏽")
        
        turtle.Terminator()
    else:
        print("figura no reconcida... intentalo nuevamente")