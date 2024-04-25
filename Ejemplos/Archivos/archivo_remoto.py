import requests

url = "http://62.138.24.147/pruebas.txt"

r = requests.get(url)

print(r.text)