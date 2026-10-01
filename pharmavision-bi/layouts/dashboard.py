from dash import dcc, html


def _kpi_card(title: str, value_id: str) -> html.Div:
    return html.Div(
        [
            html.Div(title, className="kpi-title"),
            html.Div(id=value_id, className="kpi-value"),
        ],
        className="kpi-card",
    )


def create_layout() -> html.Div:
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
                                options=[{"label": "All", "value": "ALL"}],
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
                                options=[{"label": "All", "value": "ALL"}],
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
