import sqlite3
import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "ecommerce_sales.db"


# Connect to database
conn = sqlite3.connect(DATABASE_PATH)


print("=" * 50)
print("E-COMMERCE SALES SQL ANALYSIS")
print("=" * 50)


# 1. TOTAL SALES SUMMARY
print("\n========== SALES SUMMARY ==========")

query = """
SELECT
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM sales;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))

# 2. CATEGORY ANALYSIS

print("\n========== CATEGORY ANALYSIS ==========")

query = """
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))

# 3. REGION ANALYSIS

print("\n========== REGION ANALYSIS ==========")

query = """
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))

# 4. TOP 10 SUB-CATEGORIES

print("\n========== TOP 10 SUB-CATEGORIES ==========")

query = """
SELECT
    [Sub-Category],
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY [Sub-Category]
ORDER BY total_sales DESC
LIMIT 10;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))

# 5. LOSS-MAKING SUB-CATEGORIES

print("\n========== LOSS-MAKING SUB-CATEGORIES ==========")

query = """
SELECT
    [Sub-Category],
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY [Sub-Category]
HAVING SUM(Profit) < 0
ORDER BY total_profit;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))

# 6. CUSTOMER SEGMENT ANALYSIS

print("\n========== CUSTOMER SEGMENT ANALYSIS ==========")

query = """
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Segment
ORDER BY total_sales DESC;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))

# 7. DISCOUNT IMPACT

print("\n========== DISCOUNT IMPACT ON PROFIT ==========")

query = """
SELECT
    Discount,
    ROUND(AVG(Sales), 2) AS average_sales,
    ROUND(AVG(Profit), 2) AS average_profit
FROM sales
GROUP BY Discount
ORDER BY Discount;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))

# 8. TOP 10 STATES

print("\n========== TOP 10 STATES BY SALES ==========")

query = """
SELECT
    State,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY State
ORDER BY total_sales DESC
LIMIT 10;
"""

print(pd.read_sql_query(query, conn).to_string(index=False))


# Close connection
conn.close()


print("\n" + "=" * 50)
print("SQL ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 50)