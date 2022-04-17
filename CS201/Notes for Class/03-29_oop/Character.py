#!/usr/bin/env python3

from termcolor import colored as colorize

class Character:
    # Initializer or Constructor
    def __init__(self, name, color=None, background_color=None):
        # attributes (variables attached to an object instance)
        self.name = name
        self.color = color if color else "white"
        self.background_color = background_color if background_color else "grey"
        self.colorized_name = colorize(
            self.name,
            self.color,
            f"on_{self.background_color}",
        )
        self.greeting = f'Hello, friend, my name is {self.name}!'
        self.health = 10

    def __str__(self):
        return f"{self.colorized_name} ({self.health}) [{self.color}, {self.background_color}]"

    # instance methods (functions attached to an object instance)
    def speak(self, msg):
        print(f'{self.colorized_name} says, "{msg}".')

    def emote(self, action):
        print(f"{self.colorized_name} {action}.")

    def display_health(self):
        print(f"{self.colorized_name}'s Health:")
        health_bar = colorize(' ' * self.health, 'white', 'on_'+self.color)
        print(f"{self.health: >4} - {health_bar}")

    def say_hello(self):
        self.speak(self.greeting)

    def slap(self, char):
        self.emote(f"slaps {char.colorized_name} for 1 point of smacking damage! **SLAP**")
        char.health -= 1
        char.display_health()




if __name__ == "__main__":

    # Create an instance of the class (object)
    alice = Character("Will", "red")
    bob = Character("Chris", "blue")

    print(alice)
    print(bob)

    print(type(alice))
    print(type(bob))

    # Is it an instance?
    print(type(alice) is Character)

    # Avoid adding attributes after instantiation
    # alice.name = "Alice"

    print(alice.name)
    print(bob.name)

    print("---------------------------")

    alice.speak("Hello!")
    Character.speak(bob, "Hello!")

    print("---------------------------")

    alice.say_hello()
    bob.say_hello()

    alice.emote("extends hand to shake")
    bob.emote("shakes hand")

    alice.display_health()
    bob.display_health()

    alice.slap(bob)
