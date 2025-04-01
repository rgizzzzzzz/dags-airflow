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
)select
    productid as unique_field,
    count(*) as n_records

from __dbt__cte__stg_product
where productid is not null
group by productid
having count(*) > 1



      
    ) dbt_internal_test