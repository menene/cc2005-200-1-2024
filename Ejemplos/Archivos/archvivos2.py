import csv

with open("Estudiantes-60.csv", mode="r") as archivo:
    lineas = csv.DictReader(archivo)
        
    for linea in lineas:
        print(linea)