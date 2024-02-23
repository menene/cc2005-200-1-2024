import turtle
import dibujo
import calculos

ventana = turtle.Screen()
vamoacalmarno = turtle.Turtle()
vamoacalmarno.shape("turtle")
vamoacalmarno.color("red")
vamoacalmarno.speed(8)

largo = 150
# dibujo.triangulo_relleno(vamoacalmarno, largo, "blue")
# perimetro = calculos.perimetro_triangulo(largo)
# area = calculos.area_triangulo(largo)

# print("El perimetro es:", perimetro)
# print("El área es:", area)
figura = input("Ingrese la figura a dibujar: ")

dibujo.poligono(figura, vamoacalmarno, largo)

perimetro = calculos.perimetro(figura, largo)
area = calculos.area_hexagono(figura, largo)

print("El perimetro es:", perimetro)
print("El área es:", area)

ventana.exitonclick()
vamoacalmarno.end()