import pandas as pd
import openpyxl

df = pd.read_excel("students.xlsx")

print(df)
print("\n")

print(df.head())
print("\n")

print("Shape:", df.shape)
print("\n")

print("Marks:", df["Marks"])
print("\n")

print("Names:", df["Name"])
