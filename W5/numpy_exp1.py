import os

try:
    # Attempt to clear the screen for macOS
    os.system('clear')
except:
    try:
        # Attempt to clear the screen for Windows if the first try fails
        os.system('cls')
    except:
        # Output an error message if both attempts fail
        print("Unable to clear the screen.")


import numpy as np  # Import the NumPy library for numerical operations

# Create 1D NumPy arrays
# Initializing 1-dimensional arrays 
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]             #如果只有list，run的话，不会算答案，只会show list。   如果是arr，就会算
arr1 = np.array(list1)    #arr是convert something into numpy  （arr是array） use list to convert it into array
arr2 = np.array([5, 4, 3, 2, 1])

print(list1 + list2)