
  
    

  create  table "Adventureworks"."teste"."stg_product_category__dbt_tmp"
  
  
    as
  
  (
    

SELECT
    ProductCategoryID,
    Name AS CategoryName
FROM
    "Adventureworks"."production"."productcategory"
  );
  