print("Type in the name of an animal and press ENTER.")
animal = input()
print("What letter-casing would you like to use?")
print("Options include: ")
print(" upper.")
print(" lower.")
print(" title.")
casing = input()
casing = casing.lower()
if casing == "upper":
    animal = animal.upper()
elif casing == "lower":
    animal = animal.lower()
elif casing == "title":
    animal = animal.title()
else:    
    print("invalid entry")
print(animal)