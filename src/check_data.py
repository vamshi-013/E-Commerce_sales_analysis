import pandas as pd

# Load dataset
df = pd.read_csv("data/raw_sales_data.csv", encoding="latin1")

print("=" * 50)
print("E-COMMERCE SALES DATASET CHECK")
print("=" * 50)

print("\nDataset loaded successfully!")

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())