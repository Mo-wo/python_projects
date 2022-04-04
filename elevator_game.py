import time

def print_pause(message):
    print(message)
    time.sleep(2.5)

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")

#Response 1
def first_floor(items):
    print_pause("You pushed the button for the first floor.")
    print_pause("After a few moments, you'll find yourself in the lobby.")
    
    if "ID Card" in items:
        print_pause("The clerk greets you, but she has already given you your ID card, so there is nothing more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID card.")
        items.append("ID Card")
    print_pause("You head back to the elevator.")
    ride_elevator(items)

#Response 2
def second_floor(items):
    print_pause("You pushed the button for the second floor.")
    print_pause("After a few moments, you'll find yourself in the human resources department.")
    
    if "Handbook" in items:
        print_pause("The HR folks are busy at their desks.") 
        print_pause("There doesn't seem to be much to do here.") 

    else:
        print_pause("The head of HR greets you.") 
        if "ID Card" in items:
            print_pause("He looks at your ID card and then"
            " gives you a copy of the employee handbook.")
            items.append("Handbook")
        else:
            print_pause("He has something for you, but says he can't"
            " give it to you until you go get your ID card.")
       
    print_pause("You head back to the elevator.")
    ride_elevator(items)

#Response 3
def third_floor(items):
    print_pause("You pushed the button for the third floor.")
    print_pause("After a few moments, you'll find yourself in the engineering department.")

    if "Handbook" in items and "ID Card" in items:
        print_pause("Fortunately, you got that from HR!")
        print_pause("Congratulatons! You are ready to start your new job as vice president of engineering!")
    else:
        if "ID Card" not in items and "Handbook" not in items:
            print_pause("Unfortunately, the door is locked "
            "and you can't get in.")
            print_pause("It looks like you need some kind of key card to open the door.")
            print_pause("You head back to the elevator.")
            ride_elevator(items)

        elif "ID Card" in items and "Handbook" not in items:
            print_pause("You use your ID card to open the door.")
            print_pause("Your program manager greets you and tells you that you need to have a copy of the employee handbook in order to start work.")
            ride_elevator(items)
                 
        else:
            print_pause("They scowl when they see that you don't have it, and send you back to the elevator.")
            ride_elevator(items)

def ride_elevator(items):
    print_pause("Please enter the number for the floor you would like to visit:")
    response = input("1. Lobby\n"
                    "2. Human resources\n"
                    "3. Engineering department\n")
     
    if response == "1":
       first_floor(items) 
    elif response == "2":
        second_floor(items)
    elif response == "3":
        third_floor(items)
    else:
        print_pause("That floor does not exist") 

    print_pause("Where would you like to go next?")
    ride_elevator(items) 

def play_game():
    items = []
    intro()
    ride_elevator(items)           

play_game()


