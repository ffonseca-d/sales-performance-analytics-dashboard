from pathlib import Path
import polars as pl

import os
from pathlib import Path
import polars as pl

# 1. Forzamos a buscar la ruta absoluta real desde la raíz del contenedor de Render
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "generated" / "sales_dataset.parquet"

def load_data() -> pl.DataFrame:
    """Load the analytical dataset used by the dashboard."""
    
    # 2. Imprime la ruta exacta en los logs de Render para saber dónde está buscando
    print(f"--- INTENTANDO CARGAR PARQUET DESDE: {DATA_PATH.resolve()} ---", flush=True)
    
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH.resolve()}. Run the generator first."
        )

    return pl.read_parquet(DATA_PATH)


def filter_data(
    df: pl.DataFrame,
    region: str | None = None,
    category: str | None = None,
) -> pl.DataFrame:
    """Apply dashboard filters to the analytical dataset."""
    # Si llega None o "ALL", ignoramos el filtro y mostramos todo
    if region and region != "ALL":
        df = df.filter(pl.col("region") == region)

    if category and category != "ALL":
        df = df.filter(pl.col("category") == category)

    return df
