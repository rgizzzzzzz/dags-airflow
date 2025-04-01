
  
    

  create  table "Adventureworks"."teste"."mart_sales_by_category__dbt_tmp"
  
  
    as
  
  (
    

WITH category_sales AS (
    SELECT
        pc.CategoryName,
        SUM(sp.TotalSales) AS TotalSales
    FROM "Adventureworks"."teste"."int_sales_by_product" sp
    JOIN "Adventureworks"."teste"."stg_product_category" pc 
        ON sp.ProductSubcategoryID = pc.ProductCategoryID
    GROUP BY pc.CategoryName
)
SELECT * FROM category_sales
  );
  