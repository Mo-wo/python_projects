import time

def print_pause(message):
    print(message)
    time.sleep(2.5)

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")

def validate_floor_input(prompt, opt1, opt2, opt3):
    while True:
        response = input(prompt).lower()
        if opt1 in response:
            break
        elif opt2 in response:
            break
        elif opt3 in response:
            break
        else:
            print_pause("This floor does not exist")
            goto_floor()
    return response

def goto_floor():
    print_pause("Please enter the number for the floor you would like to visit:")
    message = validate_floor_input(
        "1. Lobby\n"
        "2. Human resources\n"
        "3. Engineering department\n", "1", "2", "3")
    if "1" in message:
        print_pause("You pushed the button for the first floor.")
        print_pause("After a few moments, you'll find yourself in the lobby.")
    elif "2" in message:
        print_pause("You pushed the button for the second floor.")
        print_pause("After a few moments, you'll find yourself in the human resources department.")
    elif "3" in message:
        print_pause("You pushed the button for the third floor.")
        print_pause("After a few moments, you'll find yourself in the engineering department.")
    another_floor()

def another_floor():
    print_pause("Where would you like to go next?")
    goto_floor()

def use_elevator():
    intro()
    goto_floor()
    another_floor()

use_elevator()