# diccionario = {"codigo": "cc2005", "nombre": "Algoritmos", "creditos": 6}
# print(diccionario)
# print(diccionario["codigo"])

# lista = ["cc2005", "Algoritmos", 6]
# print(lista)
# print(lista[0])

diccionario = {"codigo": "cc2005", "nombre": "Algoritmos", "creditos": 6}
print(diccionario)
diccionario["creditos"] = 4
print(diccionario)
diccionario["catedratico"] = "Erick Marroquin"
diccionario["seccion"] = 60
print(diccionario)
del diccionario["seccion"]
print(diccionario)
# print(diccionario["hola"])
# print(diccionario.get("hola"))
print(diccionario.get("hola", "No existe... :("))

# print("CLAVES:", diccionario.keys())
# print("VALORES:", diccionario.values())

print("CLAVES:", list(diccionario.keys()))
print("VALORES:", list(diccionario.values()))