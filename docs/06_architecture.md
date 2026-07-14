# Solution Architecture

## Overview

PharmaVision BI is designed as a modern Business Intelligence application inspired by enterprise analytics solutions.

The architecture separates backend data preparation from frontend visualization by using an analytical SQL view as the backend source and a preprocessed Apache Parquet dataset as the single source of truth consumed by the Dash application.

This approach prioritizes performance, maintainability, and scalability while keeping the dashboard completely independent from the database layer.

---

# Architectural Goals

The architecture has been designed to:

- Decouple the dashboard from the database.
- Optimize dashboard loading performance.
- Centralize business logic.
- Reuse analytical calculations across visualizations.
- Simulate a production-ready Business Intelligence solution.

---

# High-Level Architecture

```text
            SQL Analytical View
        (Backend Data Preparation)
                    │
                    ▼
             Parquet Export
                    │
                    ▼
      sales_dataset.parquet
          (Single Source of Truth)
                    │
                    ▼
            Data Access Layer
                (data.py)
                    │
                    ▼
        Business Logic Layer
        (KPIs & Calculations)
                    │
                    ▼
          Dash Application
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
    Layouts     Callbacks     Styles
                    │
                    ▼
                End User
```

---

# Architecture Layers

## 1. SQL Backend Layer

The analytical backend is responsible for preparing business-ready data before it reaches the dashboard.

Rather than querying transactional tables directly, all required joins, filters, and backend transformations are assumed to be handled within a SQL analytical view.

### Responsibilities

- Consolidate business information.
- Apply backend joins.
- Prepare analytical datasets.
- Simplify dashboard consumption.
- Serve as the export source for Parquet generation.

---

## 2. Parquet Layer

The SQL analytical view is exported into a single optimized Apache Parquet dataset.

This dataset acts as the **Single Source of Truth** for the dashboard.

### Responsibilities

- Store validated analytical data.
- Optimize read performance.
- Reduce loading times.
- Eliminate runtime database dependencies.

Dataset:

```
sales_dataset.parquet
```

---

## 3. Data Access Layer

Implemented in:

```
data.py
```

This layer is responsible for reading the Parquet dataset and exposing reusable data structures to the rest of the application.

### Responsibilities

- Load the Parquet dataset using Polars.
- Handle common filtering logic.
- Prepare reusable DataFrames.
- Provide standardized data access for KPI calculations.

This layer never contains visualization logic.

---

## 4. Business Logic Layer

This layer contains every business calculation used throughout the dashboard.

Examples include:

- Total Revenue
- Units Sold
- Year-over-Year Growth
- Contribution %
- Rankings
- Regional Performance
- Product Performance

Business calculations remain completely independent from the dashboard interface.

---

## 5. Presentation Layer

The presentation layer is implemented using Dash.

Its only responsibility is presenting information already prepared by the Business Logic Layer.

### Main Components

- app.py
- layouts/
- callbacks/
- styles/

Dashboard pages include:

- Executive Overview
- Sales Performance
- Geographic Analysis
- Product Analysis

---

# Project Structure

```text
pharmavision-bi/
│
├── docs/
│
├── data/
│   └── sales_dataset.parquet
│
├── layouts/
│   ├── executive.py
│   ├── sales.py
│   ├── geography.py
│   └── products.py
│
├── callbacks/
│   ├── executive.py
│   ├── sales.py
│   ├── geography.py
│   └── products.py
│
├── styles/
│
├── assets/
│
├── screenshots/
│
├── app.py
├── data.py
├── requirements.txt
└── README.md
```

---

# Data Flow

The application follows the workflow below:

1. Business data is consolidated into a SQL analytical view.
2. The SQL view is exported as an optimized Apache Parquet dataset.
3. `data.py` loads the Parquet file using Polars.
4. Business calculations are generated from the loaded dataset.
5. Dash layouts request processed information.
6. Callbacks update visualizations dynamically based on user interaction.
7. Charts are rendered using Plotly.

---

# Design Principles

## Single Source of Truth

The dashboard consumes only one analytical dataset.

Every KPI, visualization, and business calculation originates from the same validated Parquet file.

---

## Backend / Frontend Separation

Database preparation is isolated from dashboard development.

The frontend never connects directly to SQL.

---

## Performance First

Reading a single optimized Parquet dataset is significantly faster than executing multiple SQL queries during user interaction.

This approach minimizes latency and improves the overall dashboard experience.

---

## Separation of Concerns

Each module has a unique responsibility.

- SQL prepares data.
- data.py loads data.
- Business logic calculates KPIs.
- Dash renders information.

---

## Reusability

Business calculations can be reused across multiple dashboard pages without duplication.

---

## Maintainability

The modular architecture allows new dashboards, KPIs, and visualizations to be added with minimal impact on existing components.

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Backend | SQL Server (Analytical View) |
| Storage | Apache Parquet |
| Data Processing | Polars |
| Dashboard | Dash |
| Visualization | Plotly |
| Language | Python |

---

# Future Evolution

The current architecture is designed to support future enhancements, including:

- Automated Parquet generation pipeline.
- Scheduled data refresh.
- DuckDB integration.
- Additional dashboard modules.
- Cloud deployment.

---

# Why this matters

Modern Business Intelligence applications prioritize responsiveness, modularity, and maintainability.

By separating backend data preparation from frontend visualization and using a single optimized Parquet dataset as the application's source of truth, PharmaVision BI closely follows the architecture commonly adopted in enterprise analytics environments.

This design allows business users to interact with large analytical datasets efficiently while keeping the codebase clean, scalable, and easy to maintain.