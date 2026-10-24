import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Customer Behavior and Sales Trends",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Customer Behavior and Sales Trends")
st.write("Analyze customer purchases and sales data.")

df = pd.read_csv("data/customer_sales.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

st.subheader("📊 Sales Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{df['TotalAmount'].sum():,.0f}")
col2.metric("Total Orders", len(df))
col3.metric("Unique Customers", df["CustomerID"].nunique())

st.divider()

st.subheader("💰 Sales by Category")

category_sales = df.groupby("Category")["TotalAmount"].sum()

fig, ax = plt.subplots()
category_sales.plot(kind="bar", ax=ax)
ax.set_xlabel("Category")
ax.set_ylabel("Total Sales (₹)")
ax.set_title("Category-wise Sales")
plt.xticks(rotation=0)
st.pyplot(fig)

st.subheader("📅 Monthly Sales Trend")

df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["TotalAmount"].sum()

fig2, ax2 = plt.subplots()
monthly_sales.plot(kind="line", marker="o", ax=ax2)
ax2.set_xlabel("Month")
ax2.set_ylabel("Total Sales (₹)")
ax2.set_title("Monthly Sales")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

st.subheader("👥 Customer Gender Analysis")

gender_count = df["Gender"].value_counts()
st.bar_chart(gender_count)

st.subheader("📦 Sales Data Preview")
st.dataframe(df.head(20), use_container_width=True)