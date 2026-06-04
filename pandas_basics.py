import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Clair"],
    "Age": [25, 33, 20],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

print(df)
print("\n")

print(df.head())
print("\n")

print(df.shape)
print("\n")

print(df.columns)
print("\n")

print(df.describe())