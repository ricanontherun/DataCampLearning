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

# We only care about records where Weekly_Sales > 10,000
df = df[df.Weekly_Sales > 10000]

# clean up the data, focus on the fields we'll use in subsequent operations.
df.fillna({
    'Weekly_Sales': df['Weekly_Sales'].mean(),
})

df.fillna(0, inplace=True)

# Add month field
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

df.to_csv("data/retail-data-cleaned.csv", index=False)
