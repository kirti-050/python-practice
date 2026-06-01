import requests

response = requests.get("https://wttr.in/Lucknow?format=j1")

data = response.json()

print(data.keys())
print("\n")

print(data["current_condition"])
print("\n")

print(type(data["current_condition"]))
print("\n")

print(data["current_condition"][0].keys())

print(data["current_condition"][0])
