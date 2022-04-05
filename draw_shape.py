import turtle
import time

def print_pause(message, sec=1.5):
    print(message)
    time.sleep(sec)


# def program_intro(color, sides, length, angle, turtle_name="george"):
#     print_pause("Welcome to Turtle graphics\n"
#     "I can help you draw any shape with a few details")
#     turtle_name = input("What would you like to call your turtle\n").lower()
#     color = input("What color do you want your shape in?\n").lower()
#     sides = int(input("How many sides should your shape have?\n"))
#     length = int(input("What will the length of each side be?\n"))
#     angle = int(input("Enter an angle\n"))


def shape_program(color, sides, length, angle, turtle_name="george"):
    turtle_name = turtle.Turtle()
    turtle_name.color(color)
    turtle_name.penup()
    turtle_name.back(50)
    turtle_name.pendown()
    for side in range(sides):
        turtle_name.forward(length)
        turtle_name.right(angle)


# def draw_shape(color, sides, length, angle, turtle_name="george"):
#     shape_program(color, sides, length, angle, turtle_name="george")


# draw_shape("yellow", 0, 0, 0, "turtle_name")

shape_program("cyan", 8, 50, 45, "turtle_name")
turtle_name="george"

shape_program("yellow", 5, 50, 72, "mowo")

shape_program("green", 3, 50, 120, "mowo")