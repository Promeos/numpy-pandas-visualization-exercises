import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
# Creating boolean masks using relational operators allows me to create
# An array of 1's and 0's. I can then use `np.sum` to total the numbers
# That meet the conditional expression.

# I found `np.count_zero` while looking for examples.
# https://github.com/numpy/numpy/issues/8913
# negative_numbers = np.count_nonzero(a < 0)
negative_numbers = np.sum(a < 0)
print(f"Negative numbers: {negative_numbers}")


# How many positive numbers are there?
# positive_numbers = np.count_nonzero(a > 0)
positive_numbers = np.sum(a > 0)
print(f"Positive numbers: {positive_numbers}")

# How many even positive numbers are there?
positive_evens = np.sum(a[a > 0] % 2 == 0)
print(f"Positive even numbers: {positive_evens}")

# If you were to add 3 to each data point, how many positive numbers would there be?
plus_3_postive_numbers = np.sum(a + 3 > 0)
print(f"Postive numbers after a + 3: {plus_3_postive_numbers}")

# If you squared each number, what would the new mean and standard deviation be?
a_mean = np.mean(a)
a_stddev = np.std(a)
print("\na's Mean and Standard Deviation BEFORE -> a ** 2")
print("-" * 40)
print("Mean --- {}\nStandard Deviation --- {}".format(a_mean, a_stddev))

a_mean_squared = np.mean(a ** 2, dtype=np.float64)
a_stddev_squared = np.std(a ** 2, dtype=np.float64)
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
sum_of_a


# Exercise 2 - Make a variable named min_of_a to hold
#  the minimum of all the numbers in the above list

# Exercise 3 - Make a variable named max_of_a to hold
#  the max number of all the numbers in the above list

# Exercise 4 - Make a variable named mean_of_a to hold
#  the average of all the numbers in the above list

# Exercise 5 - Make a variable named product_of_a to hold
#  the product of multiplying all the numbers in the above list together

# Exercise 6 - Make a variable named squares_of_a. It should hold
#  each number in a squared like [1, 4, 9, 16, 25...]

# Exercise 7 - Make a variable named odds_in_a. It should hold
#  only the odd numbers

# Exercise 8 - Make a variable named evens_in_a. It should hold
#  only the evens.

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.

# Exercise 10 - transpose the array b.

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2


