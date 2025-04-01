{{ config(materialized='table') }}

SELECT
    salesorderid,
    ProductID,
    OrderQty,
    unitprice
FROM
    {{ source('sales', 'salesorderdetail') }}
