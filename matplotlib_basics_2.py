import matplotlib.pyplot as plt

print("Plotting a histogram")

marks = [85, 90, 78, 92, 88, 76, 95, 81, 85, 89]

plt.hist(marks)

plt.title("Marks Distribution")

plt.show()

print("Plotting a scatter plot")

hours_studied = [1, 2, 3, 4, 5]
scores = [50, 60, 70, 85, 95]

plt.scatter(hours_studied, scores)

plt.title("Study HOurs vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")

plt.show()

