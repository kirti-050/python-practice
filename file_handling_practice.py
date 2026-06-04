txt = input("Enter a note: ")

with open ("User_note.txt", "w") as file:
    file.write(txt)

# to add more notes without replacing the old one 
# just write "a" instead of "w"

with open ("User_note.txt", "r") as file:
    print(file.read())