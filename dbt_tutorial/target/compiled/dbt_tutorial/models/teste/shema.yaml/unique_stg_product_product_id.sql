
    
    

with __dbt__cte__stg_product as (


SELECT
    ProductID,
    Name AS ProductName,
    ProductSubcategoryID
FROM
    "Adventureworks"."production"."product"
)select
    product_id as unique_field,
    count(*) as n_records

from __dbt__cte__stg_product
where product_id is not null
group by product_id
having count(*) > 1


