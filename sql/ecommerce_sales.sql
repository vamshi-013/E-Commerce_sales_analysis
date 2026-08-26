-- ==========================================
-- E-COMMERCE SALES SQL ANALYSIS
-- ==========================================


-- 1. Total sales, profit and quantity
SELECT
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM sales;


-- 2. Sales and profit by category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;


-- 3. Sales and profit by region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;


-- 4. Top 10 sub-categories by sales
SELECT
    [Sub-Category],
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY [Sub-Category]
ORDER BY total_sales DESC
LIMIT 10;


-- 5. Loss-making sub-categories
SELECT
    [Sub-Category],
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY [Sub-Category]
HAVING SUM(Profit) < 0
ORDER BY total_profit;


-- 6. Sales and profit by customer segment
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Segment
ORDER BY total_sales DESC;


-- 7. Discount impact on profit
SELECT
    Discount,
    ROUND(AVG(Sales), 2) AS average_sales,
    ROUND(AVG(Profit), 2) AS average_profit
FROM sales
GROUP BY Discount
ORDER BY Discount;


-- 8. Top 10 states by sales
SELECT
    State,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY State
ORDER BY total_sales DESC
LIMIT 10;