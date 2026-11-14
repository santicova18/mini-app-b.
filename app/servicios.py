from typing import TypedDict


class PreguntaPublica(TypedDict):
    id: int
    texto: str
    opciones: list[str]


class Pregunta(PreguntaPublica):
    respuesta_correcta: int


_PREGUNTAS: list[Pregunta] = [
    {
        "id": 1,
        "texto": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Marte", "Júpiter", "Saturno", "Venus"],
        "respuesta_correcta": 1,
    },
    {
        "id": 2,
        "texto": "¿Cuál es la capital de Japón?",
        "opciones": ["Kioto", "Osaka", "Tokio", "Nagoya"],
        "respuesta_correcta": 2,
    },
    {
        "id": 3,
        "texto": "¿Quién pintó la Mona Lisa?",
        "opciones": [
            "Vincent van Gogh",
            "Pablo Picasso",
            "Claude Monet",
            "Leonardo da Vinci",
        ],
        "respuesta_correcta": 3,
    },
    {
        "id": 4,
        "texto": "¿Cuál es el océano más extenso de la Tierra?",
        "opciones": [
            "Océano Atlántico",
            "Océano Índico",
            "Océano Pacífico",
            "Océano Ártico",
        ],
        "respuesta_correcta": 2,
    },
    {
        "id": 5,
        "texto": "¿Qué gas absorben principalmente las plantas durante la fotosíntesis?",
        "opciones": ["Oxígeno", "Nitrógeno", "Hidrógeno", "Dióxido de carbono"],
        "respuesta_correcta": 3,
    },
]


def listar_preguntas() -> list[PreguntaPublica]:
    return [
        {
            "id": pregunta["id"],
            "texto": pregunta["texto"],
            "opciones": pregunta["opciones"],
        }
        for pregunta in _PREGUNTAS
    ]


def responder(id_pregunta: int, opcion: int) -> tuple[bool, int] | None:
    for pregunta in _PREGUNTAS:
        if pregunta["id"] == id_pregunta:
            respuesta_correcta = pregunta["respuesta_correcta"]
            return opcion == respuesta_correcta, respuesta_correcta
    return None
