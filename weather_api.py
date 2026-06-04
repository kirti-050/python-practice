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
print("\n")

print(data["current_condition"][0])
print("\n")

print("Temperature in Celsius:", data["current_condition"][0]["temp_C"])
print("\n")

print("Temperature in Fahrenheit:", data["current_condition"][0]["temp_F"])
print("\n")

print("Weather Description:", data["current_condition"][0]["weatherDesc"][0]["value"])
print("\n")

print("Humidity:", data["current_condition"][0]["humidity"])
