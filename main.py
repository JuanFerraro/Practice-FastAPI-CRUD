from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from models import Persona
from utils import leer_personas, escribir_personas, buscar_persona


app = FastAPI()
app.title = 'CRUD Python FastAPI'

# Archivos estaticos:
app.mount("/static", StaticFiles(directory="./public/static"), name="static")

# GET: Ruta Main
@app.get('/', tags = ['principal'])
def principal():
    return FileResponse('./public/static/html/index.html')

# POST: Ruta para agregar persona 
@app.post('/personas', tags = ['personas'])
def agregar_persona(persona: Persona):
    personas = leer_personas()
    nueva_persona = persona.dict()
    personas.append(nueva_persona)
    escribir_personas(personas)
    return {'message': 'Persona agregada correctamente'}

# GET: Buscar persona
@app.get('/personas/busqueda', tags=['personas'])
def busqueda_persona(id):
    print('=> ',id)
    personas = leer_personas()
    busqueda = buscar_persona(personas, id)
    if busqueda == False:
        print('No Encontrado')
        return {'message': '404 Persona no encontrada'}
    else:
        print('Encontrao')
        return {'message': 'Persona encontrada'}
