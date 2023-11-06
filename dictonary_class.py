import os
os.system('clear') 


# Create a dictionary of student information
student = {
    "name": "Alice",
    "age": int(20),
    "major": "Computer Science",
    "grades": {
        "math": 95,
        "english": 88,
        "history": 92
    }
}

#From ChatGPT
math_grade = student["grades"]["math"]
print(math_grade)

#a = print(student["grades"])
#print(a["math"])

# Access dictionary values by keys
#student_name = student["name"]
#student_age = student["age"]