# Asks user for distance in feet.
print(" Enter a distance in feet.")
user_input1 = input()
feet = float(user_input1)

# creates values for each conversion based on feet.
inches = float(user_input1) * 12
miles = float(user_input1) / 5280
yards = float(user_input1) / 3

# asking user which conversion.
print(" Which unit would you like to convert to?")
print("Options include:")
print(" Inches.")
print(" Yards.")
print(" Miles.")

# erases whitespace in input and switches any input to lower case letters.
user_input2 = input()
user_input2 = user_input2.lower()
user_input2 = user_input2.strip()

#conditions for each conversion.
if user_input2 == "inches":    
    print(str(inches) + " in")

elif user_input2 == "yards":    
    print(str(yards) + " yd")

elif user_input2 == "miles":
    print(str(miles) + " mi")

else:
    print("Invalid unit selection \"" + user_input2 + "\".")
    exit()    