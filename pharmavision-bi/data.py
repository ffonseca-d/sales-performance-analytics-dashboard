import os
from pathlib import Path
import polars as pl

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "generated" / "sales_dataset.parquet"

def load_data() -> pl.DataFrame:
    """Load the analytical dataset used by the dashboard."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH.resolve()}."
        )

    df = pl.read_parquet(DATA_PATH)
    
    # CONVERSIÓN CRÍTICA PARA SERVIDORES NUBE:
    # Convertimos la columna 'date' de tipo pl.Date a texto plano (String)
    df = df.with_columns(
        pl.col("date").dt.strftime("%Y-%m-%d")
    )

    return df


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
