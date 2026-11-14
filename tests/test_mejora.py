from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_cantidad_solicitada_de_preguntas():
    respuesta = cliente.get("/api/preguntas?cantidad=3")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 3


def test_cantidad_por_defecto_y_limites_validos():
    assert len(cliente.get("/api/preguntas").json()) == 5
    assert len(cliente.get("/api/preguntas?cantidad=1").json()) == 1
    assert len(cliente.get("/api/preguntas?cantidad=5").json()) == 5


def test_cantidad_fuera_de_rango_es_rechazada():
    for cantidad in (0, 6):
        respuesta = cliente.get(f"/api/preguntas?cantidad={cantidad}")

        assert respuesta.status_code == 422
