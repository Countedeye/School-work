# William Sutton
# cs15120

import time

# Inventory list
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#introductions with user
name = input("Welcome traveler! You've come a long way. What is your name?")
print("Hello " + name + ", it is nice to meet you. As a kind gesture, I'd like to give you some inventory.")


# function for displaying inventory
def displayInventory(inventory):
    # variable that helps add inventory from 0.
    sum = 0
    print("Inventory:")
    # for loop that adds inventory and displays key and values.
    time.sleep(1)
    for i in inventory:
        sum = int(dict(inventory)[i]) + int(sum)
        print(str(dict(inventory)[i]) + " " + str(i))
    # displayed the added value of inventory
    print("Total number of items in inventory: "+ str(sum))



# function that adds some inventory.
def addToInventory(inventory,addedItems):

# we are adding all the items from the 'addedItems'list
    # and add them to 'inventory' (a dictionary)
    
    time.sleep(1)
    print("New Inventory:")
    
    #This increments inventory value by 1 into current dictionary value
    for i in (addedItems):
        if i in inventory.keys():
            inventory[i] = dict(inventory)[i] + 1
        else: 
            inventory[i] = 1   
    displayInventory(inventory)
    return inventory

# function that adds multiple items to dictionary.
def addDictToInventory(inventory,addedItems):
    #adds a one second timer for user interface visual.
    time.sleep(1)
    print("New Inventory:")
    
    #This increments inventory value by 1 into current dictionary value
    for i in (addedItems):
        if i in inventory.keys():
            inventory[i] = dict(inventory)[i] + addedItems[i]
        else: 
            inventory[i] = addedItems[i]  
    displayInventory(inventory)
    return inventory


# function that gathers loot from user input
def gatherLoot():   
    # Ask user for input of adding to inventory
    # This creates a user dictionary.
    userdict = {}
    user_choice = input("Would you like to purchase items from me? Type Y if you would like to enter items one at a time, or type m for multiple values per item.")
    if user_choice == 'y'or user_choice == 'Y':   
        answer = input("Enter items that you would like to add to your loot. Type D when done.")
        # strips whitespace and changes input to lower case to eliminate errors.
        answer = answer.strip()
        answer = answer.lower()
        # begins the unlimited loop.
        while answer != 'd' and answer != 'D':
            if answer in userdict.keys():
                userdict[answer] = dict(userdict)[answer] + 1
            else:
                userdict[answer] = 1
            answer = input()  
            answer = answer.strip()
            answer = answer.lower()     
    elif user_choice == 'm' or user_choice == 'M':
        # user input with striped white space and lower case for no errors. 
        answer = input("Enter an item to add to your loot. Type D when done.   ")
        answer = answer.strip()
        answer = answer.lower()
        # allows user to input a value.
        value = input("Enter amount of item you want to purchase.   ")
        while answer != 'd' and answer != 'D':
            # checks to see if input is in dictionary labeled userdict, and answer.
            if answer in userdict.keys():
                # adds user input key and value.
                userdict[answer] = dict(userdict)[answer] + int(value)
            else:
                userdict[answer] = int(value)
            # user input with striped white space and lower case for no errors.
            answer = input("Enter an item to add to your loot. Type D when done.  ")
            answer = answer.strip()
            answer = answer.lower()
            # helps the while loop stop.
            if answer != 'd':
                value = input("Enter amount of item you want to purchase.   ")
    return userdict


#calls the functions and main code.
addedItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(inventory)
time.sleep(2)
print("Oops! I totally forgot this wonderful loot I have no need of. Here are some more items... ")
inventory = addToInventory(inventory,addedItems)
userdict = gatherLoot()
print("Thank you for your business. Here are your items.")
inventory = addDictToInventory(inventory,userdict)
