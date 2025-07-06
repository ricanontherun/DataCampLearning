# Import the cleaned and prepared data frames.
from data import df

# Average monthly sales across all data years.
average_weekly_sales_per_month = df.groupby(['Month'])['Weekly_Sales'].mean().round(2)
