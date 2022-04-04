def con_cat():
    print("Hi there! Let's know you, shall we?\n")
    name = input("What is your name?\n")
    print("That is a lovely name " + name + "!\n")
    color = input("What is your favourite colour?\n")
    print("Ah! I like " + color + " too\n")
    interest = input("Tell me one of your interest?\n")
    print("I have an interest in " + interest + " too\n")

con_cat()

def fcon_cat():
    print("Hi there! Let's know you, shall we?")
    name = input("What is your name?\n")
    print(f"That is a lovely name {name} !\n")
    color = input("What is your favourite colour?\n")
    print(f"Ah! I like {color} too\n")
    interest = input("Tell me one of your interest?\n")
    print(f"I have an interest in {interest} too\n")

fcon_cat()
