from dash import Input, Output
import plotly.express as px

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
        # --- CORRECCIÓN DE FILTROS "ALL" ---
        # Si el usuario selecciona "All", lo cambiamos a None para que no busque un texto "All" en el Parquet
        reg_filter = None if region == "All" or not region else region
        cat_filter = None if category == "All" or not category else category

        # Pasamos las variables saneadas a la función de filtrado
        filtered = filter_data(df, region=reg_filter, category=cat_filter)
        # ------------------------------------

        kpis = calculate_kpis(filtered)

        trend = revenue_trend(filtered)
        region_data = revenue_by_region(filtered)
        category_data = revenue_by_category(filtered)

        trend_fig = px.line(
            trend.to_pandas(),
            x="month",
            y="revenue",
            markers=True,
            title="Monthly Revenue Trend",
        )
        region_fig = px.bar(
            region_data.to_pandas(),
            x="revenue",
            y="region",
            orientation="h",
            title="Revenue by Region",
        )
        category_fig = px.bar(
            category_data.to_pandas(),
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
