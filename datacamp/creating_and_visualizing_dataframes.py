### 1. Which Avocado Size is Most Popular?

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(x='size', y='sum', kind='bar')

# Show the plot
plt.show()


### 2. Changes in Sales Over Time

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
# The lineplot will automatically set the x axis with the datetime column.
nb_sold_by_date.plot(kind='line')

# Show the plot
plt.show()


### 3. Avocado Supply and Demand

# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x='nb_sold', y='avg_price', title='Number of avocados sold vs. average price', kind='scatter')

# Show the plot
plt.show()


### 4. Price of Conventional vs. Organic Avocadoes

# Histogram of conventional avg_price 
avocados[avocados['type'] == 'conventional']['avg_price'].hist()

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist()

# Add a legend
plt.legend(['conventional', 'organic'])

# Show the plot
plt.show()


### 5. Fill in Missing Values

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
# Incredible!!! 
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()


### 6. Remove Missing Values

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())


### 7. Replace Missing Values

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()


### 8. List of Dictionaries

# Create a list of dictionaries with new data
# Each key value pair corresponds to a column name the value in that column, for each row.
avocados_list = [
    {'date': '2019-11-03', 'small_sold': 10376832, 'large_sold':7835071},
    {'date': '2019-11-10', 'small_sold': 10717154, 'large_sold':8561348}
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)


### 9. Dictionary of Lists

# Create a dictionary of lists with new data
# Similar to the example above, each key-value pair corresponds to a column name and a list of values.
avocados_dict = {
  "date": ['2019-11-17', '2019-12-01'],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)


### 10. CSV to DataFrame

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv('airline_bumping.csv')

# Take a look at the DataFrame
print(airline_bumping.head())


### 11. DataFrame to CSV

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k', ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv('airline_totals_sorted.csv')