import json

with open("Libros.json","r") as file:
    result = json.load(file)
    print(result)