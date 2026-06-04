txt = input("Enter a note: ")

with open ("User_note.txt", "w") as file:
    file.write(txt)
 
with open ("User_note.txt", "r") as file:
    print(file.read())