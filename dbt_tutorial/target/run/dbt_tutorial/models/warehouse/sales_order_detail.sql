
  
    

  create  table "Adventureworks"."teste"."sales_order_detail__dbt_tmp"
  
  
    as
  
  (
    

SELECT 
    salesorderid, 
    salesorderdetailid, 
    carriertrackingnumber, 
    orderqty, 
    productid, 
    specialofferid, 
    unitprice, 
    unitpricediscount, 
    rowguid as row_id, 
    modifieddate
from "Adventureworks"."sales"."salesorderdetail"
  );
  