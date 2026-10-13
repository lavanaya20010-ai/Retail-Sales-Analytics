
import pandas as pd
import matplotlib.pyplot as plt

# Read the sales data
df = pd.read_csv("sales.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Calculate revenue by region
region_sales = df.groupby("Region")["Revenue"].sum()
region_sales = region_sales.sort_values(ascending=False)

# Create the bar chart
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("sales_by_region.png")
plt.show()

print("Chart saved as sales_by_region.png")
