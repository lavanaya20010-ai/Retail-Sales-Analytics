
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Analytics Dashboard")
st.write("Analyze sales revenue, products, categories, and regions.")

df = pd.read_csv("sales.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%B")

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{df['Revenue'].sum():,.0f}")
col2.metric("Total Orders", len(df))
col3.metric("Units Sold", int(df["Quantity"].sum()))

st.divider()

# Category analysis
st.subheader("Sales by Category")
category_sales = df.groupby("Category")["Revenue"].sum()
st.bar_chart(category_sales)

# Region analysis
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Revenue"].sum()
st.bar_chart(region_sales)

# Monthly sales trend
st.subheader("Monthly Sales Trend")
monthly_sales = df.groupby("Month", sort=False)["Revenue"].sum()
st.line_chart(monthly_sales)

# Data table
st.subheader("Sales Data")
st.dataframe(df, use_container_width=True)
