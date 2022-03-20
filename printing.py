hello = input("Hello and Welcome. What is your name?")
print("Welcome,", hello, "!")
question = input("Are you good at math?")
if (question == "Yes"):
    answer = input("Answer this question: 1045 + 2022")
    if (answer == "3067"):
        print("You really are good at math!")
    else:
        print("Are you really good at math?")
elif(question == "No"):
    print("Only math gurus are acceptable. Bye!")
else:
    print("You need to be certain of your math skills, It is either a yes or no!")
