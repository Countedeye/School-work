'''You will be creating a list of numbers in a variable called " myList ",
defined below.

myList = [1, 51, 26, 1, 23, 16, 7, 23, 99, -2, 26, 44]

Create the following functions which perform operations on myList
printOne - Print each item in the list.
printTwo - prints each item in the list, using a different way than you used in\
    the printOne function
sort - Sort the list of numbers in descending order.'''

myList = [1,51,26,7,23,99,-2,26,41]


#printOne
print(myList)

#printTwo sorting in ascending order.
print(sorted(myList))

#sorting in descending order.
print(sorted(myList, reverse=True))
