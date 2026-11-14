from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app import servicios

app = FastAPI()
plantillas = Jinja2Templates(directory="app/templates")


class SolicitudRespuesta(BaseModel):
    id: int
    opcion: int = Field(ge=0, le=3)


@app.get("/")
def pagina_principal(request: Request):
    return plantillas.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.get("/api/preguntas")
def obtener_preguntas():
    return servicios.listar_preguntas()


@app.post("/api/responder")
def responder(solicitud: SolicitudRespuesta):
    resultado = servicios.responder(solicitud.id, solicitud.opcion)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    correcta, respuesta_correcta = resultado
    return {
        "correcta": correcta,
        "respuesta_correcta": respuesta_correcta,
    }
