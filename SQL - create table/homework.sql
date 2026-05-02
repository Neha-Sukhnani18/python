import numpy as np

# Create an array
arr = np.array([10, 15, 20, 25, 30])

# Replace values: if greater than 20, use 1; else use 0
result = np.where(arr > 20, 1, 0)
print(result)  # Output: [0 0 0 1 1]
