from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from models import Persona
from utils import leer_personas, escribir_personas


app = FastAPI()
app.title = 'CRUD Python FastAPI'

# Archivos estaticos:
app.mount("/static", StaticFiles(directory="./public/static"), name="static")

@app.get('/', tags = ['principal'])
def principal():
    return FileResponse('./public/static/html/index.html')

@app.post('/personas', tags = ['personas'])
def agregar_persona(persona: Persona):
    personas = leer_personas()
    nueva_persona = persona.dict()
    personas.append(nueva_persona)
    escribir_personas(personas)
    return {'message': 'Persona agregada correctamente'}