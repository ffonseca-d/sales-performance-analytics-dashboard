from dash import Dash

from layouts.dashboard import create_layout
from callbacks.dashboard import register_callbacks
from data import load_data  # 1. Asegúrate de importar tu lector de parquet

# 2. Cargamos el dataframe una sola vez al arrancar el servidor
df_inicial = load_data()

app = Dash(__name__, title="PharmaVision BI", suppress_callback_exceptions=True)

# 3. Le pasamos el dataframe como argumento a la función
app.layout = create_layout(df_inicial)

register_callbacks(app)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)
