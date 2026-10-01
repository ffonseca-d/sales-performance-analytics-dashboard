# PharmaVision BI

Interactive Business Intelligence application for pharmaceutical commercial analytics.

> **Optimize data once. Analyze everywhere.**

PharmaVision BI is a portfolio project inspired by enterprise BI workflows. It uses a preprocessed analytical dataset in Apache Parquet as the single source of truth for a modular Dash/Plotly application.

## Current MVP

- Synthetic pharmaceutical sales data generator
- Analytical Parquet dataset
- Polars-based data access layer
- Reusable KPI calculations
- Interactive Dash dashboard
- Global filters
- SQL analytical-view blueprint
- Technical documentation

## Architecture

```text
SQL Analytical View
        |
        v
Parquet Export
        |
        v
sales_dataset.parquet
(Single Source of Truth)
        |
        v
data.py
        |
        v
Business Metrics
        |
        v
Dash Application
   |       |       |
layouts callbacks styles
```

## Quick start

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the synthetic dataset:

```bash
python -m src.data.generator
```

Run the application:

```bash
python app.py
```

Then open the local Dash URL shown in the terminal.

## Project structure

```text
pharmavision-bi/
├── app.py
├── data.py
├── requirements.txt
├── README.md
├── sql/
│   └── 01_sales_analytical_view.sql
├── src/
│   ├── business/
│   │   └── metrics.py
│   └── data/
│       └── generator.py
├── layouts/
│   └── dashboard.py
├── callbacks/
│   └── dashboard.py
├── styles/
├── data/
│   └── generated/
└── docs/
```

## Confidentiality

All data in this repository is synthetic. No proprietary client, product, customer, route, or company information is included.

## Roadmap

1. Synthetic dataset
2. Data validation and transformation
3. KPI engine
4. Interactive dashboard
5. Documentation and portfolio polish
