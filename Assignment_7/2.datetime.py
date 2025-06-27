import pandas as pd
print(pd.date_range('6-1-2025',periods=5))
# Sample DataFrame with string dates
df = pd.DataFrame({
    'date': ['2023-06-01', '2024-01-28', '2025-12-31']
})
df['date'] = pd.to_datetime(df['date'], errors='raise')  # or errors='coerce' if needed

print(df[df['date'] > '2024-01-01'])

print(pd.Timestamp.now())      # current datetime
print(pd.Timestamp.today())     # current date

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_name'] = df['date'].dt.day_name()
df['month_name'] = df['date'].dt.month_name()
df['week'] = df['date'].dt.isocalendar().week
print(df)

df.set_index('date', inplace=True)
monthly_summary = df.resample('ME').count()
print("Monthly summary:\n", monthly_summary)

print("Entries from 2024:\n", df.loc['2024'])

# Final DataFrame
print("Final DataFrame:\n", df)