select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

with __dbt__cte__stg_sales_order_detail as (


SELECT
    salesorderid,
    ProductID,
    OrderQty,
    unitprice
FROM
    "Adventureworks"."sales"."salesorderdetail"
)select
    salesorderid as unique_field,
    count(*) as n_records

from __dbt__cte__stg_sales_order_detail
where salesorderid is not null
group by salesorderid
having count(*) > 1



      
    ) dbt_internal_test