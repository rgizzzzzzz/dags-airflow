

select duedate, orderdate, count(1) as num_occurrences
from "Adventureworks"."warehouse"."sales_order_header"
where duedate <= orderdate
group by 1, 2

