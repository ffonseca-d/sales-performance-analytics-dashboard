from dash import Dash
from layouts.dashboard import create_layout
from callbacks.dashboard import register_callbacks

app = Dash(__name__, title="PharmaVision BI", suppress_callback_exceptions=True)

# Volvemos a cargarlo de forma limpia sin pasarle argumentos
app.layout = create_layout()

register_callbacks(app)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)
