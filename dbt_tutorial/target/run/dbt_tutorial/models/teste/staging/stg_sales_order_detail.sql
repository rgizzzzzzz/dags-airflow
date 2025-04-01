
  
    

  create  table "Adventureworks"."teste"."stg_sales_order_detail__dbt_tmp"
  
  
    as
  
  (
    

SELECT
    salesorderid,
    ProductID,
    OrderQty,
    unitprice
FROM
    "Adventureworks"."sales"."salesorderdetail"
  );
  