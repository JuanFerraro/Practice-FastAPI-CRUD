from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import Persona
from utils import leer_personas, escribir_personas

app = FastAPI()
app.title = 'CRUD Python FastAPI'

@app.get('/', tags = ['principal'])
def principal():
    return HTMLResponse('<h1>CRUD Python FastAPI</h1>')

@app.post('/personas', tags = ['personas'])
def agregar_persona(persona: Persona):
    personas = leer_personas()
    nueva_persona = persona.dict()
    personas.append(nueva_persona)
    escribir_personas(personas)
    return {'message': 'Persona agregada correctamente'}