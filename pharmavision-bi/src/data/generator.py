from pathlib import Path

import numpy as np
import polars as pl


SEED = 42
ROWS = 50_000
OUTPUT = Path(__file__).parents[2] / "data" / "generated" / "sales_dataset.parquet"


def generate_dataset(rows: int = ROWS) -> pl.DataFrame:
    """Generate a fully synthetic pharmaceutical sales dataset."""
    rng = np.random.default_rng(SEED)

    regions = np.array(["North", "Central", "West", "South", "East"])
    districts = np.array(
        ["District A", "District B", "District C", "District D", "District E"]
    )
    routes = np.array([f"Route {i:02d}" for i in range(1, 21)])
    products = np.array(
        ["CardioMax", "NeuroCare", "GastroPlus", "ImmunoAid", "DermaClear", "RespiraX"]
    )
    categories = {
        "CardioMax": "Cardiovascular",
        "NeuroCare": "Neurology",
        "GastroPlus": "Gastroenterology",
        "ImmunoAid": "Immunology",
        "DermaClear": "Dermatology",
        "RespiraX": "Respiratory",
    }

    product = rng.choice(products, rows)
    units = rng.integers(1, 80, rows)
    unit_price = rng.uniform(8, 120, rows).round(2)

    dates = rng.choice(
        np.arange(np.datetime64("2024-01-01"), np.datetime64("2026-01-01")),
        rows,
    )

    df = pl.DataFrame(
        {
            "date": dates,
            "region": rng.choice(regions, rows),
            "district": rng.choice(districts, rows),
            "route": rng.choice(routes, rows),
            "distributor": [f"Distributor {i:03d}" for i in rng.integers(1, 101, rows)],
            "product": product,
            "category": [categories[p] for p in product],
            "units": units,
            "revenue": (units * unit_price).round(2),
            "visited_flag": rng.choice([True, False], rows, p=[0.78, 0.22]),
        }
    )

    return df.sort("date")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df = generate_dataset()
    df.write_parquet(OUTPUT, compression="zstd")
    print(f"Generated {df.height:,} rows -> {OUTPUT}")


if __name__ == "__main__":
    main()
