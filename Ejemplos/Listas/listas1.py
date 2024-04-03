# lista = [1, 2, 3, 4, 5, 6]
# print(lista)

# heterogenea = [1, "a", 3.14, True]
# print(heterogenea)

# lista = [2, 2, 3, 4, 5, 6]
# lista2 = [9, 8, 7]

# print(lista + lista2)
# print(lista * 3)

# print(lista)
# lista[0] = 1
# print(lista)

# sub_lista = lista[0:4]
# sub_lista = lista[0:4:2]
# sub_lista = lista[4:]
# sub_lista = lista[:4]
# print("Original:", lista)
# print("Slice:", sub_lista)

# notas = [99, 98, 97, 97, 96, 84, 80, 61]
# # notas[0] = 100
# # notas[1] = 100
# # notas[2] = 100
# notas[0:3] = [100, 100, 100]
# print(notas)

# lista_super = ["Pan", "Frijol", "Huevo", "Queso"]
# print("Original:", lista_super)
# lista_super.append("Ketchup")
# print("Alrterada:", lista_super)
# lista_super.insert(1, "Champurradas")
# print("Alrterada con insert:", lista_super)
# # lista_super.remove("Cerveza")
# del lista_super[0]
# print("Alrterada con delete:", lista_super)
# valor = lista_super.pop()
# print("Alrterada con pop:", lista_super)
# print(valor)
# lista_super.clear()
# print("Alrterada con clear:", lista_super)

# notas = [78, 34, 22, 99, 90, 65,98, 97, 97, 96, 84, 80, 61]
# # notas.sort()
# notas.sort(reverse=True)

# print(notas)

# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [7, 8 ,9]

# lista1.append(lista2)
# print(lista1)
# print(lista1[6])
# print(lista1[6][0])

cadena = "Hello World"
nueva_lista = cadena.split(" ")
print(nueva_lista)

nuevo_string = "-".join(nueva_lista)
print(nuevo_string)