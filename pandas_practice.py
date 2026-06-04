import pandas as pd

df = pd.read_excel("student.xlsx")

print(df.head())
print("\n")

print(df.tail())
print("\n")

print(df.info())
print("\n")

print(df.describe())
print("\n")

print(df["Marks"])
print("\n")

print(df[df["Marks"] > 80])
print("\n")

print(df[df["City"] == "Delhi"])
