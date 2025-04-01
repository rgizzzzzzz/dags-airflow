{{ config(materialized='table') }}

SELECT
    ProductID,
    Name AS ProductName,
    ProductSubcategoryID
FROM
    {{ source('production', 'product') }}
