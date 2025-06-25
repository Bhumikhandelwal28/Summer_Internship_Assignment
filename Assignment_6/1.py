import pandas as pd

date_series = pd.Series(['2025-01-01', '2025-01-02', '2025-01-03'])
date_series = pd.to_datetime(date_series)
values = pd.Series([10, 20, 30])
time_series = pd.Series(values.values, index=date_series)

print(time_series)

