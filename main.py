# FastAPI
from fastapi import FastAPI, Form, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Models
from models import Persona

# Utils
from utils import leer_personas, escribir_personas, buscar_persona

app = FastAPI()
app.title = 'CRUD Python FastAPI'
app.version = '1.0'

# Archivos estaticos:
app.mount("/static", StaticFiles(directory="./public/static"), name="static")
templates = Jinja2Templates(directory="./public/templates")

# GET: Ruta Main
@app.get('/', tags = ['principal'])
def principal(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# GET: Mostrar todas las personas
@app.get('/personas', tags = ['personas'])
def lista_personas():
    personas = leer_personas()
    if personas != False:
        return JSONResponse(content=personas, status_code=200)
    else:
        raise HTTPException(status_code=401, detail="No hay personas")

# POST: Ruta para agregar persona 
@app.post('/personas', tags = ['personas'])
def agregar_persona(persona: Persona = Depends(Persona.as_form)):
    print(persona)
    print(type(persona))
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

# PUT: Actualizar persona por id
@app.put('/personas/{id}', tags=['personas'])
def actualizar_persona(id: str, persona: Persona):
    personas = leer_personas()
    update_persona = persona.dict()
    for persona in personas:
        if persona['id'] == update_persona['id']:
            persona['nombre'] = update_persona['nombre']          
            persona['apellido'] = update_persona['apellido']          
            persona['id'] = update_persona['id']          
            persona['edad'] = update_persona['edad']          
            persona['estudios'] = update_persona['estudios']          
            persona['puntaje'] = update_persona['puntaje']   
            escribir_personas(personas) #Escribo en el archivo la lista actualizada
            return JSONResponse(status_code=200, content='Persona actualizada')       
    return HTTPException(status_code=404, detail='Persona no encontrada')

# DELETE: Eliminar persona por id
@app.delete('/personas/{id}', tags=['personas'])
def eliminar_persona(id):
    personas = leer_personas()
    for persona in personas:
        if persona['id'] == id:
            personas.remove(persona)
            escribir_personas(personas) #Escribo en el archivo la lista actualizada
            return JSONResponse(status_code=200, content='Persona eliminada correctamente')
    return HTTPException(status_code=404, detail='Persona no encontrada')
    

