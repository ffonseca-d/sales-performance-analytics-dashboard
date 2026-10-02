from pathlib import Path
import polars as pl

DATA_PATH = Path(__file__).parent / "data" / "generated" / "sales_dataset.parquet"

def load_data() -> pl.DataFrame:
    """Load the analytical dataset used by the dashboard."""
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
    if region and region != "ALL":
        df = df.filter(pl.col("region") == region)

    if category and category != "ALL":
        df = df.filter(pl.col("category") == category)

    return df
