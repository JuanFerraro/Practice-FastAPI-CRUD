import json

# Funcion para leer el archivo json y retornar lista
def leer_personas():
    with open('personas.json', 'r') as file:
        personas = json.load(file)
    return personas

# Funcion para escribir en el archivo json
def escribir_personas(personas):
    with open('personas.json', 'w') as file:
        json.dump(personas, file, indent=4)