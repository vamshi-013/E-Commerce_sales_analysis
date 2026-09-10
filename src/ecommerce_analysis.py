import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw_sales_data.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH, encoding="latin1")

print("=" * 50)
print("E-COMMERCE SALES ANALYSIS")
print("=" * 50)

# Remove duplicate rows
print(f"\nOriginal rows: {len(df)}")

df = df.drop_duplicates()

print(f"Rows after removing duplicates: {len(df)}")

# Save cleaned dataset
cleaned_file = OUTPUT_DIR / "cleaned_sales_data.csv"
df.to_csv(cleaned_file, index=False)

print("\nCleaned dataset saved successfully!")

# SALES SUMMARY

print("\n========== SALES SUMMARY ==========")

print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Total Quantity Sold: {df['Quantity'].sum():,}")

# CATEGORY ANALYSIS

category_analysis = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== CATEGORY ANALYSIS ==========")
print(category_analysis.round(2))

category_analysis.to_csv(
    OUTPUT_DIR / "category_analysis.csv"
)

# REGION ANALYSIS

region_analysis = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== REGION ANALYSIS ==========")
print(region_analysis.round(2))

region_analysis.to_csv(
    OUTPUT_DIR / "region_analysis.csv"
)

# TOP SUB-CATEGORIES

sub_category_analysis = (
    df.groupby("Sub-Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== TOP SUB-CATEGORIES ==========")
print(sub_category_analysis.head(10).round(2))

sub_category_analysis.to_csv(
    OUTPUT_DIR / "sub_category_analysis.csv"
)

# DISCOUNT ANALYSIS

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Average_Sales=("Sales", "mean"),
        Average_Profit=("Profit", "mean")
    )
    .round(2)
)

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis)

discount_analysis.to_csv(
    OUTPUT_DIR / "discount_analysis.csv"
)

# VISUALIZATION 1 - SALES BY CATEGORY

category_analysis["Total_Sales"].plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_by_category.png"
)

plt.close()

# ==========================================
# VISUALIZATION 2 - PROFIT BY REGION
# ==========================================

region_analysis["Total_Profit"].plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "profit_by_region.png"
)

plt.close()

# ==========================================
# VISUALIZATION 3 - SALES BY SUB-CATEGORY
# ==========================================

top_subcategories = sub_category_analysis.head(10)

top_subcategories["Total_Sales"].sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sales")
plt.ylabel("Sub-Category")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_subcategories.png"
)

plt.close()

# ==========================================
# VISUALIZATION 4 - DISCOUNT VS PROFIT
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "discount_vs_profit.png"
)

plt.close()

print("\n==========================================")
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("==========================================")

print("\nFiles saved in the output folder.")