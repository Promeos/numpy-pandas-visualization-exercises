### 1. Mean and Median

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame to display information about the dataset: Number of rows, columns, missing values, column dtypes, memory usage.
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())


### 2. Summarizing Dates

# Print the maximum of the date column to return the most recent date in the dataset.
print(sales['date'].max())

# Print the minimum of the date column to return the earliest date in the dataset.
print(sales['date'].min())


### 3. Efficient Summaries

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column. Pass the function to the .agg method of the dataframe.
print(sales['temperature_c'].agg(iqr))


### 4. Cumulative Statistics

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values(by='date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1.weekly_sales.cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col. AWESOME!!!!
sales_1_1['cum_max_sales'] = sales_1_1.weekly_sales.cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])


### 5. Dropping Duplicates

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
# Although the boolean mask isn't explicity set to equals True, short circuit operations apply to boolean masks as they do with if statements.
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates['date'])


### 6. Counting Categorical Variables

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type. The sum of all values is equal to 1
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)


### 7. Store Statistics: What percent of sales occurred at each store type

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)


### 8. Calculations with Groupby

# Group by type; calc total weekly sales by aggregating the weekly_sales column
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales['weekly_sales'])
print(sales_propn_by_type)


### 9. Multiple Grouped Summaries

# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


### 10. Pivot Tables: Pivoting on one Variable

# Pivot for mean weekly_sales for each store type
# pandas pivot table method calculates the mean of the data by default.
mean_sales_by_type = sales.pivot_table(index='type', values='weekly_sales')

# Print mean_sales_by_type
print(mean_sales_by_type)


### 11. Fill in missing values and sum values with pivot tables

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(index='department', columns='type', values='weekly_sales', fill_value=0))