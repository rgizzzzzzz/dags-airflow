select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



with __dbt__cte__stg_product as (


SELECT
    ProductID,
    Name AS ProductName,
    ProductSubcategoryID
FROM
    "Adventureworks"."production"."product"
)select productid
from __dbt__cte__stg_product
where productid is null



      
    ) dbt_internal_test