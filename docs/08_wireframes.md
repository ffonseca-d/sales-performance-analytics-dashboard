# Wireframes

## Overview

The goal of PharmaVision BI is to provide an intuitive analytical experience that enables business users to explore sales performance through a single interactive application.

Rather than displaying static dashboards, the application allows users to progressively analyze information through global filters, KPIs, rankings, trends, and detailed visualizations.

The dashboard follows a "filter once, analyze everywhere" philosophy, where all visualizations react to the same filtering context.

---

# Navigation Structure

```
Home
│
├── Executive Overview
├── Sales Performance
├── Geographic Analysis
└── Product Analysis
```

Global filters remain available across every page.

---

# Global Layout

```
+---------------------------------------------------------------+
|                       Header / Navigation                     |
+---------------------------------------------------------------+

| Date | Region | District | Route | Category | Product |

+---------------------------------------------------------------+

| KPI Cards                                                |

+---------------------------------------------------------------+

| Main Visualizations                                      |

+---------------------------------------------------------------+

| Secondary Analysis                                       |

+---------------------------------------------------------------+
```

---

# Global Filters

The following filters are shared across the entire application.

| Filter | Description |
|----------|-------------|
| Date | Analysis period |
| Region | Commercial region |
| District | Commercial district |
| Route | Sales route |
| Product Category | Product grouping |
| Product | Individual product |

Changing any filter updates every KPI and visualization simultaneously.

---

# Page 1 — Executive Overview

## Purpose

Provide a high-level summary of commercial performance.

### KPIs

- Total Revenue
- Units Sold
- YoY Growth
- Contribution %
- Active Customers

### Visualizations

- Revenue Trend
- Revenue by Region
- Revenue by Category
- Top Products
- Top Regions

### Business Questions

- How is the business performing?
- Are sales growing?
- Which regions contribute the most?

---

# Page 2 — Sales Performance

## Purpose

Analyze commercial performance at different hierarchy levels.

### KPIs

- Revenue
- Units
- Average Revenue
- Growth %

### Visualizations

- Regional Ranking
- District Ranking
- Route Ranking
- Customer Ranking
- Revenue Distribution

### Business Questions

- Which regions perform better?
- Which routes require attention?
- Which customers generate the highest revenue?

---

# Page 3 — Geographic Analysis

## Purpose

Visualize territorial performance.

### Visualizations

- Treemap by Region
- District Comparison
- Route Performance
- Geographic Rankings

### Business Questions

- Which territories are growing?
- Where should commercial efforts be focused?

---

# Page 4 — Product Analysis

## Purpose

Evaluate product portfolio performance.

### KPIs

- Revenue by Product
- Units Sold
- Product Contribution

### Visualizations

- Product Ranking
- Category Distribution
- Product Trend
- Pareto Analysis

### Business Questions

- Which products drive revenue?
- Which products are underperforming?

---

# User Experience Principles

The application follows these UX principles:

- Global filters across all pages.
- Minimal navigation depth.
- Progressive drill-down analysis.
- Fast loading.
- Consistent visual language.
- Business-first design.

---

# Dashboard Layout Guidelines

## Header

Contains:

- Application title
- Navigation menu
- Last refresh date

---

## Filter Section

Global filters are always visible.

Users should never navigate to configure filters.

---

## KPI Section

KPIs are displayed at the top of every page.

Each KPI should provide immediate business context.

---

## Visualization Section

Charts should answer business questions before presenting data.

Visualizations are organized from general to specific.

---

## Detail Section

Tables and rankings provide detailed exploration after high-level analysis.

---

# Visualization Principles

The dashboard prioritizes business readability over visual complexity.

Preferred visualizations include:

- KPI Cards
- Line Charts
- Horizontal Bar Charts
- Treemaps
- Bubble Charts
- Ranking Tables

Every visualization must answer at least one documented Business Question.

---

# Responsiveness

The dashboard is designed primarily for desktop users.

Layouts should adapt to standard laptop resolutions while maintaining readability.

---

# Why this matters

A Business Intelligence dashboard should guide users through a decision-making process rather than simply displaying charts.

The wireframes define how users interact with the platform, ensuring that every page, filter, KPI, and visualization contributes to answering meaningful business questions in a clear and intuitive way.