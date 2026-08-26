import pandas as pd
import sqlite3
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "output" / "cleaned_sales_data.csv"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "ecommerce_sales.db"

# Create database folder if needed
DATABASE_DIR.mkdir(exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Connect to SQLite
conn = sqlite3.connect(DATABASE_PATH)

# Save dataframe as SQL table
df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

# Verify row count
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")

total_rows = cursor.fetchone()[0]

conn.close()

print("\n==========================================")
print("DATABASE CREATED SUCCESSFULLY!")
print("==========================================")

print("\nTable name: sales")
print(f"Total rows inserted: {total_rows}")

print("\nDatabase location:")
print(DATABASE_PATH)