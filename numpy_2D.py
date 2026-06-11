import numpy as np

students = np.array([
    [85, 90, 78],
    [92, 88, 76], 
    [95, 81, 89]
])

print(students)

# Accessing elements

print("Second element of first row:", students [0][1]) #second element of first row

print("Accessing entire second row:", students[1]) #accessing entire second row

print("Accessing first column:", students [:, 0]) #accessing first column

# Calculating statistics across rows and columns

print("Average of all 9 numbers:", np.mean(students)) # averages all 9 numbers

print("Average of each student(rows):", np.mean(students, axis = 1)) #average of each student(rows)

print("Average of each subject(columns):", np.mean(students, axis = 0)) #average of each subject(columns)
