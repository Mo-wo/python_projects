# function that takes a string and a target character, and counts the number of times the character occurs in the string using for and while loop

#For Loop
def char_in_str():
    string = input("Enter word here: ")
    target = input("Enter character to look for here: ") 
    total = 0
    for char in string:
        if char == target:
            total += 1
    return total
    #else:
     #   print("This character is not in this word")
char_in_str()
