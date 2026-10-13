
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

category_sales = df.groupby("Category")["Revenue"].sum()

category_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

print("Category chart saved successfully!")
