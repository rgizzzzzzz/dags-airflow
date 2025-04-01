
  
    

  create  table "Adventureworks"."teste"."int_sales_by_product__dbt_tmp"
  
  
    as
  
  (
    

WITH sales AS (
    SELECT
        sod.ProductID,
        SUM(sod.unitprice) AS TotalSales
    FROM "Adventureworks"."teste"."stg_sales_order_detail" sod
    GROUP BY sod.ProductID
)
SELECT 
    s.ProductID,
    s.TotalSales,
    p.ProductSubcategoryID
FROM sales s
JOIN "Adventureworks"."teste"."stg_product" p ON s.ProductID = p.ProductID
  );
  