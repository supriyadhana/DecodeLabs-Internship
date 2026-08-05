import pandas as pd

#Load Dataset
df = pd.read_excel(r"C:\Users\Admin\Downloads\Dataset for Data Analytics.xlsx")

#Display Dataset
print("First 5 Rows")
print(df.head())

#Dataset Shape
print("\nDataset Shape")
print(df.shape)

#Column Names
print("\nColumn Names")
print(df.columns)

#Dataset Information
print("\nDataset Information")
df.info()

#Missing Values
print("\nMissing Values")
print(df.isnull().sum())

#Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

#Remove Duplicates
df = df.drop_duplicates()

#Fill Missing Coupon Codes
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")


#Check Missing Values Again
print("\nMissing Values After Cleaning")
print(df.isnull().sum())

#Check Data Types
print("\nData Types")
print(df.dtypes)

#Save Cleaned Dataset
df.to_excel("data/Cleaned_Dataset.xlsx", index=False)

print("\nCleaning Completed Successfully!")
