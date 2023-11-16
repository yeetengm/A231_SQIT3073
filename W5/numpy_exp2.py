
import numpy as np  # Import the NumPy library for numerical operations

# Create 1D NumPy arrays
# Initializing 1-dimensional arrays 
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
arr1 = np.array(list1)    #arr是convert something into numpy  （arr是array） use list to convert it into array
arr2 = np.array([5, 4, 3, 2, 1])
arr3 = np.array([2, 2, 2, 2, 2])

print(arr1 + arr2 * arr3)