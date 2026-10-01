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
        Output("region-filter", "options"),
        Output("category-filter", "options"),
        Input("region-filter", "value"),
    )
    def populate_filters(_):
        regions = [{"label": "All", "value": "ALL"}] + [
            {"label": value, "value": value}
            for value in sorted(df["region"].unique().to_list())
        ]
        categories = [{"label": "All", "value": "ALL"}] + [
            {"label": value, "value": value}
            for value in sorted(df["category"].unique().to_list())
        ]
        return regions, categories

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
        filtered = filter_data(df, region=region, category=category)
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
