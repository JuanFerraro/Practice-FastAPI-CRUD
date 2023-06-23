import json

# Funcion para leer el archivo json y retornar lista
def leer_personas():
    with open('personas.json', 'r') as file:
        personas = json.load(file) # Convierte json a lista
    return personas

# Funcion para escribir en el archivo json
def escribir_personas(personas: list):
    with open('personas.json', 'w') as file:
        json.dump(personas, file, indent=4)

# Funcion para buscar persona en el archivo json
def buscar_persona(personas: list, id: str):
    encontrado = next((persona for persona in personas if persona['id'] == id), None)
    if encontrado != None:
        return True
    else: 
        return False