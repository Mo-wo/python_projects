import time

def print_pause(message):
    print(message)
    time.sleep(2)

#Validate Input
def valid_input(prompt, choice1, choice2):
    while True:
        response = input(prompt).lower()
        if choice1 in response:
            break
        elif choice2 in response:
            break            
        else:
            print_pause("Sorry, I don't understand this input.")
    return response


#Welcome Prompt
def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")
    
#Validate Order
def get_order():
    choice = valid_input("Please place your order, would you like waffles or pancakes?\n", "waffles", "pancakes")
    
    if "waffles" in choice:
        print_pause("Waffles it is!")
    elif "pancakes" in choice:
        print_pause("Pancakes it is!")
    
    print_pause("Your order will be ready shortly")
        
#Order Again
def order_again():
    another_choice = valid_input("Would you like to place another order? Please say 'yes' or 'no'\n", "yes", "no")

    if "no" in another_choice:
        print_pause("OK, Goodbye")
    elif "yes" in another_choice:
        print_pause("Very good, I'm happy to take another order")  
        get_order()  

def order_breakfast():
    intro()
    get_order()
    order_again()

order_breakfast()
