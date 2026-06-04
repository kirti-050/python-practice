import requests

response = requests.get("https://api.github.com/users/octocat")

data = response.json()

print(data.keys())

print("\n")
print("Github Username:", data["login"])

print("\n")
print("Public Repositories:",data["public_repos"])

print("\n")
print("Followers:", data["followers"])

print("\n")
print("Following:", data["following"])
