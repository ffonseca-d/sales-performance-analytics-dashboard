# MVP Notes

## Current implementation

The first runnable increment intentionally focuses on proving the core architecture:

```text
Synthetic Generator
       ↓
Parquet Dataset
       ↓
data.py
       ↓
KPI Functions
       ↓
Dash + Plotly
```

The SQL file in `sql/` documents the intended backend analytical-view layer. It is not executed by the local MVP because the public portfolio repository does not depend on a SQL Server instance.

## Next increment

- Add data validation.
- Add date filtering.
- Add YoY calculations.
- Expand hierarchy drill-down.
- Add more dashboard views.
- Add tests.
