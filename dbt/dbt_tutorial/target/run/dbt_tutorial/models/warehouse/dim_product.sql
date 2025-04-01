
  
    

  create  table "Adventureworks"."teste"."dim_product__dbt_tmp"
  
  
    
  
  (
    productid int not null primary key,
    name varchar,
    productnumber varchar,
    makeflag boolean,
    finishedgoodsflag boolean,
    color varchar,
    safetystocklevel int,
    reorderpoint int,
    standardcost numeric,
    listprice numeric,
    size varchar,
    sizeunitmeasurecode varchar,
    weightunitmeasurecode varchar,
    weight numeric,
    daystomanufacture int,
    productline varchar,
    class varchar,
    style varchar,
    productsubcategoryid int,
    productmodelid int,
    sellstartdate timestamp,
    sellenddate timestamp,
    discontinueddate timestamp,
    modifieddate timestamp
    
    )
 ;
    insert into "Adventureworks"."teste"."dim_product__dbt_tmp" (
      productid, name, productnumber, makeflag, finishedgoodsflag, color, safetystocklevel, reorderpoint, standardcost, listprice, size, sizeunitmeasurecode, weightunitmeasurecode, weight, daystomanufacture, productline, class, style, productsubcategoryid, productmodelid, sellstartdate, sellenddate, discontinueddate, modifieddate
    )
  
  (
    
    select productid, name, productnumber, makeflag, finishedgoodsflag, color, safetystocklevel, reorderpoint, standardcost, listprice, size, sizeunitmeasurecode, weightunitmeasurecode, weight, daystomanufacture, productline, class, style, productsubcategoryid, productmodelid, sellstartdate, sellenddate, discontinueddate, modifieddate
    from (
        SELECT 
    productid, 
    "name", 
    productnumber, 
    makeflag, 
    finishedgoodsflag, 
    color, 
    safetystocklevel, 
    reorderpoint, 
    standardcost, 
    listprice, 
    "size", 
    sizeunitmeasurecode, 
    weightunitmeasurecode, 
    "weight", 
    daystomanufacture, 
    productline, 
    "class", 
    "style", 
    productsubcategoryid, 
    productmodelid, 
    sellstartdate, 
    sellenddate, 
    discontinueddate, 
    modifieddate
FROM 
    "Adventureworks"."production"."product"
    ) as model_subq
  );
  