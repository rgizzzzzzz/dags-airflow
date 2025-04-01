{{ config(materialized='table') }}

SELECT
    ProductCategoryID,
    Name AS CategoryName
FROM
    {{ source('production', 'productcategory') }}
