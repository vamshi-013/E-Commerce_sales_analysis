# E-Commerce Sales Dashboard

## Project Overview

This project analyzes an e-commerce sales dataset to understand sales performance, profitability, customer segments, regions, categories, and the impact of discounts on profit.

The project was built using Python, SQL, SQLite, and Power BI to demonstrate an end-to-end data analytics workflow.

---

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- SQLite
- SQL
- Power BI
- Git & GitHub

---

## Project Workflow

1. Loaded and inspected the raw sales dataset.
2. Checked data types, missing values, and duplicate records.
3. Removed duplicate records and created a cleaned dataset.
4. Performed exploratory data analysis using Python.
5. Created visualizations for sales and profit analysis.
6. Stored the cleaned dataset in a SQLite database.
7. Performed business analysis using SQL queries.
8. Built an interactive Power BI dashboard.

---

## Dataset

- Original Records: 9,994
- Duplicate Records Removed: 17
- Final Records: 9,977
- Columns: 13

Key columns include:

- Ship Mode
- Segment
- Region
- Category
- Sub-Category
- Sales
- Quantity
- Discount
- Profit

---

## Key Insights

### Sales Performance

- Total Sales: **$2.30M**
- Total Profit: **$286.24K**
- Total Quantity Sold: **37,820**

### Category Performance

- Technology generated the highest sales.
- Technology also generated the highest profit.
- Office Supplies generated strong profit despite lower sales compared to Technology.

### Regional Performance

- West region generated the highest sales and profit.
- East region was the second-best performing region.

### Loss-Making Products

Some sub-categories generated negative profit:

- Tables
- Bookcases
- Supplies

### Discount Impact

Higher discounts generally resulted in lower average profit.

High discount levels such as 30%, 40%, and above showed negative average profit, indicating that excessive discounting can negatively impact profitability.

---

## Power BI Dashboard

The interactive dashboard includes:

- Total Sales KPI
- Total Profit KPI
- Total Quantity KPI
- Profit Margin KPI
- Sales by Region
- Sales by Category
- Sales by Sub-Category
- Profit by Category
- Discount Impact on Average Profit
- Region and Category filters

---

## Dashboard Preview

![E-Commerce Sales Dashboard](output/ecommerce_sales_dashboard.png)

---

## Project Structure

```text
ecommerce_sales_dashboard/
│
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
│
├── database/
│   └── ecommerce_sales.db
│
├── output/
│   ├── ecommerce_sales_dashboard.png
│   └── analysis_visualizations
│
├── power_bi/
│   └── ecommerce_sales_dashboard.pbix
│
├── sql/
│   └── ecommerce_sales_queries.sql
│
├── src/
│   ├── check_data.py
│   ├── ecommerce_analysis.py
│   ├── create_database.py
│   └── run_sql_analysis.py
│
├── insights.md
├── requirements.txt
└── README.md