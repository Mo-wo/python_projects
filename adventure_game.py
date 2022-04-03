import time
import random


# Print and delay function
def print_pause(message, secs=1):
    print(message)
    time.sleep(secs)


# Protagonist's input validation
def validate_input(prompt, options, validated_function):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        else:
            validated_function


# Protagonist is introduced to the game
def game_intro(antagonist):
    print_pause("You find yourself standing in "
                "an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {antagonist} is somewhere"
                " around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your "
                "trusty (but not very effective) dagger.\n", 2)


# Game choice messages
def choices_intro():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


# Messages to protagonist in the house
def house(antagonist, weapon):
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when"
                f" the door opens and out steps a {antagonist}.", 2)
    print_pause(f"Eep! This is the {antagonist}'s house!")
    print_pause(f"The {antagonist} attacks you!")

    if "Sword of Ogoroth" in weapon:
        print_pause("You prepare for a duel,"
                    " you make a fighting stance")
    else:
        print_pause("You feel a bit under-prepared"
                    " for this, what with only having a tiny dagger.", 2)


# Game's first choice
def first_choice(antagonist, weapon):
    house(antagonist, weapon)
    fight_choice = validate_input("Would you like to (1) fight or (2) run away?\n", ["1", "2"], first_choice)
    if fight_choice == "1":
        fight(antagonist, weapon)
    elif fight_choice == "2":
        print_pause("You run back into the field. "
                    "Luckily, you don't seem to have been followed.\n")
        field(antagonist, weapon)


# What happens when protagonist chooses to fight
def fight(antagonist, weapon):
    if "Sword of Ogoroth" in weapon:
        print_pause(f"As the {antagonist}"
                    " moves to attack, you unsheath your new sword.")
        print_pause(f"The {weapon[0]} shines brightly"
                    " in your hand as you brace yourself for the attack.")
        print_pause(f"But the {antagonist} takes one look"
                    " at your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {antagonist}."
                    " You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match "
                    f"for the {antagonist}.")
        print_pause("You have been defeated!", 2)
        print_pause("GAME OVER")
    play_again()


# Protagonist action in the field
def field(antagonist, weapon):
    choices_intro()
    protagonist_choices(antagonist, weapon)


# Game's second choice
def cave(antagonist, weapon):
    print_pause("You peer cautiously into the cave.", 3)
    if "Sword of Ogoroth" not in weapon:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        weapon.append("Sword of Ogoroth")

    else:
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")

    print_pause("You walk back out to the field.\n")
    field(antagonist, weapon)


# Protagonist makes a choice
def protagonist_choices(antagonist, weapon):
    response = validate_input("(Please enter 1 or 2)\n", ["1", "2"], protagonist_choices)

    if response == "1":
        first_choice(antagonist, weapon)
    elif response == "2":
        cave(antagonist, weapon)


# Protagonist chooses to play game again
def play_again():
    restart_choice = validate_input("Would you like to play again?"
                                    " (y/n)\n", ["y", "n"], play_again)

    if restart_choice == "y":
        print_pause("Excellent! Restarting the game ...", 3)
        play_game()
    elif restart_choice == "n":
        print_pause("Thanks for playing! See you next time.")


# Entry Point
def play_game():
    antagonist = random.choice(["troll", "pirate", "dragon",
                                " gorgon", "wicked fairie"])
    weapon = []
    game_intro(antagonist)
    choices_intro()
    protagonist_choices(antagonist, weapon)


play_game()
