
    
    

with child as (
    select productid as from_field
    from "Adventureworks"."warehouse"."fact_sales"
    where productid is not null
),

parent as (
    select productid as to_field
    from "Adventureworks"."warehouse"."dim_product"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


