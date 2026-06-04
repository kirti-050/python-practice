import pandas as pd

df = pd.read_excel("student.xlsx")
a = 0
m = (df["Marks"])

for i in m:
    a = a + i
print("Average marks:", a/len(m))

print("\n")

sorted_df = df.sort_values("Marks", ascending = False)
print("Highest Marks:", sorted_df.iloc[0])

print("\n")

print("Lowest Marks:", sorted_df.iloc[-1])

print("\n")

print("Students above 80 marks:", df[df["Marks"] > 80][["Name", "Marks"]])
