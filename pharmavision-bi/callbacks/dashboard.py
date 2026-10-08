from dash import Input, Output
import plotly.express as px
import polars as pl

from data import filter_data, load_data
from src.business.metrics import (
    calculate_kpis,
    revenue_by_category,
    revenue_by_region,
    revenue_trend,
)

def register_callbacks(app) -> None:
    df = load_data()
    
    @app.callback(
        Output("kpi-revenue", "children"),
        Output("kpi-units", "children"),
        Output("kpi-visited", "children"),
        Output("revenue-trend", "figure"),
        Output("revenue-region", "figure"),
        Output("revenue-category", "figure"),
        Input("region-filter", "value"),
        Input("category-filter", "value"),
    )
    def update_dashboard(region, category):
        # 1. Saneamos los filtros ignorando variaciones de "All" / "ALL"
        reg_filter = None if not region or region.upper() == "ALL" else region
        cat_filter = None if not category or category.upper() == "ALL" else category

        filtered = filter_data(df, region=reg_filter, category=cat_filter)
        kpis = calculate_kpis(filtered)

        # 2. Obtenemos los DataFrames de Polars agregados (que ya ocupan muy pocas filas)
        trend = revenue_trend(filtered)
        region_data = revenue_by_region(filtered)
        category_data = revenue_by_category(filtered)

        # 3. Forzamos a convertir la columna temporal a String directamente en Polars
        # Esto evita el bug de truncado/zonas horarias sin usar Pandas
        if "month" in trend.columns:
            trend = trend.with_columns(pl.col("month").dt.strftime("%Y-%m-%d"))

        # 4. Pasamos los objetos de Polars DIRECTAMENTE a Plotly Express
        trend_fig = px.line(
            trend,
            x="month",
            y="revenue",
            markers=True,
            title="Monthly Revenue Trend",
        )
        
        region_fig = px.bar(
            region_data,
            x="revenue",
            y="region",
            orientation="h",
            title="Revenue by Region",
        )
        
        category_fig = px.bar(
            category_data,
            x="category",
            y="revenue",
            title="Revenue by Category",
        )

        return (
            f"${kpis['revenue']:,.0f}",
            f"{kpis['units']:,.0f}",
            f"{kpis['visited_rate']:.1f}%",
            trend_fig,
            region_fig,
            category_fig,
        )
