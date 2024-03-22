# c1 = "Hola"
# c2 = "Mundo"

# print(c1+c2)
# print(c1)
# print(c2)

# c1 = "HoLa MuNdO"
# largo = len(c1)
# print(largo)
# print("La cadena es solo texto:", c1.isalpha())
# print("La cadena es numerica:", c1.isdigit())

# opcion = input("Ingrede un número entero")
# if not opcion.isdigit():
#     print("Por favor ingrese un numero")
# else:
#     print("Gracias por seguir instrucciones")

# opcion = "a"
# while not opcion.isdigit():
#     opcion = input("Ingrede un número entero: ")

# c1 = "HoLa MuNdO"
# print(c1.lower())
# print(c1.upper())
# print(c1.title())
# print(c1)

# opcion = input("Ingrese 'salir' para terminar: ")
# opcion = opcion.lower()

# if opcion.lower() == "salir":
#     print("saliendo...")
# else:
#     print("no saliendo...")

c1 = "hola mundo!"
# print(c1.count("o"))
# print(c1.replace("a", "@"))
# print(c1)
# print(c1.find("h"))
# print(c1.find("H"))
# print(c1.find("o"))
# print(c1.rfind("o"))
# print("h" in c1)
# print("H" in c1)

# print(c1[0])
# print(c1[1])
# print(c1[len(c1) - 1])
# print(c1[-1], c1[0])

# for letra in c1:
#     print(letra)

indice = 0
while indice < len(c1):
    print(c1[indice])
    indice += 1