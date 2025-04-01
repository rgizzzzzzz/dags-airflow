{{ config(materialized='table') }}

WITH sales AS (
    SELECT
        sod.ProductID,
        SUM(sod.unitprice) AS TotalSales
    FROM {{ ref('stg_sales_order_detail') }} sod
    GROUP BY sod.ProductID
)
SELECT 
    s.ProductID,
    s.TotalSales,
    p.ProductSubcategoryID
FROM sales s
JOIN {{ ref('stg_product') }} p ON s.ProductID = p.ProductID


