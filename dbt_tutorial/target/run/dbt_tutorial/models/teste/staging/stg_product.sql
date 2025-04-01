
  
    

  create  table "Adventureworks"."teste"."stg_product__dbt_tmp"
  
  
    as
  
  (
    

SELECT
    ProductID,
    Name AS ProductName,
    ProductSubcategoryID
FROM
    "Adventureworks"."production"."product"
  );
  