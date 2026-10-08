import os
from pathlib import Path
import polars as pl

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "generated" / "sales_dataset.parquet"

def load_data() -> pl.DataFrame:
    """Load the analytical dataset used by the dashboard."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH.resolve()}")

    # Retornamos el dataframe original con la fecha nativa de Polars
    return pl.read_parquet(DATA_PATH)


def filter_data(
    df: pl.DataFrame,
    region: str | None = None,
    category: str | None = None,
) -> pl.DataFrame:
    """Apply dashboard filters to the analytical dataset."""
    
    # Validamos convirtiendo a mayúsculas para evitar errores de formato
    if region and region.upper() != "ALL":
        df = df.filter(pl.col("region") == region)

    if category and category.upper() != "ALL":
        df = df.filter(pl.col("category") == category)

    return df

