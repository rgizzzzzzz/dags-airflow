
    
    



with __dbt__cte__stg_product as (


SELECT
    ProductID,
    Name AS ProductName,
    ProductSubcategoryID
FROM
    "Adventureworks"."production"."product"
)select product_id
from __dbt__cte__stg_product
where product_id is null


