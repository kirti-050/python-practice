import matplotlib.pyplot as plt

print("Plotting a bar chart")

subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]

plt.bar(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()


print("Plotting a line chart")

days = [1, 2, 3, 4, 5]
scores = [70, 75, 80, 85, 90]

plt.plot(days, scores, marker = 'o')

plt.title("Score Improvement")
plt.xlabel("Day")
plt.ylabel("Score")

plt.show()

print("Mini Project: Learning Progress Tracker")

days = [1, 2, 3, 4, 5, 6, 7]
problems_solved = [3, 5, 7, 9, 9, 11, 11]

plt.plot(days, problems_solved, marker = 'o')

plt.title("LeetCode Progress")
plt.xlabel("Day")
plt.ylabel("Problems Solved")

plt.show()

print("Plotting a pie chart")

activities = ["Python", "LeetCode", "Projects"]
hours = [10, 6, 8]

plt.pie(hours, labels = activities, autopct = "%1.1f%%")

plt.title("Study Time Distribution")

plt.show()

