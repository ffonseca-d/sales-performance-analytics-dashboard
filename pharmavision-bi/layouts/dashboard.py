from dash import dcc, html

def _kpi_card(title: str, value_id: str) -> html.Div:
    return html.Div(
        [
            html.Div(title, className="kpi-title"),
            html.Div(id=value_id, className="kpi-value"),
        ],
        className="kpi-card",
    )

def create_layout() -> html.Div:  # <-- Quitamos el argumento 'df'
    # Escribe aquí las regiones y categorías reales de tu set de datos
    regions = [
        {"label": "All", "value": "ALL"},
        {"label": "East", "value": "East"},
        {"label": "West", "value": "West"},
        {"label": "North", "value": "North"},
        {"label": "South", "value": "South"}
    ]
    
    categories = [
        {"label": "All", "value": "ALL"},
        {"label": "Antibiotics", "value": "Antibiotics"},
        {"label": "Analgesics", "value": "Analgesics"},
        {"label": "Vitamins", "value": "Vitamins"}
    ]

    return html.Div(
        [
            html.Header(
                [
                    html.H1("PharmaVision BI"),
                    html.P("Sales Performance Analytics"),
                ],
                className="header",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label("Region"),
                            dcc.Dropdown(
                                id="region-filter",
                                options=regions,
                                value="ALL",
                                clearable=False,
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            html.Label("Category"),
                            dcc.Dropdown(
                                id="category-filter",
                                options=categories,
                                value="ALL",
                                clearable=False,
                            ),
                        ]
                    ),
                ],
                className="filters",
            ),
            html.Div(
                [
                    _kpi_card("Total Revenue", "kpi-revenue"),
                    _kpi_card("Units Sold", "kpi-units"),
                    _kpi_card("Visited Rate", "kpi-visited"),
                ],
                className="kpi-grid",
            ),
            html.Div(
                [
                    dcc.Graph(id="revenue-trend"),
                    dcc.Graph(id="revenue-region"),
                ],
                className="chart-grid",
            ),
            html.Div(
                [dcc.Graph(id="revenue-category")],
                className="chart-full",
            ),
        ],
        className="container",
    )
