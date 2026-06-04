import pandas as pd

df = pd.read_excel("student.xlsx")

df.sort_values("Marks")

# Who scored the second highest marks?

sorted_df = df.sort_values("Marks", ascending = False)
second_highest = sorted_df.iloc[1]

print(second_highest)