import pandas as pd

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\Decodelab internship\data\Cleaned_Dataset.csv")
# Display first 5 rows
print("First 5 Rows")
print(df.head())

# Dataset shape
print("\nDataset Shape")
print(df.shape)

# Column names
print("\nColumn Names")
print(df.columns)

# Dataset information
print("\nDataset Information")
df.info()

# Basic Statistics
print("\nBasic Statistics")
print(df.describe())

# Mean, Median, Count
print("\nQuantity Statistics")
print("Mean:", df["Quantity"].mean())
print("Median:", df["Quantity"].median())
print("Count:", df["Quantity"].count())

print("\nUnit Price Statistics")
print("Mean:", df["UnitPrice"].mean())
print("Median:", df["UnitPrice"].median())

print("\nTotal Price Statistics")
print("Mean:", df["TotalPrice"].mean())
print("Median:", df["TotalPrice"].median())

# Product Distribution
print("\nProduct Distribution")
print(df["Product"].value_counts())

# Payment Method Distribution
print("\nPayment Method Distribution")
print(df["PaymentMethod"].value_counts())

# Order Status Distribution
print("\nOrder Status Distribution")
print(df["OrderStatus"].value_counts())

# Referral Source Distribution
print("\nReferral Source Distribution")
print(df["ReferralSource"].value_counts())

# Outlier Detection
print("\nQuantity Outliers")

Q1 = df["Quantity"].quantile(0.25)
Q3 = df["Quantity"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Quantity"] < lower) |
    (df["Quantity"] > upper)
]

print("Number of Outliers:", len(outliers))
print(outliers)

# Key Observations

print("\nKey Observations")

print("- The dataset contains 1,200 orders and 14 columns.")
print("- The average Quantity is 2.95, with a median of 3.")
print("- The average Unit Price is 356.41, while the median is 364.21.")
print("- The average Total Price is 1053.97, with a median of 823.62.")
print("- Printer has the highest number of orders with 181 orders.")
print("- Phone has the lowest number of orders with 156 orders.")
print("- Online is the most commonly used payment method with 258 orders.")
print("- Cancelled is the most common order status with 250 orders.")
print("- Instagram is the most common referral source with 259 orders.")
print("- No outliers were detected in the Quantity column using the IQR method.")
