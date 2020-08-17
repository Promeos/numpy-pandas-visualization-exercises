# importing the numpy module using conventional notation
import numpy as np

# create a numpy array to practice data array fundamentals
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

# I found `np.count_zero` while looking for examples.
# https://github.com/numpy/numpy/issues/8913
# negative_numbers = np.count_nonzero(a < 0)

# Inside the parentheses I can utilize numpy's ability to create
# boolean masks using relational operators. a < 0 creates a series
# of boolean values - True = 1, False = 0 if the value is less than
# Zero - selecting only negative numbers. I apply the `np.sum` function
# To collect all 'True' values, represented by the value 1 and store it
# in a variable called negative_numbers.
negative_numbers = (a < 0).sum()
print(f"Negative numbers: {negative_numbers}")

# How many positive numbers are there?

# positive_numbers = np.count_nonzero(a > 0)

# Similar to the exercise above, I create a boolean mask or filter series
# To create a series of True/False, 1's and 0's based on a conditional expression.
# I want to find all the values in a that are greater than zero. Selecting
# Positive Values! Once the 1's/0's are generated, I call the `np.sum` function
# To add up all True values. This tells me how many elements the series `a` have a
# Value greater than 0.  
positive_numbers = (a > 0).sum()
print(f"Positive numbers: {positive_numbers}")

# How many even positive numbers are there?

# positive_evens = np.sum(a[a > 0] % 2 == 0)

# Viewing the code snippet above ^, I had no idea about '|', '&', '~'
# As a work around I use a boolean mask to search for values greater than 0.
# I then evaluate the filter series once more looking for numbers that are easily divisible
# by 2.

# Now I know! Thank you Zach! Due to Numpy syntax, I'll need to place each
# Conditional expression inside of parentheses. I can then use a logical operator
# To compare the boolean values from the two conditional expressions. Yay!
# Using Numpy's equivalent of `and` == '&'. Once everything inside of the parentheses
# Evaluates, I can use the `np.sum` function 'to vaccuum up' all 1's. It will return
# A single value, total positive even numbers in series `a` which I store in the 
# Variable positive_evens.
positive_evens = ((a > 0) & (a % 2 == 0)).sum()
print(f"Positive even numbers: {positive_evens}")

# If you were to add 3 to each data point, how many positive numbers would there be?

# Using a Numpy's vectorization/broadcasting, I can apply a calculation to a series
# 'a + 3'. This means that every element in series `a` with have 3 added to its value.
# I can compare the resulting series in a conditional expression - all values greater than 0.
# Once the conditional expression is finished evaluating, I can use `np.sum` to total
# All True/1's values in the boolean mask. I store that value in a variable called
# 'plus_3_positive_numbers' for safe keeping.
plus_3_postive_numbers = (a + 3 > 0).sum()
print(f"Postive numbers after a + 3: {plus_3_postive_numbers}")

# If you squared each number, what would the new mean and standard deviation be?

# Yay no more `sum(list)` / `len(list)``. I include the mean and standard deviation before
# Squaring series `a` to see the current mean and standard deviation. 
a_mean = a.mean(dtype=np.float64) # Docs say np.float64 is more precise
a_stddev = a.std(dtype=np.float64)
print("\na's Mean and Standard Deviation BEFORE -> a ** 2")
print("-" * 40)
print("Mean --- {}\nStandard Deviation --- {}".format(a_mean, a_stddev))

# Because I'm not using a relational operator == No boolean values, I can perform 
# Math operations directly on series `a`. Expression inside of the parentheses is finished
# Evaluating, I can call `np.mean`\`np.std` to calculate the mean and standard deviation
# Of `a` squared.
a_squared_mean = (a ** 2).mean(dtype=np.float64)
a_squared_stddev = (a ** 2).std(dtype=np.float64)
print("\na's Mean and Standard Deviation AFTER -> a ** 2")
print("-" * 40)
print("Mean --- {}\nStandard Deviation --- {}\n".format(a_squared_mean, a_squared_stddev))

# A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.

# I did not know this was called `centering`. Sweet. I substract the mean value of `a`
# From the series `a` to center the datapoints at 0. I store the centered series in the variable
# Named `a_centered`.
a_centered = a - a_mean
print("a centered == a - a_mean == {}\n".format(a_centered))

