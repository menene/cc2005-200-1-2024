# LEER UN TXT COMPLETO
archivo = open("file.txt", "r", encoding="utf8")
contenido = archivo.read()
print(contenido)
archivo.close()

# LEER UN TXT LINEA POR LINEA
# filename = "file.txt"
# filename = "shrek.txt"
# with open(filename) as file_object:
#     for line in file_object:
#         if line.rstrip() != "":
#             print(line.rstrip())
        # print(line)
        # print(line.rstrip())

# ESCRIBIR A UN ARCHIVO DE TEXTO
# archivo = open("nombre.txt", "w", encoding="utf8")
# archivo.write("Este conetenido se va a escribir en el archivo.")
# archivo.close()

# archivo = open("mensaje.txt", "w", encoding="utf8")
# for i in range(10000):
#     archivo.write("Te odio dembele\n")
# archivo.close()