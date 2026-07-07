import numpy as np

# =====================================================================
# Task 1: Create an array consisting of linearly spaced elements between 0 to 9
# =====================================================================
# Using np.linspace to generate 10 linearly spaced numbers from 0 to 9
original_array = np.linspace(0, 9, 10, dtype=int)
print("1. Original 1D Array:")
print(original_array)
print("-" * 40)

# =====================================================================
# Task 2: Replace all odd numbers with -1 without modifying the original array
# =====================================================================
# np.where returns a new array based on the condition (if odd, use -1, else keep original)
modified_array = np.where(original_array % 2 != 0, -1, original_array)
print("2. Modified Array (odds replaced with -1):")
print(modified_array)
print("Verify original array remains unchanged:")
print(original_array)
print("-" * 40)

# =====================================================================
# Task 3: Convert the original 1D array into a 2D array with two rows
# =====================================================================
# Reshaping the 10-element array into 2 rows and 5 columns
two_d_array = original_array.reshape(2, 5)
print("3. Converted 2D Array (with 2 rows):")
print(two_d_array)
print("-" * 40)

# =====================================================================
# Task 4: Iterate through the original array and find the sum of all evens
# =====================================================================
# Note: The problem contains a typo ("events"), which refers to "evens"
sum_of_evens = 0

# Iterating through the elements using a standard loop as requested
for element in original_array:
    if element % 2 == 0:
        sum_of_evens += element

print("4. Sum of all even numbers:")
print(sum_of_evens)
