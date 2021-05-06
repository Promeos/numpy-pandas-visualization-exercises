### 1. Inspecting a DataFrame

# Use pandas built-in method, .head() to display the first 5 rows of the dataset.
# Print the head of the homelessness data
print(homelessness.head())


### 2. Parts of a DataFrame

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness. Returns the column names of the homelessness dataframe.
print(homelessness.columns)

# Print the row index of homelessness. Returns the index values of the homelessness dataframe.
print(homelessness.index)


### 3. Sorting Rows

# Use pandas built-in method .sort_values to sort the values by a specified column.
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values(by='individuals')

# Print the top few rows of the newly sorted dataframe.
print(homelessness_ind.head())


### 4. Subsetting Columns

# Select the individuals column using bracket notation
individuals = homelessness['individuals']

# Print the first 5 rows of the dataset
print(individuals.head())


### 5. Subsetting Rows

# Use a boolean mask as a filter to the dataframe
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10_000]

# See the result
print(ind_gt_10k)


### 6. Subsetting rows by Categorical Variables

# Subset for rows in South Atlantic or Mid-Atlantic regions
# Use pandas built-in method `.isin()` to determine the rows where the region is in the South Atlantic or the Mid-Atlantic
south_mid_atlantic = homelessness[homelessness['region'].isin(['South Atlantic', 'Mid-Atlantic'])]

# See the result
print(south_mid_atlantic)


### 7. Adding new columns

# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_individuals col as proportion of individuals
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']

# See the result
print(homelessness)


### 8. Sort Rows, Subsetting Columns, Subsetting Rows, Adding new Columns.

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness.individuals / homelessness.state_pop

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values(by='indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result