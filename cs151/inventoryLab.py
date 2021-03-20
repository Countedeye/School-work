# William Sutton
# cs15120

# Inventory list
myInv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# function for displaying inventory
def displayInventory(myInv):
    # variable that helps add inventory from 0.
    sum = 0
    print("Inventory:")
    # for loop that adds inventory and displays key and values.
    for i in myInv:
        sum = int(dict(myInv)[i]) + int(sum)
        print(str(dict(myInv)[i]) + " " + str(i))
    # displayed the added value of inventory
    print("Total number of items in inventory: "+ str(sum))

#calls the function.
displayInventory(myInv)
