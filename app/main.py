from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import dash
import dash_core_components as dcc
import dash_html_components as html
from starlette.middleware.wsgi import WSGIMiddleware


# Crear instancia de FastAPI
app = FastAPI()

# Crear la app Dash
dash_app = dash.Dash(__name__, server=app, routes_pathname_prefix="/dash/")


dash_app.layout = html.Div(children=[
    html.H1("Dashboard en Azure"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Ejemplo de Gráfica'
            }
        }
    )
])

# Integrar Dash en FastAPI
app.mount("/dash", WSGIMiddleware(dash_app.server))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
