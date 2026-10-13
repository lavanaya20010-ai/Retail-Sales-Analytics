
import pandas as pd
import matplotlib.pyplot as plt

print("Starting monthly sales analysis...")

df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["Month"] = df["Date"].dt.strftime("%B")

monthly_sales = df.groupby("Month", sort=False)["Revenue"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_sales_trend.png")
plt.show()

print("\nMonthly chart saved successfully!")
