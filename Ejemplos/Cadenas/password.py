password = input("Ingrese un password: ")

nota = 0

permitidos = ".,;:+-"

mayusculas = 0
minusculas = 0
numeros = 0
simbolos = 0
for letra in password:
    if letra.isupper():
        mayusculas += 1
    elif letra.islower():
        minusculas += 1

    if letra.isdigit():
        numeros += 1

    if letra in permitidos:
        simbolos += 1

if mayusculas > 0 and minusculas > 0:
    print("\nContine mayusculas y minusculas +10")
    nota += 10

if numeros != 0:
    print("Contine números +10")
    nota += 10

if len(password) >= 10:
    print("Al menos 10 caracteres +5")
    nota += 5

if simbolos != 0:
    print("Al menos 1 símbolo +5")
    nota += 5

if password.count(" ") > 0:
    print("Contiene espacios -5")
    nota -= 5

if "password" in password.lower():
    print("Contiene la palabra 'password' -50")
    nota -= 50

print("\nLa calificación es:", nota)