with open ("notes.txt", "w") as file:
    file.write("Welcome to Python programming!")

with open ("notes.txt", "r") as file:
    print(file.read())
