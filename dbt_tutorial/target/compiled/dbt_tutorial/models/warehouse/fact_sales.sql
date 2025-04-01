SELECT 
    h.salesorderid, 
    d.salesorderdetailid,
    h.revisionnumber, 
    h.orderdate, 
    h.duedate, 
    h.shipdate, 
    h.status, 
    h.onlineorderflag, 
    h.purchaseordernumber, 
    h.subtotal, 
    h.taxamt, 
    h.freight, 
    h.totaldue,
    d.carriertrackingnumber, 
    d.orderqty, 
    d.productid, 
    d.specialofferid, 
    d.unitprice, 
    d.unitpricediscount
FROM "Adventureworks"."teste"."sales_order_header" AS h
JOIN "Adventureworks"."teste"."sales_order_detail" AS d
ON h.salesorderid = d.salesorderid