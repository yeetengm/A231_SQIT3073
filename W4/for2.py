import os
os.system('cls') 
 

# List of integers
numbers = [1, 2, 3, 4, 5]
totalnumber = len(numbers)
print(totalnumber)
# For loop to iterate through the list
for num in numbers:
    square = num ** 2
    print(f"The square of {num} is {square}")

print('This show the iteration of loop in the list')

i = 0
while i < totalnumber:
    sq=numbers[i]**2
    i+=1
    print(sq)