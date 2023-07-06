# FastAPI
from fastapi import FastAPI, Form, Query, Request, HTTPException, Depends
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
def lista_personas(request: Request):
    personas = leer_personas()
    if personas:
        return templates.TemplateResponse("index.html", {"request": request, "personas": personas})
    else:
        error = "No hay personas registradas."
        return templates.TemplateResponse("index.html", {"request": request, "error": error})

# POST: Ruta para agregar persona 
@app.post('/personas', tags = ['personas'])
def agregar_persona(request: Request, persona: Persona = Depends(Persona.as_form)):
    personas = leer_personas()
    nueva_persona = persona.dict()
    for persona in personas:
        if persona['id'] == nueva_persona['id']:
            error = 'Persona ya registrada! verifica el ID'
            return templates.TemplateResponse("index.html", {"request": request, "error": error})
    personas.append(nueva_persona)
    escribir_personas(personas) #Escribo en el archivo la nueva lista
    message = "Persona agregada correctamente."
    return templates.TemplateResponse("index.html", {"request": request, "message": message})
    
# GET: Buscar persona por id
@app.get('/personas/{id}', tags=['personas'])
def busqueda_persona(id: str):
    personas = leer_personas()
    persona = buscar_persona(personas, id)
    if persona == False:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    else:
        return JSONResponse(content=persona)

# Edit route
@app.get('/personas/edit/{id}', tags=['personas'])
def edit_person(request: Request, id: str):
    personas = leer_personas()
    for person in personas:
        if id == person['id']:
            edit_person = person
    return templates.TemplateResponse("index.html", {"request": request, "edit_person": edit_person})

# PUT: Actualizar persona por id (changed to post)
@app.post('/personas/update/', tags=['personas'])
def actualizar_persona(request: Request, persona: Persona = Depends(Persona.as_form)):
    personas = leer_personas()
    update_persona = persona.dict()
    for persona in personas:
        if persona['id'] == update_persona['id'] :
            persona['nombre'] = update_persona['nombre']          
            persona['apellido'] = update_persona['apellido']          
            persona['id'] = update_persona['id']          
            persona['edad'] = update_persona['edad']          
            persona['estudios'] = update_persona['estudios']          
            persona['puntaje'] = update_persona['puntaje']   
            escribir_personas(personas) #Escribo en el archivo la lista actualizada
            message = "Persona actualizada correctamente."
            return templates.TemplateResponse("index.html", {"request": request, "message": message})
    return HTTPException(status_code=404, detail='Persona no encontrada')

# DELETE: Eliminar persona por id (changed to get)
@app.get('/personas/delete/{id}', tags=['personas'])
def eliminar_persona(request: Request,id):
    personas = leer_personas()
    for persona in personas:
        if persona['id'] == id:
            personas.remove(persona)
            escribir_personas(personas) #Escribo en el archivo la lista actualizada
            message = "Persona eliminada correctamente."
            return templates.TemplateResponse("index.html", {"request": request, "message": message})
    return HTTPException(status_code=404, detail='Persona no encontrada')
    

