SELECT *
FROM orders;

SELECT OrderID, Product, Quantity, TotalPrice
FROM orders;

SELECT *
FROM orders
WHERE OrderStatus = 'Delivered';

SELECT OrderID, Product, TotalPrice
FROM orders
WHERE TotalPrice > 2000;

SELECT *
FROM orders
ORDER BY TotalPrice DESC;

SELECT Product, Quantity, TotalPrice
FROM orders
ORDER BY Quantity DESC;


SELECT Product, COUNT(*) AS OrderCount
FROM orders
GROUP BY Product;

SELECT PaymentMethod, COUNT(*) AS OrderCount
FROM orders
GROUP BY PaymentMethod
ORDER BY OrderCount DESC;

SELECT
    COUNT(*) AS TotalOrders,
    AVG(Quantity) AS AverageQuantity,
    SUM(TotalPrice) AS TotalSales,
    AVG(TotalPrice) AS AverageOrderValue
FROM orders;

SELECT
    Product,
    COUNT(*) AS OrderCount,
    SUM(TotalPrice) AS TotalSales,
    AVG(TotalPrice) AS AverageSales
FROM orders
GROUP BY Product
ORDER BY TotalSales DESC;