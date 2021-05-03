import random 


def printLetters(text):
    #loops through text that is called line by line.
    for i in text:
        #prints each letter in the text on separate lines.
        print(i)
    
def countLetter(myText,letter):
    #keeps track of how many letters are in the text.
    counter = 0
    #loops through myText and checks each character.
    for i in myText:
        if i == letter:
            #keeps a counter of how many times that character matches.
            counter = counter + 1
    return counter

def removeSpaces(myText):
    # creates a list of words from myText
    userText = myText.split()
    #Sets myText to empty to store new string.
    myText = ""
    for val in userText:
        #appends each word in userText to myText.
        myText = myText + val
    return myText


def ASCIICode():
    #List of letters that can be read.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in alphabet:
        #prints the alphabet plus the ASCII value of each character in the list.
        print(i + " " + str(ord(i)))



def countDown(n):
    #This allows a code to begin at the end and read backwards by one.
    for i in range (n,-1,-1):
        #This stops the code at 1 
        if i >= 1:
            print(str(i))
        else:
            print("Blast-off!")   


def addUp(n):
    sum = 0
    #n+1 includes n when the code begins to add each number.
    for i in range(n+1):
        sum = sum + i
    return sum
            

def pwdCheck():
    userInput = input("What is your password?")
    # will continue to loop until the answer is correct.
    while userInput != "please":
        userInput = input("Wrong password, Try again.")


def additionFacts(x):
    for i in range(x):
        randint1 = random.randint(1,20)
        randint2 = random.randint(1,20)
        sum = randint1 + randint2
        print(f"{randint1} + {randint2} = {sum}")



def headsCount():
    numHeads = 0
    heads = 1
    tails = 2
    for i in range(10):
        coinflip = random.randint(1,2)
        if coinflip == heads:
            numHeads += 1
            print("heads")
        elif coinflip == tails:
            print("tails")
    return numHeads


def mathQuiz():
    random1 = random.randint(1,20)
    random2 = random.randint(1,20)
    sum = random1 + random2
    userInput = input(f"{random1} + {random2} = ")
    if int(userInput) == sum:
        print("Correct")
    else:
        print("Incorrect")

def powersOfX(X):
    for i in range(10):
        power = X**i
        print(power)


def factorials(X):
    factorial = 1
    
    if X < 1000000:
        #start at 1 and end at x+1.
        for i in range(1,X+1):
            factorial = factorial * i 
        print(factorial)
    else:
        print("Error message.")

def factors():
    userInput = int(input("input an integer. "))
    for i in range(1,userInput+1):
        if userInput%i == 0:
            print(i)

def isPrime():
    userInput = int(input("Input an integer. "))
    factorList = []
    for i in range(1,userInput+1):
        # if a factor is found, add it to list.
        if userInput%i == 0:
            factorList.append(i)
    #if size of factor list is 2, then it is prime.
    if len(factorList) == 2:
        return True
    else:
        return False     

def sortIt(myFile):
    #reads the entire file into fileString.
    fileString= myFile.read()
    words= fileString.split()
    # sorts the list.
    for i in range(len(words)):
        # start at 1 + i so you dont compare the same element.
        for x in range(i+1,len(words)):
            # if the current element at i is greater than element at x, the code swaps values.
            if int(words[i]) > int(words[x]):
                temp = words[i]
                words[i] = words[x]
                words[x] = temp
    print(words)


def rectangle(x,y):
    rectangle = ""
    for i in range(x):
        for z in range(y):    
            #if first row or last row print all astricks.
            if i == 0 or i == x-1: 
                rectangle = rectangle + "*"
            else:
                # if first or last element of row add astrick.
                if z == 0 or z == y-1:
                    rectangle = rectangle + "*"    
                # add space instead of astrick.
                else:
                    rectangle = rectangle + " "    
        print(rectangle)
        rectangle = ""



def randomCoinTrial(X):
    numHeads = 0
    heads = 1
    #loops 10 times.
    for val in range(10):
        #loop x times on the 10.
        for i in range(X):
            coinflip = random.randint(1, 2)
            if coinflip == heads:
                numHeads += 1
    print(numHeads)        
    #finds the percent by dividing the number of heads by the total times ran.
    percent = float(numHeads) / X*10        
    print(f"{percent} %")


#randomCoinTrial(5)

# testing code
#rectangle(5, 7)
#myFile = open("number.txt", "rt")
#sortIt(myFile)
#print(isPrime())
#factors()
#factorials(4)
#powersOfX(2)
#mathQuiz()
#print(headsCount())
#additionFacts(10)
#text = "this is a string."
#printLetters(text)
#myText = "Test."
#letter = 's'
#test = print(countLetter(myText,letter))
#countLetter(myText,letter)
#print(removeSpaces(myText))
#ASCIICode()
#n = 10
#countDown(n)
#print(addUp(n))
#pwdCheck()
