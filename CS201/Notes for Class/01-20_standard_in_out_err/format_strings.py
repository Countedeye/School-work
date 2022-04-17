#!/usr/bin/env python3

person1 = {
    "first": "Alice",
    "last": "Alison",
    "age": 19,
    "animal": "dogs",
}

person2 = {
    "first": "Bob",
    "last": "Roberts",
    "age": 20,
    "animal": "cats",
}

# String concatenation
print(person1["first"] + " " + person1["last"] + " is " + str(person1["age"]) + " years old and likes " + person1["animal"] + "!")

print(f'{person2["first"]} {person2["last"]} is {person2["age"]} years old and likes {person2["animal"]}!')
