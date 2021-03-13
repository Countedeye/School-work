# William Sutton
# cs15120


myList = [1,51,26,7,23,99,-2,26,41]

#printOne function
def printOne():
    for i in range(0,len(myList)):
        print(myList[i])
    

#printTwo sorting in ascending order.
def printTwo():
    for i in myList:
        print(i)

#sorting in descending order.
def sort():
    for i in myList:
        myList.sort(reverse=True)
        print(i)

#Calling each function for proof of 
printOne()
printTwo()
sort()