from dash import Dash, html

from layouts.dashboard import create_layout
from callbacks.dashboard import register_callbacks

app = Dash(__name__, title="PharmaVision BI")
app.layout = create_layout()

register_callbacks(app)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)
