## Rol
Actúa como desarrollador backend con experiencia en FastAPI.

## Objetivo
Modificar el endpoint GET /api/preguntas para que acepte el parámetro opcional `cantidad`, entre 1 y 5, y devuelva solo esa cantidad de preguntas. Sin el parámetro devuelve 5, y con un valor fuera del rango responde con el código 422. La página principal también debe permitir elegir cuántas preguntas se juegan. Además, crea una prueba nueva en tests/test_mejora.py que compruebe esta mejora.

## Contexto
Lee AGENTS.md, app/main.py, app/servicios.py y app/templates/index.html.

## Restricciones
No modifiques tests/test_aceptacion.py.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos y espera mi aprobación.

## Ejemplo
GET /api/preguntas?cantidad=3 devuelve 3 preguntas.
GET /api/preguntas?cantidad=8 devuelve 422.

## Criterio de éxito
`python -m pytest -v` pasa todas las pruebas (las de aceptación y las de la mejora). Si después de 3 intentos no se cumple, detente y explica el problema.