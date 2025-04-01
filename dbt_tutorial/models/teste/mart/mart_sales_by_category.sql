{{ config(materialized='table') }}

WITH category_sales AS (
    SELECT
        pc.CategoryName,
        SUM(sp.TotalSales) AS TotalSales
    FROM {{ ref('int_sales_by_product') }} sp
    JOIN {{ ref('stg_product_category') }} pc 
        ON sp.ProductSubcategoryID = pc.ProductCategoryID
    GROUP BY pc.CategoryName
)
SELECT * FROM category_sales
