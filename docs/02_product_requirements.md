# Product Requirements Document (PRD)

## Project

**PharmaVision BI**

---

# Purpose

Develop an end-to-end Business Intelligence platform that enables pharmaceutical commercial teams to monitor sales performance, analyze business trends, and make informed decisions through interactive dashboards and AI-assisted insights.

The project aims to demonstrate practical skills in Business Intelligence development, including data engineering, SQL, Python, dashboard development, and Generative AI integration.

---

# Product Goals

## Primary Goals

- Deliver an interactive Business Intelligence platform.
- Showcase an end-to-end analytics workflow.
- Demonstrate best practices in software architecture and documentation.
- Simulate an enterprise-level analytics solution using synthetic data.

## Secondary Goals

- Build a portfolio-ready project.
- Strengthen technical interview discussions.
- Practice modern BI development methodologies.

---

# Stakeholders

| Stakeholder | Responsibility |
|------------|----------------|
| Commercial Director | Consumes executive KPIs |
| Regional Manager | Monitors regional performance |
| Business Analyst | Performs detailed analysis |
| Data Analyst (Developer) | Builds and maintains the platform |

---

# Functional Requirements

## Data

The platform must:

- Load sales information from Parquet files.
- Support large datasets efficiently.
- Allow future integration with SQL databases.

---

## Data Processing

The system must:

- Clean raw data.
- Validate data quality.
- Calculate business KPIs.
- Generate reusable analytical datasets.

---

## Dashboard

The application must include:

- Executive Overview
- Sales Performance
- Geographic Analysis
- AI Insights

---

## Filtering

Users must be able to filter information by:

- Date
- Region
- District
- Route
- Product
- Category

All filters should interact dynamically across the application.

---

## KPIs

The platform must calculate:

- Total Revenue
- Units Sold
- Year-over-Year Growth
- Contribution Percentage
- Average Revenue per Customer
- Top Performing Regions
- Top Products

---

## Visualizations

The dashboard should include:

- KPI Cards
- Time Series
- Bar Charts
- Treemap
- Bubble Chart
- Ranking Tables

---

## Artificial Intelligence

The application should include AI-assisted features capable of:

- Explaining sales trends.
- Summarizing dashboard insights.
- Suggesting possible business actions.
- Answering predefined business questions.

---

# Non-Functional Requirements

## Performance

- Load dashboard in less than 3 seconds.
- Efficient processing using Polars.

---

## Scalability

The architecture should allow:

- Additional dashboards.
- New KPIs.
- Additional datasets.

---

## Maintainability

The codebase must be:

- Modular
- Documented
- Reusable
- Easy to extend

---

## Usability

The dashboard should:

- Be intuitive.
- Require minimal training.
- Prioritize business users over technical users.

---

# Assumptions

- Synthetic data accurately represents real business scenarios.
- Users are familiar with basic sales KPIs.
- Data quality issues are simulated.

---

# Constraints

- No confidential information.
- No proprietary datasets.
- No company branding.
- No internal business logic.

---

# Success Criteria

The project will be considered successful when:

- Users can answer key business questions quickly.
- Dashboard navigation feels intuitive.
- AI-generated insights provide meaningful explanations.
- The repository is fully documented.
- The application can be executed locally with minimal setup.

---

# Out of Scope

The first version will NOT include:

- Authentication
- User management
- Forecasting models
- Real-time streaming
- Cloud deployment
- Role-based permissions

These features may be added in future releases.

---

# Release Strategy

## MVP (v1.0)

- Interactive dashboard
- Synthetic dataset
- KPI calculations
- AI-assisted insights
- Complete documentation

## Future Versions

### v1.1

- Forecasting

### v1.2

- SQL backend

### v2.0

- Cloud deployment
- User authentication
- Advanced AI features