/*
    PharmaVision BI
    Backend blueprint

    In the production-inspired architecture, the dashboard would consume
    an analytical SQL view. The resulting view would then be exported to
    sales_dataset.parquet.

    This file intentionally uses generic table and column names.
*/

CREATE VIEW analytics.vw_sales_analytical AS
SELECT
    s.sale_date AS date,
    r.region_name AS region,
    d.district_name AS district,
    rt.route_name AS route,
    c.distributor_name AS distributor,
    p.product_name AS product,
    p.category_name AS category,
    s.units,
    s.revenue,
    s.visited_flag
FROM sales.fact_sales AS s
INNER JOIN master.regions AS r
    ON s.region_id = r.region_id
INNER JOIN master.districts AS d
    ON s.district_id = d.district_id
INNER JOIN master.routes AS rt
    ON s.route_id = rt.route_id
INNER JOIN master.distributors AS c
    ON s.distributor_id = c.distributor_id
INNER JOIN master.products AS p
    ON s.product_id = p.product_id;
