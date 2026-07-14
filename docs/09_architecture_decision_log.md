# Architecture Decision Log

## Overview

This document records the most important architectural and technical decisions made during the development of PharmaVision BI.

The purpose of this log is to document not only *what* decisions were made, but also *why* they were made, including the trade-offs considered.

Keeping a decision log improves maintainability, provides historical context, and helps future contributors understand the rationale behind the architecture.

---

# Decision 001

## Title

Business Intelligence Application instead of a traditional Dashboard

### Status

Accepted

### Date

2026-07

### Context

The project could be implemented as a simple dashboard containing charts and KPIs.

However, the objective of this portfolio is to demonstrate the design of a complete Business Intelligence solution rather than a single reporting interface.

### Decision

Develop the project as a modular Business Intelligence application composed of multiple analytical views sharing the same business logic and data source.

### Rationale

This approach better represents real enterprise BI solutions and allows the project to demonstrate software architecture, modularity, and maintainability.

---

# Decision 002

## Title

Single Parquet Dataset as the Single Source of Truth

### Status

Accepted

### Date

2026-07

### Context

A traditional BI solution could consume multiple relational tables following a dimensional model.

However, modern analytical applications frequently consume preprocessed analytical datasets for improved performance.

### Decision

Use a single optimized Apache Parquet dataset as the application's only data source.

### Rationale

- Faster loading times.
- Reduced memory consumption.
- Simpler architecture.
- Consistent KPI calculations.
- Better dashboard responsiveness.

### Trade-offs

Pros

- Excellent read performance.
- Simpler application architecture.
- Easy deployment.
- Reduced code complexity.

Cons

- Data refresh requires regenerating the Parquet file.
- Less flexible than querying a live database.

---

# Decision 003

## Title

SQL as Backend Preparation Layer

### Status

Accepted

### Date

2026-07

### Context

The dashboard requires business-ready data but should remain independent from transactional databases.

### Decision

Assume that backend data preparation is performed through an analytical SQL view.

The dashboard never connects directly to SQL.

Instead, the SQL view is exported into a Parquet dataset consumed by the application.

### Rationale

This architecture closely resembles enterprise Business Intelligence environments while keeping the frontend lightweight.

---

# Decision 004

## Title

Polars as Data Processing Library

### Status

Accepted

### Date

2026-07

### Context

The application requires efficient reading and transformation of analytical datasets.

### Decision

Use Polars as the primary dataframe library.

### Rationale

- Excellent Parquet support.
- Faster execution than Pandas for analytical workloads.
- Lazy evaluation support.
- Lower memory usage.
- Modern API.

### Alternative Considered

Pandas

### Why not Pandas?

Although Pandas remains the industry standard, Polars provides better performance for analytical datasets and aligns with modern BI development practices.

---

# Decision 005

## Title

Dash as Dashboard Framework

### Status

Accepted

### Date

2026-07

### Context

Several dashboard frameworks were considered.

### Decision

Develop the frontend using Dash.

### Rationale

Dash provides greater flexibility for building modular analytical applications while maintaining full control over callbacks, layouts, and reusable components.

### Alternatives Considered

- Streamlit
- Power BI
- Tableau

### Why Dash?

The goal of the project is to demonstrate software development skills alongside Business Intelligence capabilities rather than relying on low-code visualization platforms.

---

# Decision 006

## Title

Modular Project Structure

### Status

Accepted

### Date

2026-07

### Context

The project could be implemented in a single Python file.

### Decision

Separate the application into independent modules:

- app.py
- data.py
- layouts/
- callbacks/
- styles/

### Rationale

A modular structure improves readability, maintainability, and scalability while reflecting enterprise Dash applications.

---

# Decision 007

## Title

Synthetic Dataset

### Status

Accepted

### Date

2026-07

### Context

The original project that inspired PharmaVision BI was developed using confidential enterprise data.

### Decision

Generate a fully synthetic dataset inspired by realistic pharmaceutical commercial scenarios.

### Rationale

- Preserve confidentiality.
- Avoid proprietary information.
- Enable public distribution.
- Maintain realistic business complexity.

---

# Decision 008

## Title

Business-first Development

### Status

Accepted

### Date

2026-07

### Context

Many portfolio projects begin by implementing charts.

### Decision

Design the project starting from business problems, business questions, and KPIs before implementing visualizations.

### Rationale

Business Intelligence exists to answer business questions, not simply to display data.

Every visualization included in PharmaVision BI must support at least one documented business question.

---

# Future Decisions

Future versions of this document will include decisions regarding:

- Deployment strategy.
- Automated ETL.
- Testing strategy.
- CI/CD.
- Cloud hosting.

---

# Why this matters

Every software project is the result of a series of architectural decisions.

Documenting these decisions makes the project easier to understand, maintain, and evolve while demonstrating the reasoning behind the chosen technologies and architecture.

Rather than documenting only the final solution, this project also documents the thought process that led to each technical decision.