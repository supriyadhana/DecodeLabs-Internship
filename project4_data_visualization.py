import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("data/Cleaned_Dataset.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("Dataset loaded successfully!")
print(df.head())

# Visualization 1: Quantity vs Total Price

plt.figure(figsize=(8, 5))

plt.scatter(df["Quantity"], df["TotalPrice"], alpha=0.6)

plt.title("Relationship Between Quantity and Total Price")
plt.xlabel("Quantity Ordered")
plt.ylabel("Total Price")

plt.grid(True)
plt.savefig("quantity_vs_totalprice.png", dpi=300, bbox_inches="tight")
plt.show()


# Visualization 2: Total Sales by Product

product_sales = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))

plt.bar(product_sales.index, product_sales.values)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("total_sales_by_product.png", dpi=300, bbox_inches="tight")
plt.show()

# Visualization 3: Order Status Distribution

status_counts = df["OrderStatus"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(status_counts.index, status_counts.values)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("order_status_distribution.png", dpi=300, bbox_inches="tight")
plt.show()


# Visualization 4: Sales Trend Over Time

daily_sales = df.groupby("Date")["TotalPrice"].sum().sort_index()

plt.figure(figsize=(10, 5))

plt.plot(daily_sales.index, daily_sales.values)

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_trend_over_time.png", dpi=300, bbox_inches="tight")
plt.show()

# Visualization 5: Average Order Value by Product

average_price = df.groupby("Product")["TotalPrice"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))

plt.bar(average_price.index, average_price.values)

plt.title("Average Order Value by Product")
plt.xlabel("Product")
plt.ylabel("Average Total Price")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("average_order_value_by_product.png", dpi=300, bbox_inches="tight")
plt.show()

# Visualization 6: Total Price Distribution - Box Plot

plt.figure(figsize=(8, 5))

plt.boxplot(df["TotalPrice"])

plt.title("Distribution of Total Price")
plt.ylabel("Total Price")

plt.grid(True, axis="y")

plt.savefig("total_price_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

# Visualization 7: Payment Method Distribution - Pie Chart

payment_counts = df["PaymentMethod"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Method Distribution")

plt.savefig("payment_method_pie_chart.png", dpi=300, bbox_inches="tight")
plt.show()


# Visualization 8: Quantity Distribution - Histogram

plt.figure(figsize=(8, 5))

plt.hist(df["Quantity"], bins=5)

plt.title("Distribution of Order Quantity")
plt.xlabel("Quantity")
plt.ylabel("Number of Orders")

plt.grid(True, axis="y")

plt.savefig("quantity_histogram.png", dpi=300, bbox_inches="tight")
plt.show()