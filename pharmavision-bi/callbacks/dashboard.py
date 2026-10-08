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
        # 1. Saneamos los filtros ignorando variaciones de "All" / "ALL"
        reg_filter = None if not region or region.upper() == "ALL" else region
        cat_filter = None if not category or category.upper() == "ALL" else category

        filtered = filter_data(df, region=reg_filter, category=cat_filter)
        kpis = calculate_kpis(filtered)

        # 2. Las funciones de métricas de Polars se ejecutarán perfectamente con fechas nativas
        trend = revenue_trend(filtered)
        region_data = revenue_by_region(filtered)
        category_data = revenue_by_category(filtered)

        # 3. Convertimos a Pandas para Plotly
        df_trend_pandas = trend.to_pandas()
        
        # Evitamos problemas de zonas horarias en Render convirtiendo la fecha calculada a texto para Plotly
        if "month" in df_trend_pandas.columns:
            df_trend_pandas["month"] = df_trend_pandas["month"].astype(str)

        trend_fig = px.line(
            df_trend_pandas,
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
