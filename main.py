from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Persona
from utils import leer_personas, escribir_personas, buscar_persona

app = FastAPI()
app.title = 'CRUD Python FastAPI'

# Archivos estaticos:
app.mount("/static", StaticFiles(directory="./public/static"), name="static")
templates = Jinja2Templates(directory="./public/templates")

# GET: Ruta Main
@app.get('/', tags = ['principal'])
def principal(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# POST: Ruta para agregar persona 
@app.post('/personas', tags = ['personas'])
def agregar_persona(persona: Persona):
    personas = leer_personas()
    nueva_persona = persona.dict()
    for persona in personas:
        if persona['id'] == nueva_persona['id']:
            return HTTPException(status_code=400, detail="Persona ya existente")
    personas.append(nueva_persona)
    escribir_personas(personas) #Escribo en el archivo la nueva lista
    return JSONResponse(content='Persona agregada correctamente', status_code=201)

# GET: Buscar persona por id
@app.get('/personas/{id}', tags=['personas'])
def busqueda_persona(id: str):
    personas = leer_personas()
    persona = buscar_persona(personas, id)
    if persona == False:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    else:
        return JSONResponse(content=persona)


