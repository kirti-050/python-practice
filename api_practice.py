import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()

print(data)
print("\n")

print(data["fact"])
print("\n")

print(data["length"])
