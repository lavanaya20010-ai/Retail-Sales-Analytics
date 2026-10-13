
import pandas as pd

df = pd.read_csv("sales.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("===== BUSINESS SALES INSIGHTS =====")

# Best-performing product
product_sales = df.groupby("Product")["Revenue"].sum()
print("\nTop product by revenue:", product_sales.idxmax())

# Best-performing region
region_sales = df.groupby("Region")["Revenue"].sum()
print("Top region:", region_sales.idxmax())

# Best-performing category
category_sales = df.groupby("Category")["Revenue"].sum()
print("Top category:", category_sales.idxmax())

# Monthly sales
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%B")
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("Highest-sales month:", monthly_sales.idxmax())
print("Highest monthly revenue: Rs.", monthly_sales.max())

# Overall revenue
print("\nTotal revenue: Rs.", df["Revenue"].sum())
print("Total orders:", len(df))
print("Total units sold:", df["Quantity"].sum())