# Calculate the z-score for each data point. Recall that the z-score is given by:

# I used the variable `a_centered` divide by `a_stddev` to calculate the Z-Score of
# series `a`. Z-Score tells us how many standard deviations a datapoint is from the mean.
a_zscore = a_centered / a_stddev
print("a z-score == {}".format(a_zscore))


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold 
# the sum of all the numbers in above list

# I call Python's built-in function `sum()` to sum all the values in a list/collection.
# I store the total value in a variable called `sum_of_a`.
sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold
# the minimum of all the numbers in the above list

# I call Python's built-in function `min()` to find the smallest value in a list/collection.
# I store the smallest value in a variable called `min_of_a`.
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold
# the max number of all the numbers in the above list

# I call Python's built-in function `max()` to find the largest value in a list/collection.
# I store the largest value in a variable called `max_of_a`.
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold
# the average of all the numbers in the above list

# NOOOOOOOO. LOL. See line 67.
mean_of_a = sum_of_a / len(a)

# Exercise 5 - Make a variable named product_of_a to hold
# the product of multiplying all the numbers in the above list together

# https://stackoverflow.com/questions/49863633/numpy-product-vs-numpy-prod-vs-ndarray-prod
# np.product?
# np.prod?

# This one tripped me up. I need to create a variable outside of a for loop to store the
# Product of all elements in a list. Why 1 and not 0? I use 1 because the value
# at `a[0]` multiplied by itself is the just the value at 'a[0]'. I can use the shorthand
# assignment operator *= to multiply every element with those operated on so far. At the end
# of the for loop, variable `product_of_a` stores the product of list `a`.
product_of_a = 1

for num in a:
    product_of_a *= num

# Exercise 6 - Make a variable named squares_of_a. It should hold
# each number in a squared like [1, 4, 9, 16, 25...]

# Using a list comprehension, I can create a new list from the exisiting list and peform
# an operation on each element of a list. For every number in list `a`, I square the number
# at each interation. I can store the list comprehension in a variable named `squares_of_a`.
squares_of_a = [num ** 2 for num in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold
# only the odd numbers

# Using a list comprehension with an if clause, I can create a new list from an existing one.
# In this exercise I want to only store values in a new list if they're odd.
# Each iteration I compare the value in the if clause. Inside the If clause I compare a
# Value in a conditional expression. If the value is NOT evenly divisible by 2, then it's
# an odd number. Once the list comprehension is finished evaluating, I store the new list
# of odd numbers in a variable called `odds_in_a`
odds_in_a = [num for num in a if(num % 2 != 0)]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold
# only the evens.

# Similar to the example above, I invert the conditional expression in the if clause to
# find all even values. I store those values in a variable called `evens_in_a`.
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

# I use the `np.array` function to cast b from type list -> numpy.ndarray
# Once `b` is converted, I can call `np.sum` directly on Array `b` to return the total
# Of all values in `b`. I store that value in a variable called `sum_of_b`
b = np.array(b)
sum_of_b = b.sum()

# Exercise 2 - refactor the following to use numpy.

# Using `np.min` I can locate the smallest value in array `b`. An axis isn't specified,
# So the function runs over the entire array.
min_of_b = b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

# Using `np.max` I can comb over the entire array `b` to locate the highest value. Similar
# To `np.min` I have the option to find a max value on an axis, or the entire array.
max_of_b = b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b

# Using `np.mean` I can find the mean of array `b`. dtype included for accuracy
mean_of_b = b.mean(dtype=np.float64)

# Exercise 5 - refactor the following to use numpy for calculating
# the product of all numbers multiplied together.

# Using `np.prod` or `np.product` I can calculate the product of an array. No 0's in
# array `b`...
product_of_b = b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares

# I can use `np.square` to create a new array with each value in array `b` squared.
squares_of_b = np.square(b)

# Exercise 7 - refactor using numpy to determine the odds_in_b

# Like the examples with array `a`, I can use a boolean mask inside square brackets
# To create a filter to find: All odd values. The new array with only odd values is
# Stored in `odds_in_b` 
odds_in_b = b[b % 2 != 0]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
print(b.shape)

# Exercise 10 - transpose the array b.
b_transpose = b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# I can use `np.reshape` directly on array to change the dimensions of the array.
# I cannot make an array that is more or less than the number of elements in the
# exisiting array.
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