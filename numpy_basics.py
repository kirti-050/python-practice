import numpy as np

#Creating an array 
marks = np.array([85, 90, 78, 92, 88])

print(marks)

#Accessing elements

print(marks[0])
print(marks[-1])

#Array slicing

print(marks[1:4])

#Numpy math functions

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))

print("Adding 5 to every element:", marks + 5)
print("Multiplying 2 to every element:", marks * 2)

# Array comparisons

print(marks > 85)

print(marks[marks > 85])
