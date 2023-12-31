# Pydantic
from pydantic import BaseModel, Field

# FastAPI
from fastapi import Form

# Schema del modelo Persona
class Persona(BaseModel):
    nombre: str = Field(min_lenght = 3, max_length = 25)
    apellido: str = Field(min_lenght = 3, max_length = 25)
    id: str = Field(min_lenght = 7, max_length = 10)
    edad: int = Field(gt = 15, lt = 99)
    estudios: str = Field(min_lenght = 7, max_length = 50)
    puntaje: float = Field(ge = 0, le = 10)

    @classmethod
    def as_form(
        cls,
        nombre: str = Form(),
        apellido: str = Form(),
        id: str = Form(),
        edad: int = Form(),
        estudios: str = Form(),
        puntaje: float = Form()
    ):
        return cls(
            nombre = nombre,
            apellido = apellido,
            id = id,
            edad = edad,
            estudios = estudios,
            puntaje = puntaje
        )

    class Config:
        schema_extra = {
            'example': {
                "nombre": "Juan",
                "apellido": 'Mendoza',
                'id': '10203040',
                'edad': 21,
                'estudios': 'Arquitecto de software',
                'puntaje': 7.2
            }
        }