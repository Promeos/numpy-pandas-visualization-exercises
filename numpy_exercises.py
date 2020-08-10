# importing the numpy module using conventional notation
import numpy as np

# create a 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
# Creating boolean masks using relational operators allows me to create
# An array of 1's and 0's. I can then use `np.sum` to total the numbers
# That meet the conditional expression.

# I found `np.count_zero` while looking for examples.
# https://github.com/numpy/numpy/issues/8913
# negative_numbers = np.count_nonzero(a < 0)

# Inside the parentheses I can utilize numpy's ability to create
# boolean masks using relational operators. a < 0 creates an array
# of boolean values - True = 1, False = 0 if the value is less than
# Zero - negative numbers. I apply the np.sum function
# To collect all 'True' values, represented by the value 1 and store it
# as a variable.
negative_numbers = (a < 0).sum()
print(f"Negative numbers: {negative_numbers}")


# How many positive numbers are there?
# positive_numbers = np.count_nonzero(a > 0)
# Similar to the exercise above, I create a boolean mask or filter array
# To create an array of 1's and 0's 
positive_numbers = (a > 0).sum()
print(f"Positive numbers: {positive_numbers}")

# How many even positive numbers are there?
# positive_evens = np.sum(a[a > 0] % 2 == 0)
positive_evens = ((a > 0) & (a % 2 == 0)).sum()
print(f"Positive even numbers: {positive_evens}")

# If you were to add 3 to each data point, how many positive numbers would there be?
plus_3_postive_numbers = (a + 3 > 0).sum()
print(f"Postive numbers after a + 3: {plus_3_postive_numbers}")

# If you squared each number, what would the new mean and standard deviation be?
a_mean = a.mean(dtype=np.float64)
a_stddev = a.std(dtype=np.float64)
print("\na's Mean and Standard Deviation BEFORE -> a ** 2")
print("-" * 40)
print("Mean --- {}\nStandard Deviation --- {}".format(a_mean, a_stddev))

a_mean_squared = (a ** 2).mean(dtype=np.float64)
a_stddev_squared = (a ** 2).std(dtype=np.float64)
print("\na's Mean and Standard Deviation AFTER -> a ** 2")
print("-" * 40)
print("Mean --- {}\nStandard Deviation --- {}\n".format(a_mean_squared, a_stddev_squared))

# A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.
a_centered = a - a_mean
print("a centered == a - a_mean == {}\n".format(a_centered))

# Calculate the z-score for each data point. Recall that the z-score is given by:
a_zscore = a_centered / a_stddev
print("a z-score == {}".format(a_zscore))


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold 
# the sum of all the numbers in above list
sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold
# the minimum of all the numbers in the above list
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold
# the max number of all the numbers in the above list
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold
# the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)

# Exercise 5 - Make a variable named product_of_a to hold
# the product of multiplying all the numbers in the above list together
# https://stackoverflow.com/questions/49863633/numpy-product-vs-numpy-prod-vs-ndarray-prod
# np.product?
# np.prod?
product_of_a = 1

for num in a:
    product_of_a *= num

# Exercise 6 - Make a variable named squares_of_a. It should hold
# each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [num ** 2 for num in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold
# only the odd numbers

odds_in_a = [num for num in a if(num % 2 != 0)]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold
# only the evens.
evens_in_a = [num for num in a if num % 2 == 0]

# What about life in two dimensions? A list of lists is a matrix, a table, a spreadsheet,
# a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, 
# average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)
sum_of_b = b.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()

# Exercise 5 - refactor the following to use numpy for calculating
# the product of all numbers multiplied together.
product_of_b = b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = np.square(b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 != 0]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
print(b.shape)

# Exercise 10 - transpose the array b.
b_transpose = b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b_reshape_list = b.reshape(1, 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, 
# each containing only 1 number (6 x 1)
b_reshape_list_of_lists = b.reshape(6, 1)


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable 
# is a numpy array prior to using numpy array methods.
c = np.array(c)
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = c.min()
max_of_c = c.max()
sum_of_c = c.sum()
product_of_c = c.prod()

# Exercise 2 - Determine the standard deviation of c.
stddev_of_c = c.std()

# Exercise 3 - Determine the variance of c.
variance_of_c = c.var()
# Exercise 4 - Print out the shape of the array c
print(c.shape)

# Exercise 5 - Transpose c and print out transposed result.
c_transpose = c.T
print(c_transpose)

# Exercise 6 - Get the dot product of the array c with c. 
c_dot_product = c.dot(c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed.
# Answer should be 261
sum_c_times_c_transposed = (c * c_transpose).sum()
print(sum_c_times_c_transposed)

# Exercise 8 - Write the code necessary to determine the product of c times c transposed.
# Answer should be 131681894400.
prod_c_times_c_transposed = (c * c_transpose).prod()
print(prod_c_times_c_transposed)


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
d_sine = np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
d_cosine = np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
d_tangent = np.tan(d)

# Exercise 4 - Find all the negative numbers in d
negative_nums_in_d = d[d < 0]

# Exercise 5 - Find all the positive numbers in d
positive_nums_in_d = d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
d_unique = np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
d_unique_count = len(np.unique(d))
print(d_unique_count)
# Exercise 8 - Print out the shape of d.
print(d.shape)

# Exercise 9 - Transpose and then print out the shape of d.
d_transpose = d.transpose()

# Exercise 10 - Reshape d into an array of 9 x 2
d_reshape = d.reshape(9, 2)
print(d_reshape)