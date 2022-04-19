class Dog:
    limbs = 4

    def __init__(self, name):
        self.name = name
        self.bark = 0

    def speak(self):
        print("BOWOW!")

    def count(self):
        self.bark += 1   
        for number in range(self.bark):
            self.speak() 
    

    def eat(self, food):
        food_list = ["biscuit", "bone", "meat", "dogfood"]
        if food in food_list:
            print("Yummy!")
        else:
            print("That's not food!")

    def hear_name(self, words):
        if self.name in words:
            self.speak()

class Retriever(Dog):
    body_color = "ombre"
    origin = "US"

    def speak(self):
        print("Woof!")

class DogPark:
    def __init__(self, dogs):
        self.dogs = dogs

    def rollcall(self):
        print("Dogs in Park:")
        for dog in self.dogs:
            print(f"{dog.name}")
        print()

    # Write the shout method here!
    def shout(self, words):
        for dog in self.dogs:
            dog.hear_name(words)

    def converse(self):
        self.rollcall()
        while True:
            words = input("Talk to doggos! ('quit' to quit) > ")
            if 'quit' in words:
                print("Bye!")
                break
            else:
                self.shout(words)


if __name__ == '__main__':
    dogs = [animals.Husky("Toklat"),
            animals.Chihuahua("Scrappy"),
            animals.Labrador("Barrett")]
    park = DogPark(dogs)
    park.converse()


class Cat:

    def __init__(self, mood="neutral"):
        self.mood = mood

    def speak(self):
        if self.mood == "neutral":
            print("Meow!")
        elif self.mood == "happy":
            print("Purrrrrr")
        elif self.mood == "angry":
            print("Hisssss!")
        else:
            print("Loud Hisssss!")