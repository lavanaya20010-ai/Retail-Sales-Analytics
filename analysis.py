
import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales.csv")

# Calculate revenue for each order
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("===== RETAIL SALES ANALYTICS =====")

# Basic overview
print("\nFirst 5 records:")
print(df.head())

print("\nTotal number of orders:", len(df))
print("Total revenue: Rs.", round(df["Revenue"].sum(), 2))

# Sales by product
print("\n===== SALES BY PRODUCT =====")
print(
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Sales by category
print("\n===== SALES BY CATEGORY =====")
print(
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Sales by region
print("\n===== SALES BY REGION =====")
print(
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Best-selling product by revenue
best_product = df.groupby("Product")["Revenue"].sum().idxmax()
print("\nTop product by revenue:", best_product)
