# file = open("new_file.txt", "w")
# file.write("Writing some text into this file")
# file.close()

# file = open("new_file.txt")
# print(file.read())
# file.close()

with open("old_file.txt") as old_file:
    old_content = old_file.read()

with open("new_file.txt", "w") as new_file:
    new_file.write(old_content)

with open("new_file.txt") as new_file:
    new_content = new_file.read()

print(new_content)

# Alternative Method
with open("old_file.txt") as old_file:
    with open("new_file.txt", "w") as new_file:
        new_file.write(old_file.read())

with open("new_file.txt") as new_file:
    print(new_file.read())
