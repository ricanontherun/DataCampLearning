import pandas as pd

data_types = {
    "Weekly_Sales": "float"
}

# Date parsing, specify fields to be parsed as Dates, and their format.
parse_dates = ['Date']
date_formats = {
    'Date': '%Y-%m-%d'
}

df = pd.read_csv("data/retail-data-raw.csv", dtype=data_types, parse_dates=parse_dates, date_format=date_formats)

# Remove invalid data
df = df[df.Date.notnull() & df.Weekly_Sales.notnull()]

# Structure of data is one record per store, per department, per week.

# clean up the data, focus on the fields we'll use in subsequent operations.
df.fillna({
    'Weekly_Sales': df['Weekly_Sales'].mean(),
})

# Add month field
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Average monthly sales
grouped_by_month = df.groupby(['Month'])
weekly_sales = grouped_by_month['Weekly_Sales']
monthly_sales = weekly_sales.mean()

print(monthly_sales)