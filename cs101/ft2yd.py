#receive input from user.
print("Please enter a distance in feet.")
user_input = input()

#creating a variable for feet
feet = float(user_input)

#creating a variable for yards.
yard = float(user_input) / 3

#sends user answer in yards.
print("The distance you chose is " + str(yard) + " yd.")