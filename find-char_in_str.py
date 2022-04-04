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

#While Loop
def char_in_str_2():
    string = input("Enter word here: ")
    target = input("Enter character to look for here: ") 
    total = 0
    index = 0
    while index < len(string):
        if index == target:
            total += 1
         index += 1
    return total

#Select loop
def loop_choice():
    selection = input("Which loop would you prefer to find your character in your string? while/for? \n").lower()
    if selection == "for":
        print(char_in_str())
    elif selection == "while":
        print(char_in_str_2())
    else:
        print("Invalid loop selection")
        loop_choice()
        
loop_choice()
        
