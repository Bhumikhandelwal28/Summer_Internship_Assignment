import pandas as pd

df = pd.read_csv("new.csv")
print("Original Data:\n", df)

# --- Data Cleaning ---

df['Total']=df['Total'].fillna(df['Price'] * df['Quantity'])

# Handle missing values
df.dropna(subset=['Date', 'Product'],inplace=True)  # Drop rows missing
df['Quantity']=df['Quantity'].fillna(0)  # Fill missing quantity with 0

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])
print("\nCleaned Data:\n", df)

# --- Data Analysis ---
product_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)
print("\nTotal Sales per Product:\n", product_sales)

daily_sales = df.groupby('Date')['Total'].sum()
print("\nTotal Sales per Day:\n", daily_sales)

avg_price = df.groupby('Product')['Price'].mean()
print("\nAverage Price per Product:\n", avg_price)

most_sold = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("\nMost Sold Products by Quantity:\n", most_sold)
