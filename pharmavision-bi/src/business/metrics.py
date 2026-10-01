import polars as pl


def calculate_kpis(df: pl.DataFrame) -> dict[str, float]:
    """Calculate dashboard-level KPIs from the filtered dataset."""
    revenue = df["revenue"].sum()
    units = df["units"].sum()
    visited_rate = df["visited_flag"].mean() * 100 if df.height else 0

    return {
        "revenue": float(revenue),
        "units": float(units),
        "visited_rate": float(visited_rate),
    }


def revenue_by_region(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df.group_by("region")
        .agg(pl.col("revenue").sum().alias("revenue"))
        .sort("revenue", descending=True)
    )


def revenue_by_category(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df.group_by("category")
        .agg(pl.col("revenue").sum().alias("revenue"))
        .sort("revenue", descending=True)
    )


def revenue_trend(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df.with_columns(pl.col("date").dt.truncate("1mo").alias("month"))
        .group_by("month")
        .agg(pl.col("revenue").sum().alias("revenue"))
        .sort("month")
    )
